// morph.js — face mesh warping for OldPhoto Alive.
// Given a face landmark mesh (478 points, normalized 0..1), build a triangle
// mesh via Delaunator and render a warped face each frame by moving vertices.
// Runs entirely in the browser on the raw image (no upload).
//
// Requires global `Delaunator` (loaded via vendor/delaunator.js).

// ---- Triangulation via Delaunator ----
// Returns array of triangles [ [i0,i1,i2], ... ] indexing into `points`.
function delaunayTriangulation(points) {
  if (typeof Delaunator === 'undefined') {
    throw new Error('Delaunator not loaded');
  }
  const coords = [];
  for (const p of points) { coords.push(p.x, p.y); }
  const d = new Delaunator(coords);
  const tris = [];
  for (let i = 0; i < d.triangles.length; i += 3) {
    tris.push([d.triangles[i], d.triangles[i + 1], d.triangles[i + 2]]);
  }
  return tris;
}

// ---- Affine warp: draw triangle (src) into triangle (dst) on a canvas context ----
// Draws srcImg (a full canvas) clipped by dst triangle, mapped via affine transform.
function drawWarpedTri(ctx, srcImg, srcTri, dstTri) {
  const [s0, s1, s2] = srcTri;
  const [d0, d1, d2] = dstTri;
  const denom = s0.x * (s1.y - s2.y) + s1.x * (s2.y - s0.y) + s2.x * (s0.y - s1.y);
  if (Math.abs(denom) < 1e-9) return;
  const a = (d0.x * (s1.y - s2.y) + d1.x * (s2.y - s0.y) + d2.x * (s0.y - s1.y)) / denom;
  const b = (d0.y * (s1.y - s2.y) + d1.y * (s2.y - s0.y) + d2.y * (s0.y - s1.y)) / denom;
  const c = (d0.x * (s2.x - s1.x) + d1.x * (s0.x - s2.x) + d2.x * (s1.x - s0.x)) / denom;
  const d = (d0.y * (s2.x - s1.x) + d1.y * (s0.x - s2.x) + d2.y * (s1.x - s0.x)) / denom;
  const e = d0.x - a * s0.x - c * s0.y;
  const f = d0.y - b * s0.x - d * s0.y;

  ctx.save();
  ctx.beginPath();
  ctx.moveTo(d0.x, d0.y); ctx.lineTo(d1.x, d1.y); ctx.lineTo(d2.x, d2.y);
  ctx.closePath();
  ctx.clip();
  ctx.transform(a, b, c, d, e, f);
  ctx.drawImage(srcImg, 0, 0);
  ctx.restore();
}

// ---- Full face warp render ----
// landmarks: array of {x,y} (normalized 0..1) in image coords.
// displacedLandmarks: same length, the target (morphed) positions.
// srcCanvas: canvas with the source image already drawn at W,H.
function warpFaceToCanvas(srcCanvas, W, H, landmarks, displacedLandmarks, tris) {
  const out = document.createElement('canvas');
  out.width = W; out.height = H;
  const ctx = out.getContext('2d');

  // Draw source into a SEPARATE temp canvas so triangle warping can drawImage from
  // it without self-referencing `out` (would crash).
  const src = document.createElement('canvas');
  src.width = W; src.height = H;
  src.getContext('2d').drawImage(srcCanvas, 0, 0, W, H);

  // Base the frame on the full source photo (NOT a cream fill). A cream background
  // erases everything outside the face mesh — hair, neck, shoulders all turn blank,
  // and any head movement shows cream gaps. Drawing the whole photo underneath and
  // warping the face triangles over it keeps hair intact and makes gentle sway clean.
  ctx.drawImage(src, 0, 0, W, H);

  function toPix(pt) { return { x: pt.x * W, y: pt.y * H }; }
  const srcPix = landmarks.map(toPix);
  const dstPix = displacedLandmarks.map(toPix);

  for (const [i0, i1, i2] of tris) {
    drawWarpedTri(ctx, src, [srcPix[i0], srcPix[i1], srcPix[i2]], [dstPix[i0], dstPix[i1], dstPix[i2]]);
  }
  return out;
}

