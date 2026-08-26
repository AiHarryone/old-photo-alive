# OldPhoto Alive — Bring Old Photos Back to Life

Turn a still, faded photo into a gentle, living motion — in your browser. No upload, no signup, no watermark on your memories.

Live at: **https://aiharryone.github.io/old-photo-alive/**

## What it does

Upload any JPG/PNG and apply slow, cinematic motion effects:

- 🎞 **Push-in** — slow zoom toward the subject (classic Ken Burns)
- 🎞 **Pull-back** — gentle zoom out to reveal the scene
- 🎞 **Pan across** — horizontal drift through the frame
- 🎞 **Pan up** — vertical rise over the image
- 🎞 **Fade in** — a quiet dissolve from a soft field

Export as an animated GIF, ready for social media, family slideshows, memorial tributes or memory videos.

## Why it's different

- **100% in your browser** — your photo never leaves your device. Built for the privacy-sensitive moments (family photos, memories).
- **No signup, no account** — just open and use it.
- **Free to try** — push-in & pull-back with a small watermark.
- **One-time $9.99** unlock — all 5 effects, clean 1080p export, no subscription ever.

## Tech

- Static HTML + vanilla Canvas (`requestAnimationFrame` Ken Burns animation)
- Pure-JS GIF encoding via [omggif](https://github.com/deanm/omggif) (median-cut quantization, no server, no Web Worker)
- GitHub Pages hosting · Cloudflare Worker for Creem license unlock
- SEO: sitemap + robots.txt + IndexNow + Bing verification

## Free tools for KDP authors

Made by the same person who built [KDP Launch Kit](https://aiharryone.github.io/kdp-launch-kit/) — free calculators and generators for Amazon self-publishers.

## License

The tool itself is free to use; the animated GIFs you create are yours. Code released for reference.
