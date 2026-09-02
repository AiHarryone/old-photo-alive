// exif-strip.js — lossless photo metadata stripper (JPEG / PNG / WebP) + detector.
// Pure byte-level, no dependencies. Works in the browser and in Node (UMD).
//   stripMeta(buf, {keepICC}) -> { buffer, removed:[names], before, after }
//   detectMeta(buf)           -> { type, exif, xmp, icc, gps, orientation, make, model, datetime, jpegInfo }
// Why lossless: we remove only the metadata container chunks/segments and copy every
// image pixel byte verbatim — no re-encode, no quality loss.
(function (root) {
  'use strict';

  function bytesToAscii(u8, from, len) {
    var s = '';
    for (var i = from; i < from + len; i++) s += String.fromCharCode(u8[i]);
    return s;
  }
  function asciiAt(u8, from, str) {
    if (from + str.length > u8.length) return false;
    for (var i = 0; i < str.length; i++) if (u8[from + i] !== str.charCodeAt(i)) return false;
    return true;
  }
  function concat(ranges) {
    var total = 0, i;
    for (i = 0; i < ranges.length; i++) total += ranges[i][1] - ranges[i][0];
    var out = new Uint8Array(total);
    var o = 0;
    for (i = 0; i < ranges.length; i++) {
      var s = ranges[i][0], e = ranges[i][1];
      out.set(ranges[i].u8 ? ranges[i].u8 : new Uint8Array(0), o); // placeholder replaced below
    }
    return out;
  }

  // Copy [s,e) from src into a fresh Uint8Array.
  function slice(src, s, e) {
    var out = new Uint8Array(e - s);
    out.set(src.subarray(s, e));
    return out;
  }

  // ---------- JPEG ----------
  var SEG_NAMES = {
    0xE0: 'APP0 JFIF', 0xE1: 'EXIF/XMP (APP1)', 0xE2: 'APP2', 0xED: 'Photoshop/IPTC (APP13)',
    0xFE: 'Comment', 0xDB: 'DQT', 0xC4: 'DHT', 0xDA: 'SOS'
  };
  function jpegName(m) { return SEG_NAMES[m] || ('0xFF' + m.toString(16)); }

  // Returns array of {m, start, end, drop} decisions then rebuild.
  function scanJpeg(u8, keepICC) {
    var i = 2, removed = [];
    var keep = [{ s: 0, e: 2 }]; // SOI
    while (i + 4 <= u8.length) {
      if (u8[i] !== 0xFF) { keep.push({ s: i, e: u8.length }); break; } // misaligned -> keep rest
      var m = u8[i + 1];
      if (m === 0xD8) { i += 2; continue; }           // dup SOI
      if (m === 0xD9) { keep.push({ s: i, e: u8.length }); break; }  // EOI
      if (m === 0xDA) { keep.push({ s: i, e: u8.length }); break; }  // SOS: rest is entropy + EOI
      if ((m >= 0xD0 && m <= 0xD7) || m === 0x01) { i += 2; continue; } // standalone
      if (i + 4 > u8.length) { keep.push({ s: i, e: u8.length }); break; }
      var segLen = (u8[i + 2] << 8) | u8[i + 3];
      var segEnd = i + 2 + segLen;
      if (segEnd > u8.length) { keep.push({ s: i, e: u8.length }); break; }
      var drop = false;
      if (m === 0xE1) drop = true;                     // EXIF + XMP
      else if (m === 0xED) drop = true;                // Photoshop / IPTC
      else if (m === 0xFE) drop = true;                // comment
      else if (m === 0xE2) {                           // APP2: keep ICC profile if allowed, drop MPF etc
        if (!keepICC) drop = true;
        else if (!asciiAt(u8, i + 4, 'ICC_PROFILE\x00')) drop = true;
      }
      if (drop) removed.push(jpegName(m));
      else keep.push({ s: i, e: segEnd });
      i = segEnd;
    }
    return { keep: keep, removed: removed };
  }

  // Shallow EXIF read: endian, IFD0 tags make/model/datetime/orientation/GPS-pointer.
  function readJpegExif(u8, segStart, segEnd) {
    var p = segStart;
    // marker + len already known; payload starts at p+4 (after FF E1)
    if (!asciiAt(u8, p + 4, 'Exif\x00\x00')) return null;
    var t = p + 10;                                    // TIFF header
    if (t + 8 > segEnd) return null;
    var little = (u8[t] === 0x49 && u8[t + 1] === 0x49); // II vs MM
    function u16(o) { return little ? (u8[o] | (u8[o + 1] << 8)) : ((u8[o] << 8) | u8[o + 1]); }
    function u32(o) {
      return little
        ? (u8[o] | (u8[o + 1] << 8) | (u8[o + 2] << 16) | (u8[o + 3] << 24))
        : ((u8[o] << 24) | (u8[o + 1] << 16) | (u8[o + 2] << 8) | u8[o + 3]);
    }
    if (u16(t + 2) !== 42) return null;
    var ifd0 = t + u32(t + 4);
    if (ifd0 + 2 > segEnd) return null;
    var n = u16(ifd0);
    var info = { make: null, model: null, datetime: null, orientation: null, gps: false };
    var i;
    for (i = 0; i < n; i++) {
      var e = ifd0 + 2 + i * 12;
      if (e + 12 > segEnd) break;
      var tag = u16(e), type = u16(e + 2), cnt = u32(e + 4);
      var valOff = e + 8;
      if (tag === 0x0112 && type === 3 && cnt === 1) info.orientation = little ? u8[valOff] : u8[valOff + 1]; // SHORT
      else if (tag === 0x8825) info.gps = true;        // GPS IFD pointer present
      else if (tag === 0x010F && type === 2) info.make = readAscii(u8, t + u32(valOff), Math.min(cnt, 64), segEnd);
      else if (tag === 0x0110 && type === 2) info.model = readAscii(u8, t + u32(valOff), Math.min(cnt, 64), segEnd);
      else if (tag === 0x0132 && type === 2) info.datetime = readAscii(u8, t + u32(valOff), Math.min(cnt, 32), segEnd);
    }
    return info;
  }
  function readAscii(u8, off, len, limit) {
    if (off + len > limit) return null;
    return bytesToAscii(u8, off, len).replace(/\x00+$/, '') || null;
  }

  function stripJpeg(buf, keepICC) {
    var u8 = new Uint8Array(buf);
    var scan = scanJpeg(u8, keepICC);
    var ranges = scan.keep;
    var total = 0, i;
    for (i = 0; i < ranges.length; i++) total += ranges[i].e - ranges[i].s;
    var out = new Uint8Array(total);
    var o = 0;
    for (i = 0; i < ranges.length; i++) {
      var s = ranges[i].s, e = ranges[i].e;
      out.set(u8.subarray(s, e), o);
      o += e - s;
    }
    return { buffer: out.buffer, removed: scan.removed, before: buf.byteLength, after: out.byteLength };
  }

  function detectJpeg(buf) {
    var u8 = new Uint8Array(buf);
    var exif = null, icc = false, xmp = false, i = 2, metaCount = 0;
    while (i + 4 <= u8.length) {
      if (u8[i] !== 0xFF) break;
      var m = u8[i + 1];
      if (m === 0xDA || m === 0xD9) break;
      if ((m >= 0xD0 && m <= 0xD7) || m === 0x01) { i += 2; continue; }
      var len = (u8[i + 2] << 8) | u8[i + 3];
      var end = i + 2 + len;
      if (end > u8.length) break;
      if (m === 0xE1) {
        metaCount++;
        if (asciiAt(u8, i + 4, 'Exif\x00\x00')) exif = readJpegExif(u8, i, end) || { gps: false };
        else if (asciiAt(u8, i + 4, 'http://ns.adobe.com/xap/1.0/')) xmp = true;
      } else if (m === 0xE2 && asciiAt(u8, i + 4, 'ICC_PROFILE\x00')) icc = true;
      else if (m === 0xED || m === 0xFE) metaCount++;
      i = end;
    }
    return { type: 'jpeg', exif: !!exif, xmp: xmp, icc: icc, gps: !!(exif && exif.gps),
      orientation: exif && exif.orientation ? exif.orientation : null,
      make: exif && exif.make, model: exif && exif.model, datetime: exif && exif.datetime,
      metaCount: metaCount };
  }

  // ---------- PNG ----------
  function pngChunkType(u8, off) { return bytesToAscii(u8, off + 4, 4); }
  var PNG_DROP = { tEXt: 1, zTXt: 1, iTXt: 1, eXIf: 1, tIME: 1 };
  function detectPng(buf) {
    var u8 = new Uint8Array(buf);
    var off = 8, found = [];
    while (off + 8 <= u8.length) {
      var len = ((u8[off] << 24) | (u8[off + 1] << 16) | (u8[off + 2] << 8) | u8[off + 3]);
      if (len < 0) break;
      var t = pngChunkType(u8, off);
      var end = off + 12 + len;
      if (end > u8.length) break;
      if (PNG_DROP[t]) found.push(t);
      if (t === 'IEND') break;
      off = end;
    }
    return { found: found };
  }
  function stripPng(buf) {
    var u8 = new Uint8Array(buf);
    var ranges = [{ s: 0, e: 8 }];
    var off = 8, removed = [];
    while (off + 8 <= u8.length) {
      var len = ((u8[off] << 24) | (u8[off + 1] << 16) | (u8[off + 2] << 8) | u8[off + 3]);
      if (len < 0) break;
      var t = pngChunkType(u8, off);
      var end = off + 12 + len;
      if (end > u8.length) break;
      if (PNG_DROP[t]) removed.push(t);
      else ranges.push({ s: off, e: end });
      if (t === 'IEND') break;
      off = end;
    }
    var total = 0, i;
    for (i = 0; i < ranges.length; i++) total += ranges[i].e - ranges[i].s;
    var out = new Uint8Array(total);
    var o = 0;
    for (i = 0; i < ranges.length; i++) { out.set(u8.subarray(ranges[i].s, ranges[i].e), o); o += ranges[i].e - ranges[i].s; }
    return { buffer: out.buffer, removed: removed, before: buf.byteLength, after: out.byteLength };
  }

  // ---------- WebP ----------
  var WEBP_DROP = { 'EXIF': 1, 'XMP ': 1 };
  function detectWebp(buf) {
    var u8 = new Uint8Array(buf);
    if (u8.length < 12 || bytesToAscii(u8, 0, 4) !== 'RIFF' || bytesToAscii(u8, 8, 4) !== 'WEBP') return null;
    var found = [];
    // Simple (non-animated) files may store EXIF/XMP after image chunk.
    var off = 12;
    while (off + 8 <= u8.length) {
      var fourcc = bytesToAscii(u8, off, 4);
      var size = (u8[off + 4] | (u8[off + 5] << 8) | (u8[off + 6] << 16) | (u8[off + 7] << 24));
      var end = off + 8 + size + (size & 1);
      if (end > u8.length) break;
      if (fourcc === 'EXIF' || fourcc === 'XMP ') found.push(fourcc.trim());
      if (fourcc === 'VP8 ' || fourcc === 'VP8L' || fourcc === 'VP8X' || fourcc === 'ANMF') { off = end; continue; }
      off = end;
    }
    return { found: found };
  }
  function stripWebp(buf) {
    var u8 = new Uint8Array(buf);
    var ranges = [], off = 0, removed = [];
    if (u8.length < 12 || bytesToAscii(u8, 0, 4) !== 'RIFF' || bytesToAscii(u8, 8, 4) !== 'WEBP') {
      return { buffer: buf, removed: [], before: buf.byteLength, after: buf.byteLength };
    }
    ranges.push({ s: 0, e: 12 });
    off = 12;
    while (off + 8 <= u8.length) {
      var fourcc = bytesToAscii(u8, off, 4);
      var size = (u8[off + 4] | (u8[off + 5] << 8) | (u8[off + 6] << 16) | (u8[off + 7] << 24));
      var end = off + 8 + size + (size & 1);
      if (end > u8.length) { ranges.push({ s: off, e: u8.length }); break; }
      if (WEBP_DROP[fourcc]) removed.push(fourcc.trim());
      else ranges.push({ s: off, e: end });
      off = end;
    }
    var total = 0, i;
    for (i = 0; i < ranges.length; i++) total += ranges[i].e - ranges[i].s;
    var out = new Uint8Array(total);
    var o = 0;
    for (i = 0; i < ranges.length; i++) { out.set(u8.subarray(ranges[i].s, ranges[i].e), o); o += ranges[i].e - ranges[i].s; }
    return { buffer: out.buffer, removed: removed, before: buf.byteLength, after: out.byteLength };
  }

  function sniff(buf) {
    var u8 = new Uint8Array(buf);
    if (u8.length >= 3 && u8[0] === 0xFF && u8[1] === 0xD8 && u8[2] === 0xFF) return 'jpeg';
    if (u8.length >= 8 && u8[0] === 0x89 && bytesToAscii(u8, 1, 3) === 'PNG') return 'png';
    if (u8.length >= 12 && bytesToAscii(u8, 0, 4) === 'RIFF' && bytesToAscii(u8, 8, 4) === 'WEBP') return 'webp';
    return null;
  }

  function detectMeta(buf) {
    var type = sniff(buf);
    if (type === 'jpeg') return detectJpeg(buf);
    if (type === 'png') { var p = detectPng(buf); return { type: 'png', textMeta: p.found, metaCount: p.found.length }; }
    if (type === 'webp') { var w = detectWebp(buf); return { type: 'webp', extMeta: w ? w.found : [], metaCount: w ? w.found.length : 0 }; }
    return { type: null };
  }

  function stripMeta(buf, opts) {
    opts = opts || {};
    var keepICC = opts.keepICC !== false;
    var type = sniff(buf);
    if (type === 'jpeg') return stripJpeg(buf, keepICC);
    if (type === 'png') return stripPng(buf);
    if (type === 'webp') return stripWebp(buf);
    return { buffer: buf, removed: [], before: buf.byteLength, after: buf.byteLength };
  }

  var api = { detectMeta: detectMeta, stripMeta: stripMeta, sniff: sniff };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.photoMeta = api;
})(typeof self !== 'undefined' ? self : this);