// ---- Feathered Alive renderer (2026-08-29 rewrite) ----
// Why the old version looked distorted: it warped ONLY the 478-point face mesh and
// pasted it over the source, so (a) hair/ears/neck stayed frozen while the face
// moved, and (b) the warped face overlapped the unmoved original face at the mesh
// edge → ghosting. LivePortrait-style results move the WHOLE HEAD (hair included)
// as one rigid unit, and blend the face warp into the surroundings.
//
// renderAlive does exactly that in pure canvas:
//   1. warp the face with a FEATHERED mask (face replaced, edges fade into hair)
//   2. rigidly rotate/translate a head crop (face + hair) so the whole head moves

// Warp the face triangles onto a TRANSPARENT canvas (no background fill).
function warpFaceTransparent(srcCanvas, W, H, landmarks, displacedLandmarks, tris) {
  const out = document.createElement('canvas');
  out.width = W; out.height = H;
  const ctx = out.getContext('2d');
  const src = document.createElement('canvas');
  src.width = W; src.height = H;
  src.getContext('2d').drawImage(srcCanvas, 0, 0, W, H);
  function toPix(pt) { return { x: pt.x * W, y: pt.y * H }; }
  const srcPix = landmarks.map(toPix);
  const dstPix = displacedLandmarks.map(toPix);
  for (const [i0, i1, i2] of tris) {
    drawWarpedTri(ctx, src, [srcPix[i0], srcPix[i1], srcPix[i2]], [dstPix[i0], dstPix[i1], dstPix[i2]]);
  }
  return out;
}

// White mask covering the face (union of mesh triangles), blurred to feather the edge.
function faceFeatherMask(W, H, landmarks, tris, blurPx) {
  const m = document.createElement('canvas');
  m.width = W; m.height = H;
  const ctx = m.getContext('2d');
  ctx.fillStyle = '#fff';
  function px(pt) { return { x: pt.x * W, y: pt.y * H }; }
  for (const [i0, i1, i2] of tris) {
    const a = px(landmarks[i0]), b = px(landmarks[i1]), c = px(landmarks[i2]);
    ctx.beginPath();
    ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.lineTo(c.x, c.y);
    ctx.closePath(); ctx.fill();
  }
  const out = document.createElement('canvas');
  out.width = W; out.height = H;
  const o = out.getContext('2d');
  o.filter = 'blur(' + blurPx + 'px)';
  o.drawImage(m, 0, 0);
  return out;
}

// Face centre + radius in pixels (from the 468-point face mesh).
function faceCenter(landmarks, W, H) {
  let minX = 1, maxX = 0, minY = 1, maxY = 0;
  for (let i = 0; i < 468; i++) {
    if (landmarks[i].x < minX) minX = landmarks[i].x;
    if (landmarks[i].x > maxX) maxX = landmarks[i].x;
    if (landmarks[i].y < minY) minY = landmarks[i].y;
    if (landmarks[i].y > maxY) maxY = landmarks[i].y;
  }
  const cx = (minX + maxX) / 2 * W, cy = (minY + maxY) / 2 * H;
  const r = Math.max((maxX - minX) * W, (maxY - minY) * H) / 2;
  return { cx, cy, r };
}

