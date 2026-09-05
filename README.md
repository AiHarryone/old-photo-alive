# PixelFix — 12 Free Browser Tools for Photos

![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-2ea44f)
![Privacy](https://img.shields.io/badge/nothing%20uploaded-100%25%20browser-4f46e5)
![Pricing](https://img.shields.io/badge/free%20trial%20%E2%86%92%20%249.99%20one--time-059669)

**One site, twelve free image tools — all running 100% in your browser. Nothing uploaded, no account, no signup.**

Live at: **https://aiharryone.github.io/pixelfix/**

## 🧰 The tools

| Tool | What it does | Cost |
|------|--------------|------|
| [Compress Images](https://aiharryone.github.io/pixelfix/compress-image.html) | Shrink JPG/PNG/WebP, batch, resize, convert | **Free** |
| [HEIC to JPG](https://aiharryone.github.io/pixelfix/heic-to-jpg.html) | Batch-convert iPhone HEIC photos to JPG | 100 free |
| [EXIF / GPS Remover](https://aiharryone.github.io/pixelfix/exif-remover.html) | Strip GPS location & hidden metadata, lossless | 100 free |
| [AVIF to JPG](https://aiharryone.github.io/pixelfix/avif-to-jpg.html) | Convert AVIF photos to JPG (native decode) | 100 free |
| [Passport Photo Maker](https://aiharryone.github.io/pixelfix/passport-photo.html) | Official passport/visa/ID photo sizes | 1 free try |
| [Remove Background](https://aiharryone.github.io/pixelfix/remove-bg.html) | Clean person cut-outs with feathered edges | 1 free try |
| [PDF Tools](https://aiharryone.github.io/pixelfix/pdf-tools.html) | Images→PDF, merge PDFs, PDF→JPG | 1 free try |
| [GIF Maker](https://aiharryone.github.io/pixelfix/gif-maker.html) | Turn images into an animated GIF | 1 free try |
| [Watermark](https://aiharryone.github.io/pixelfix/watermark.html) | Add text/logo watermark in batch | 1 free try |
| [Document Scanner](https://aiharryone.github.io/pixelfix/document-scanner.html) | Straighten & crop a photo of any document | 1 free try |
| [Restore Photos](https://aiharryone.github.io/pixelfix/restore.html) | Fix faded, blurry, noisy old photos | 1 free try |
| [Animate Photos](https://aiharryone.github.io/pixelfix/) | Ken Burns push-in/pan/fade → animated GIF | 1 free try |

**Unlock all twelve tools forever for a one-time $9.99** — no subscription. [Get lifetime access](https://creem.io/product/prod_6AE1xgYo8j7DIbN08Bh59S).

## 🔒 Why it's different

- **100% in your browser** — photos, documents and PDFs never leave your device. Built for the privacy-sensitive moments: family photos, ID documents, and removing location data before you share.
- **Lossless where it matters** — the EXIF/GPS remover strips metadata segments without re-compressing, so your pixels stay byte-for-byte identical.
- **No signup, no account, no server** — open a page and it works.
- **Free to try** — Compress is completely free; the three converters (HEIC/AVIF/EXIF) each give 100 free files; every other tool gives one free try.
- **Lifetime unlock** — one $9.99 payment, all tools, forever.

## ❓ FAQ

<details>
<summary><b>Are my photos uploaded to a server?</b></summary>
No. Everything — compression, background removal, PDF conversion, GIF encoding, watermarking, scanning, HEIC/AVIF decoding and EXIF stripping — runs 100% in your browser. Your photos never leave your device. Removing location data by uploading would defeat the whole purpose, so it is all local.
</details>

<details>
<summary><b>Which tools are free?</b></summary>
Compress Images is completely free. HEIC, AVIF and EXIF/GPS tools each give 100 free files. The other tools each give one free try; a one-time $9.99 unlocks all twelve forever — no subscription.
</details>

<details>
<summary><b>Is the EXIF remover lossless?</b></summary>
Yes — it removes only the metadata segments (EXIF/GPS/XMP/IPTC/comments) and copies every image pixel unchanged, keeping your color profile by default. No re-compression, no quality loss.
</details>

<details>
<summary><b>Do I need an account?</b></summary>
No signup, no account, no email. Open a page and it works.
</details>

<details>
<summary><b>Can I use the results commercially?</b></summary>
Yes — anything you create is yours to use, sell or share.
</details>

## 🛠 Tech

- Static HTML + vanilla Canvas — no frameworks, no build step, no dependencies at runtime
- HEIC decoding via libheif (WebAssembly); AVIF decodes natively in the browser (createImageBitmap) — no plugin
- Metadata stripping (`exif-strip.js`) is a dependency-free, byte-level parser for JPEG/PNG/WebP
- Pure-JS GIF encoding via [omggif](https://github.com/deanm/omggif)
- Person cut-out via MediaPipe SelfieSegmentation (243 KB model, runs on-device)
- PDF via [jsPDF](https://github.com/parallax/jsPDF), [pdf-lib](https://github.com/Hopding/pdf-lib), [pdf.js](https://mozilla.github.io/pdf.js/)
- GitHub Pages hosting · Cloudflare Worker for Creem license unlock
- SEO: 43 landing pages + sitemap + robots.txt + IndexNow + Bing verification + Open Graph/Twitter cards

## 💡 Also built by the same person

- 🎃 [TrendSnap](https://aiharryone.github.io/trendsnap/) — free Halloween Invitation Maker with 20 hand-drawn templates, in your browser, nothing uploaded

- [KDP Launch Kit](https://aiharryone.github.io/kdp-launch-kit/) — free calculators and generators for Amazon KDP self-publishers
- [Certificate Maker](https://aiharryone.github.io/certificate-maker/) — online certificate generator

## 📜 License

The tools are free to use; anything you create is yours. Code released for reference.
