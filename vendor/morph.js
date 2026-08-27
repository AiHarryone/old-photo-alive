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
  ctx.fillStyle = '#fff8f0';
  ctx.fillRect(0, 0, W, H);

  // Draw source into a SEPARATE temp canvas so triangle warping can drawImage from
  // it without self-referencing `out` (would crash).
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

// ---- Landmark displacement functions ----
// Each returns a NEW landmarks array given base landmarks + time t (0..1)

// Blink: upper eyelids move down toward lower lids. Uses MediaPipe landmarks.
function displaceBlink(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y }));
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
  // exaggerate lid travel for visible "alive" effect (blink reaches ~75% closure)
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
  return out;
}

// Smile: mouth corners lift and spread slightly; lower lip lifts a touch.
function displaceSmile(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y }));
  const amt = Math.sin(t * Math.PI) * 0.7;
  const corners = [61, 291];
  const mid = landmarks[13];
  corners.forEach(i => {
    const dx = landmarks[i].x - mid.x;
    out[i].y -= amt * 0.025;
    out[i].x += Math.sign(dx) * amt * 0.014;
  });
  out[17].y -= amt * 0.016;
  // slightly lift upper lip corners' neighbors
  [185, 409].forEach(i => { if (out[i]) out[i].y -= amt * 0.01; });
  return out;
}

// Breathe: subtle whole-head scale about face center + tiny y bob.
function displaceBreathe(landmarks, t) {
  const out = landmarks.map(p => ({ x: p.x, y: p.y }));
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

// ---- Public ----
function buildFaceMesh(landmarks) {
  const pts = landmarks.map(p => ({ x: p.x, y: p.y }));
  return { points: pts, tris: delaunayTriangulation(pts) };
}

function hasFace(landmarks) {
  return landmarks && landmarks.length >= 468;
}

// Export ESM + also expose on window for non-module use
export { delaunayTriangulation, warpFaceToCanvas, displaceBlink, displaceSmile, displaceBreathe, buildFaceMesh, hasFace, drawWarpedTri };
if (typeof window !== 'undefined') {
  window.__morph = { delaunayTriangulation, warpFaceToCanvas, displaceBlink, displaceSmile, displaceBreathe, buildFaceMesh, hasFace, drawWarpedTri };
}