// The full Alive frame: feathered face warp + rigid whole-head motion.
// head = { ang (rad), dx, dy (px) } — a gentle rigid transform of the head crop.
function renderAlive(srcCanvas, W, H, landmarks, displacedLandmarks, tris, head) {
  const faceC = document.createElement('canvas');
  faceC.width = W; faceC.height = H;
  const fctx = faceC.getContext('2d');
  fctx.drawImage(srcCanvas, 0, 0, W, H);            // base = full photo

  // 1. feathered face warp (replaces only the face, edges blend into hair)
  const warped = warpFaceTransparent(srcCanvas, W, H, landmarks, displacedLandmarks, tris);
  const mask = faceFeatherMask(W, H, landmarks, tris, Math.max(3, Math.round(Math.min(W, H) * 0.03)));
  const wl = document.createElement('canvas'); wl.width = W; wl.height = H;
  const wctx = wl.getContext('2d');
  wctx.drawImage(warped, 0, 0);
  wctx.globalCompositeOperation = 'destination-in';
  wctx.drawImage(mask, 0, 0);
  fctx.drawImage(wl, 0, 0);

  // 2. rigid whole-head motion (hair + ears + face move together)
  if (head && (Math.abs(head.ang) > 1e-4 || Math.abs(head.dx) > 1e-4 || Math.abs(head.dy) > 1e-4)) {
    const fc = faceCenter(landmarks, W, H);
    const r = fc.r * 1.9;                              // expand to include hair
    const hx = Math.max(0, Math.round(fc.cx - r));
    const hy = Math.max(0, Math.round(fc.cy - r));
    const hw = Math.min(W - hx, Math.round(r * 2));
    const hh = Math.min(H - hy, Math.round(r * 2));
    if (hw > 10 && hh > 10) {
      const crop = document.createElement('canvas'); crop.width = hw; crop.height = hh;
      crop.getContext('2d').drawImage(faceC, hx, hy, hw, hh, 0, 0, hw, hh);
      const rot = document.createElement('canvas'); rot.width = hw; rot.height = hh;
      const rctx = rot.getContext('2d');
      rctx.translate(hw / 2, hh / 2);
      rctx.rotate(head.ang);
      rctx.translate(-hw / 2, -hh / 2);
      rctx.drawImage(crop, 0, 0);
      // feathered edge so the head crop blends into the background
      const hm = document.createElement('canvas'); hm.width = hw; hm.height = hh;
      const hmc = hm.getContext('2d');
      hmc.fillStyle = '#fff'; hmc.fillRect(0, 0, hw, hh);
      const hf = document.createElement('canvas'); hf.width = hw; hf.height = hh;
      const hfc = hf.getContext('2d');
      hfc.filter = 'blur(' + Math.max(2, Math.round(hw * 0.05)) + 'px)';
      hfc.drawImage(hm, 0, 0);
      const headC = document.createElement('canvas'); headC.width = W; headC.height = H;
      const hctx = headC.getContext('2d');
      hctx.drawImage(rot, hx + head.dx, hy + head.dy);
      hctx.globalCompositeOperation = 'destination-in';
      hctx.drawImage(hf, hx + head.dx, hy + head.dy);
      fctx.drawImage(headC, 0, 0);
    }
  }
  return faceC;
}

// ---- Flow-based whole-image warp (LivePortrait-style, 2026-08-29) ----
// The old approach warped ONLY the 478-point face mesh, so hair stayed frozen and
// the face edge ghosted. LivePortrait's dense_motion instead builds a smooth
// displacement field over the WHOLE image: every pixel moves by a Gaussian-weighted
// average of the sparse keypoint translations, and the field naturally fades to zero
// away from the face → hair moves with the head, background stays put, no seams.
// We approximate that field on a coarse grid and warp the image through it.

// Displacement (normalized dx,dy) at point (nx,ny), inverse-distance weighted over
// keypoints. Weight by distance to the SOURCE landmark positions (not the target):
// output[p] samples src[p - flow(p)], so flow(p) must be the motion of the content
// that was AT p — i.e. dominated by the landmarks near p in the SOURCE image. With
// target-space weights, a big local motion (e.g. a mouth corner lifting) made the
// moved keypoint fall far from p and the motion vanished.
function flowDisplacementAt(landmarks, displaced, nx, ny) {
  let sx = 0, sy = 0, sw = 0;
  for (let k = 0; k < landmarks.length; k++) {
    const lx = landmarks[k].x, ly = landmarks[k].y;
    const ddx = nx - lx, ddy = ny - ly;
    const w = 1 / (ddx * ddx + ddy * ddy + 1e-8);
    sx += w * (displaced[k].x - landmarks[k].x);
    sy += w * (displaced[k].y - landmarks[k].y);
    sw += w;
  }
  if (sw < 1e-9) return { dx: 0, dy: 0 };
  return { dx: sx / sw, dy: sy / sw };
}

// Warp the whole image through a grid driven by the flow field.
// landmarks: source keypoints (normalized), displaced: target keypoints (normalized).
function renderAliveFlow(srcCanvas, W, H, landmarks, displaced, grid) {
  grid = grid || 24;
  const gx = grid, gy = Math.max(6, Math.round(grid * H / W));
  const src = document.createElement('canvas');
  src.width = W; src.height = H;
  src.getContext('2d').drawImage(srcCanvas, 0, 0, W, H);

  // per-vertex displacement (normalized), scaled by a head-centred envelope so the
  // motion is full on the face, partial in the hair, and fades to zero in the
  // background (equivalent to LivePortrait's background keypoint + mask).
  const fc = faceCenter(landmarks, 1, 1);
  const ENV_SIG = 0.42, ENV_INV2 = 1 / (2 * ENV_SIG * ENV_SIG);
  const dcol = [];
  for (let j = 0; j <= gy; j++) {
    const row = [];
    for (let i = 0; i <= gx; i++) {
      const nx = i / gx, ny = j / gy;
      const ddx = nx - fc.cx, ddy = ny - fc.cy;
      const env = Math.exp(-(ddx * ddx + ddy * ddy) * ENV_INV2);
      const d = flowDisplacementAt(landmarks, displaced, nx, ny);
      row.push({ dx: d.dx * env, dy: d.dy * env });
    }
    dcol.push(row);
  }

  // render quad mesh: destination quads tile the frame, source quads displaced
  const out = document.createElement('canvas');
  out.width = W; out.height = H;
  const octx = out.getContext('2d');
  const cw = W / gx, ch = H / gy;
  for (let j = 0; j < gy; j++) {
    for (let i = 0; i < gx; i++) {
      // backward mapping: output[p] = source[p - flow(p)]
      const p00 = { x: (i / gx - dcol[j][i].dx) * W, y: (j / gy - dcol[j][i].dy) * H };
      const p10 = { x: ((i + 1) / gx - dcol[j][i + 1].dx) * W, y: (j / gy - dcol[j][i + 1].dy) * H };
      const p01 = { x: (i / gx - dcol[j + 1][i].dx) * W, y: ((j + 1) / gy - dcol[j + 1][i].dy) * H };
      const p11 = { x: ((i + 1) / gx - dcol[j + 1][i + 1].dx) * W, y: ((j + 1) / gy - dcol[j + 1][i + 1].dy) * H };
      const t00 = { x: i * cw, y: j * ch }, t10 = { x: (i + 1) * cw, y: j * ch };
      const t01 = { x: i * cw, y: (j + 1) * ch }, t11 = { x: (i + 1) * cw, y: (j + 1) * ch };
      drawWarpedTri(octx, src, [p00, p10, p11], [t00, t10, t11]);
      drawWarpedTri(octx, src, [p00, p11, p01], [t00, t11, t01]);
    }
  }
  return out;
}

// ---- Landmark displacement functions ----
// Each returns a NEW landmarks array given base landmarks + time t (0..1)

// Blink: upper eyelids move down toward lower lids. Uses MediaPipe landmarks.
function displaceBlink(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const amt = Math.sin(t * Math.PI); // 0 -> 1 -> 0
  // upper lids move down
  const upperL = [159, 145, 160, 158, 144, 153, 173, 157, 154, 33];
  const lowerL = [153, 145, 155, 154];
  const upperR = [386, 374, 385, 384, 398, 380, 378, 373, 382, 263];
  const lowerR = [380, 374, 381, 382];
  const rangeL = Math.max(0.005, (landmarks[153].y - landmarks[159].y));
  const rangeR = Math.max(0.005, (landmarks[380].y - landmarks[386].y));
  // compute eye centers to keep inner/outer corner fixed while lid closes
  const eyeLc = { x: (landmarks[33].x + landmarks[133].x) / 2, y: (landmarks[33].y + landmarks[133].y) / 2 };
  const eyeRc = { x: (landmarks[362].x + landmarks[263].x) / 2, y: (landmarks[362].y + landmarks[263].y) / 2 };
  // modest, smooth lid travel — a violent blink reads as a jitter, not life
  const travelL = Math.max(0.02, rangeL * 1.3);
  const travelR = Math.max(0.02, rangeR * 1.3);
  upperL.forEach(i => {
    const p = landmarks[i];
    out[i].y = p.y + travelL * amt;
    // pull toward eye center horizontally a bit for a natural close
    out[i].x = p.x + (eyeLc.x - p.x) * amt * 0.08;
  });
  upperR.forEach(i => {
    const p = landmarks[i];
    out[i].y = p.y + travelR * amt;
    out[i].x = p.x + (eyeRc.x - p.x) * amt * 0.08;
  });
  // gentle lower-lid rise + slight iris follow — subtle, so the eye reads as closing
  // without a violent snap.
  [145, 153, 154, 155, 157].forEach(i => { if (out[i]) out[i].y -= travelL * amt * 0.1; });
  [374, 380, 381, 382, 384].forEach(i => { if (out[i]) out[i].y -= travelR * amt * 0.1; });
  [468, 469, 470, 471, 472, 473, 474, 475, 476, 477].forEach(i => {
    if (out[i]) out[i].y += ((travelL + travelR) / 2) * amt * 0.2;
  });
  return out;
}

// Duchenne smile: the SAME smile envelope also softens the eyes — lower lids rise a
// touch, outer corners tighten (crow's feet), upper lids narrow slightly. Called with
// the same `t` as displaceSmile so the eyes and mouth move TOGETHER.
function displaceSquint(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const amt = Math.max(0, t) * 1.0;
  if (amt < 0.001) return out;
  // lower lid rises — the classic "smiling eyes" (left + right) — moderate
  [145, 153, 154, 155, 157, 144].forEach(i => { if (out[i]) out[i].y -= amt * 0.018; });
  [374, 380, 381, 382, 384, 373].forEach(i => { if (out[i]) out[i].y -= amt * 0.018; });
  // outer corners tighten + lift (crow's feet)
  if (out[133]) out[133].x += amt * 0.01;
  if (out[362]) out[362].x -= amt * 0.01;
  if (out[133]) out[133].y -= amt * 0.009;
  if (out[362]) out[362].y -= amt * 0.009;
  // upper lid narrows (the eye "smiles" closed a touch)
  [159, 160, 158, 33, 145].forEach(i => { if (out[i]) out[i].y += amt * 0.012; });
  [386, 385, 380, 263, 374].forEach(i => { if (out[i]) out[i].y += amt * 0.012; });
  return out;
}

// Smile: corners lift & spread, cheeks lift, lower lip rises. `t` is the smile
// strength 0..1 (caller shapes it as a sustained smile, not a quick pulse).
function displaceSmile(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const amt = Math.max(0, t) * 1.0;
  if (amt < 0.001) return out;
  const corners = [61, 291];
  const mid = landmarks[13];
  corners.forEach(i => {
    const dx = landmarks[i].x - mid.x;
    out[i].y -= amt * 0.03;                     // corner lift (moderate — no distortion)
    out[i].x += Math.sign(dx) * amt * 0.018;    // corner spread
  });
  // cheek / nasolabial lift
  [117, 346, 205, 425, 50, 280].forEach(i => { if (out[i]) out[i].y -= amt * 0.02; });
  [185, 409].forEach(i => { if (out[i]) out[i].y -= amt * 0.018; });
  return out;
}

// Mouth openness — lips part (upper lip up, lower lip + chin down). Driven by the
// library's perioral lip-activity metric, kept separate from the smile so styles
// with different lip motion visibly differ.
function displaceMouth(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const amt = Math.max(0, t) * 1.0;
  if (amt < 0.001) return out;
  if (out[17]) out[17].y -= amt * 0.02;   // upper lip up
  if (out[14]) out[14].y += amt * 0.032;  // lower lip down (mouth opens)
  if (out[16]) out[16].y += amt * 0.018;  // chin follows
  if (out[13]) out[13].y -= amt * 0.014;  // upper lip centre up a touch
  [61, 291].forEach(i => { if (out[i]) { const dx = out[i].x - out[13].x; out[i].x += Math.sign(dx) * amt * 0.012; } });
  return out;
}

// Breathe: subtle whole-head scale about face center + tiny y bob.
function displaceBreathe(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const s = 1 + 0.004 * Math.sin(t * Math.PI * 2);
  let cx = 0, cy = 0;
  for (let i = 0; i < 468; i++) { cx += landmarks[i].x; cy += landmarks[i].y; }
  cx /= 468; cy /= 468;
  for (let i = 0; i < 468; i++) {
    out[i].x = cx + (landmarks[i].x - cx) * s;
    out[i].y = cy + (landmarks[i].y - cy) * s + 0.0015 * Math.sin(t * Math.PI * 2);
  }
  return out;
}

// Eyebrows: gentle brow lift that fades in with the expression. MediaPipe's 468-mesh
// left-brow indices are [70,63,105,66,107,69,109,108,68,71]; right [336,296,334,293,300,285,295,282,283,276].
function displaceEyebrows(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const amt = 0.0045 * Math.max(0, Math.sin((t - 0.06) * Math.PI));
  if (amt < 0.0001) return out;
  [70,63,105,66,107,69,109,108,68,71,336,296,334,293,300,285,295,282,283,276].forEach(i => {
    if (out[i]) out[i].y -= amt;
  });
  return out;
}

// Head sway: a gentle, barely-there yaw about the face centre (a living person never
// holds perfectly still). Kept to ~1.2° so it reads as a presence, never a turn or tilt.
function displaceHeadSway(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y, z: (p.z !== undefined ? p.z : 0) }));
  const ang = 0.021 * Math.sin(t * Math.PI * 2);   // ±~1.2°
  const drift = 0.003 * Math.sin(t * Math.PI * 2); // tiny horizontal sway
  let cx = 0, cy = 0;
  for (let i = 0; i < 468; i++) { cx += landmarks[i].x; cy += landmarks[i].y; }
  cx /= 468; cy /= 468;
  const c = Math.cos(ang), s = Math.sin(ang);
  for (let i = 0; i < 468; i++) {
    const dx = landmarks[i].x - cx, dy = landmarks[i].y - cy;
    out[i].x = cx + dx * c - dy * s + drift;
    out[i].y = cy + dx * s + dy * c;
  }
  return out;
}

// ---- Public ----
function buildFaceMesh(landmarks) {
  const pts = landmarks.map(p => ({ x: p.x, y: p.y }));
  return { points: pts, tris: delaunayTriangulation(pts) };
}

function hasFace(landmarks) {
  return landmarks && landmarks.length >= 468;
}

// Export ESM + also expose on window for non-module use
export { delaunayTriangulation, warpFaceToCanvas, warpFaceTransparent, faceFeatherMask, faceCenter, renderAlive, flowDisplacementAt, renderAliveFlow, displaceBlink, displaceSmile, displaceMouth, displaceSquint, displaceBreathe, displaceEyebrows, displaceHeadSway, buildFaceMesh, hasFace, drawWarpedTri };
if (typeof window !== 'undefined') {
  window.__morph = { delaunayTriangulation, warpFaceToCanvas, warpFaceTransparent, faceFeatherMask, faceCenter, renderAlive, flowDisplacementAt, renderAliveFlow, displaceBlink, displaceSmile, displaceMouth, displaceSquint, displaceBreathe, displaceEyebrows, displaceHeadSway, buildFaceMesh, hasFace, drawWarpedTri };
}
