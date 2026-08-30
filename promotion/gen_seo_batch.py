# -*- coding: utf-8 -*-
"""Batch-generate PixelFix long-tail SEO pages (per-tool × use-case).
Reuses the indigo HEAD template from gen_seo_pages.py. PixelFix SEO pages live
in /seo/ so all links must be ABSOLUTE (via the {base} placeholder).
Run with `py gen_seo_batch.py`."""
import os
from gen_seo_pages import HEAD, faq_block, sec, BASE

OUT = r'D:\claude\old-photo-alive\seo'
os.makedirs(OUT, exist_ok=True)

# tool landing files (absolute, so {base} is replaced last in render)
C = 'compress-image.html'
P = 'passport-photo.html'
R = 'remove-bg.html'
D = 'pdf-tools.html'
G = 'gif-maker.html'
W = 'watermark.html'
S = 'document-scanner.html'
E = 'restore.html'
A = 'index.html'

def tpage(slug, title, meta, h1, hero, tool, tool_name, sections, faq, cta_h2, cta_p):
    """Build a per-tool landing page dict."""
    s = list(sections)
    s.append(faq_block(faq))
    return {
        'slug': slug, 'title': title, 'meta': meta, 'h1': h1, 'hero_p': hero,
        'hero_sub': 'Free in your browser · No upload · No signup',
        'sections': s,
        'cta_h2': cta_h2, 'cta_p': cta_p,
    }

PAGES = [
  tpage('compress-jpg-to-100kb.html',
    'Compress JPG to 100KB — Reduce Image Size Free (No Upload)',
    'Compress a JPG to under 100KB in your browser: shrink photos to 100kb, 50kb or any target for email, forms and uploads. Free, nothing uploaded.',
    'Compress JPG to 100KB',
    'Shrink a JPG to under 100KB for email, forms and uploads — in your browser, nothing uploaded.',
    C, 'Compress Images',
    [sec('Why 100KB Is the Magic Number', '<p>Many forms — job portals, visa applications, government sites — reject images over <b>100KB</b> or a specific width. Compressing a JPG to 100KB usually means <b>lowering quality to ~70–85</b> or reducing the pixel width, and doing it in your browser means the photo never leaves your device.</p>'),
     sec('How to Compress a JPG to 100KB', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/compress-image.html" style="color:#4f46e5;font-weight:bold;">PixelFix Compress</a> and drop in your JPG.',
        'Drag the <b>Quality slider</b> down until the estimated size shows under 100KB.',
        'If the width is large, set a <b>Max width</b> (e.g. 1200px) — that shrinks size fastest.',
        'Download the compressed JPG and upload it to your form.'
      ])),
     sec('What “Quality” Actually Does', '<p>Quality 100 keeps every detail but keeps size high; quality <b>60–80</b> looks nearly identical on screens while cutting size 50–70%. For photos (not text or logos) this is where most of the size savings live — and it stays fully on your device.</p>')],
    [('Is compressing a JPG to 100KB free?', 'Yes — PixelFix Compress is completely free, unlimited.'),
     ('Does it upload my photo?', 'No. Everything runs in your browser; the photo never leaves your device.'),
     ('What if I need 50KB or 200KB?', 'The same sliders work for any target — drag quality or width until you hit it.'),
     ('Does it work for PNG?', 'Yes — and WebP, which is usually 25–35% smaller than JPG at the same quality.')],
    'Compress a JPG to 100KB Now.',
    'Free, unlimited, and nothing is uploaded.'),
  tpage('compress-image-size-online.html',
    'Compress Image Size Online — Reduce JPG/PNG/WebP Free',
    'Compress image size online in your browser: shrink JPG, PNG or WebP, batch resize, and see the exact % saved. Free, no upload, no account.',
    'Compress Image Size Online',
    'Shrink JPG, PNG and WebP — with a live %-saved readout — entirely in your browser.',
    C, 'Compress Images',
    [sec('Size Is the Enemy of Speed', '<p>An oversized image slows every page, email and upload. Compressing keeps the quality you can see and cuts the bytes nobody needs — most photos drop <b>50–80%</b> with quality 60–85. PixelFix does it locally, so even sensitive photos can be compressed safely.</p>'),
     sec('What You Can Do', '<div class="grid">%s</div>' % ''.join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, p2) for h, p2 in [
        ('Batch compress', 'Drop in many images and compress them all at once.'),
        ('Resize by width', 'Cap the width to shrink large photos fast.'),
        ('Convert format', 'JPG → WebP (25–35% smaller), PNG → JPG, and more.'),
        ('Live savings', 'See the exact % smaller for every image, before you download.')
      ])),
     sec('The Quality Sweet Spot', '<p>For photos, <b>quality 70–85</b> is usually invisible on screens while saving the most size. For text, screenshots and logos, PNG or high-quality WebP avoids blur. Test the slider — the preview updates instantly.</p>')],
    [('Is it really free?', 'Yes — PixelFix Compress is completely free, unlimited, no signup.'),
     ('What formats are supported?', 'JPG, PNG and WebP input; JPG, PNG, WebP output.'),
     ('Are my images uploaded?', 'No — all compression runs in your browser.'),
     ('Can I compress many images at once?', 'Yes — batch upload and batch download are built in.')],
    'Compress Any Image Online Now.',
    'Free, unlimited, private — nothing is uploaded.'),
  tpage('resize-image-online.html',
    'Resize Image Online — Change Width & Height Free (No Upload)',
    'Resize an image online in your browser: set width, height or a maximum dimension for JPG/PNG/WebP. Free, no upload, no account.',
    'Resize Image Online',
    'Set width, height or a max dimension — JPG, PNG and WebP, right in your browser.',
    C, 'Compress Images',
    [sec('When You Need to Resize', '<p>Forms, emails, thumbnails and social posts each want a different size. Resizing preserves quality (unlike re-saving a small file), and doing it locally means even private photos stay on your device.</p>'),
     sec('How to Resize', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/compress-image.html" style="color:#4f46e5;font-weight:bold;">PixelFix Compress</a> and drop in your image.',
        'Set a <b>Max width</b> (e.g. 1200px) — height follows automatically.',
        'Or use the <b>Resize</b> output option for exact dimensions.',
        'Download — and check the size, which usually drops too.'
      ])),
     sec('Resize vs Re-Compress', '<p>Shrinking the pixel dimensions usually cuts file size far more than quality alone — a 4000px photo resized to 1200px is often <b>80–90% smaller</b> while looking identical on screens.</p>')],
    [('Can I resize for free?', 'Yes — PixelFix Compress is free and unlimited.'),
     ('Does resizing lose quality?', 'Downscaling keeps visual quality; it only removes pixels the display never needs.'),
     ('Is it private?', 'Yes — everything runs in your browser.'),
     ('What formats?', 'JPG, PNG and WebP in; JPG, PNG, WebP out.')],
    'Resize an Image Online Now.',
    'Free, unlimited, private — nothing is uploaded.'),
  tpage('jpg-to-webp-converter.html',
    'JPG to WebP Converter — 25–35% Smaller, Free & Private',
    'Convert JPG to WebP in your browser: 25–35% smaller than JPG at the same quality, free, unlimited, nothing uploaded.',
    'JPG to WebP Converter',
    'Convert JPG to WebP — typically 25–35% smaller at the same quality.',
    C, 'Compress Images',
    [sec('Why WebP', '<p>WebP is the modern image format — Google’s recommended default — delivering <b>25–35% smaller files</b> than JPG at equivalent quality. It’s supported by every modern browser, which is why it’s the 2026 default.</p>'),
     sec('How to Convert', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/compress-image.html" style="color:#4f46e5;font-weight:bold;">PixelFix Compress</a> and drop in your JPG.',
        'Set the output format to <b>WebP</b>.',
        'Adjust quality until it looks right — usually 75–85 for photos.',
        'Download the .webp file.'
      ])),
     sec('Where It Helps Most', '<p>WebP shines on the web — smaller images load faster pages. For sites, thumbnails, and anything sent over email, the size savings add up fast. PixelFix converts locally, so nothing is uploaded.</p>')],
    [('Is JPG to WebP free?', 'Yes — PixelFix Compress is free and unlimited.'),
     ('Is WebP supported everywhere?', 'Yes — all modern browsers open WebP natively.'),
     ('Will I lose quality?', 'At the same quality setting, WebP is visually equivalent to JPG but smaller.'),
     ('Is my photo uploaded?', 'No — the conversion runs entirely in your browser.')],
    'Convert JPG to WebP Now.',
    'Free, unlimited, private — nothing is uploaded.'),
  tpage('make-passport-photo-at-home.html',
    'Make a Passport Photo at Home — Free 2×2 & 35×45 Maker',
    'Make an official passport photo at home: US 2×2, UK 35×45, China, EU and more preset sizes with a printable 4×6 layout. Free, nothing uploaded.',
    'Make a Passport Photo at Home',
    'Turn any photo into an official passport photo — correct size, printable in minutes.',
    P, 'Passport Photo Maker',
    [sec('Why Make It at Home', '<p>Passport photos at a store cost $10–20 and a trip out. At home you control the lighting, retake until it’s right, and get the exact size your application needs — <b>in your browser, with the photo never uploaded</b>.</p>'),
     sec('How It Works', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/passport-photo.html" style="color:#4f46e5;font-weight:bold;">PixelFix Passport Photo</a> and upload a clear, face-forward photo.',
        'Pick your official size — US 2×2, UK 35×45, China, EU, Australia and more.',
        'Drag the crop so your head sits on the guide; choose white/blue/red background.',
        'Download a single photo or a <b>printable 4×6 sheet</b>.'
      ])),
     sec('Official Size Presets', '<div class="grid">%s</div>' % ''.join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, p2) for h, p2 in [
        ('US Passport & Visa', '2×2 inches (51×51mm)'),
        ('UK / EU', '35×45mm'),
        ('China ID & Passport', '33×48mm / 33×46mm'),
        ('Canada / Australia / Japan', '50×70mm / 35×45mm / 35×45mm')
      ]))],
    [('Is it really free?', 'Yes — one free try, then unlock all tools forever for a one-time $9.99.'),
     ('Does it meet official requirements?', 'It uses official size presets and a head-position guide; always double-check your application’s exact spec.'),
     ('Is my photo uploaded?', 'No — everything runs in your browser.'),
     ('Can I print it?', 'Yes — the 4×6 sheet layout prints at any photo kiosk or home printer.')],
    'Make Your Passport Photo Now.',
    'One free try — official size, printable, nothing uploaded.'),
  tpage('passport-photo-size-guide.html',
    'Passport Photo Size Guide — US, UK, China, EU, Australia (2026)',
    'Passport photo size guide: exact dimensions for US 2×2, UK 35×45, China, EU, Canada and Australia, plus background and head-size rules. Make yours free.',
    'Passport Photo Size Guide',
    'Exact photo dimensions for every major passport — US, UK, China, EU and more.',
    P, 'Passport Photo Maker',
    [sec('The Size Table', '<table style="width:100%%;border-collapse:collapse;margin:10px 0;font-size:15px;"><tr style="background:#eef2ff;"><th style="padding:8px;text-align:left;border:1px solid #e5e7eb;">Country</th><th style="padding:8px;text-align:left;border:1px solid #e5e7eb;">Photo size</th></tr>%s</table>' % ''.join(
        '<tr><td style="padding:8px;border:1px solid #e5e7eb;">%s</td><td style="padding:8px;border:1px solid #e5e7eb;">%s</td></tr>' % (a, b) for a, b in [
        ('US passport / visa', '2 × 2 inches (51 × 51mm)'),
        ('UK passport / visa', '35 × 45mm'),
        ('China passport', '33 × 48mm'),
        ('China ID card', '26 × 32mm'),
        ('EU / Schengen', '35 × 45mm'),
        ('Canada', '50 × 70mm'),
        ('Australia', '35 × 45mm'),
        ('Japan', '35 × 45mm')
      ])),
     sec('The Head-Size Rule', '<p>Most passports require your head to occupy roughly <b>70–80% of the height</b>, centered, with clear space around it. PixelFix’s <b>head guide line</b> shows you exactly where to crop so you pass the photo check on the first try.</p>'),
     sec('Background Rules', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>White</b> — US, UK, EU, most applications.',
        '<b>White or light grey</b> — China passport.',
        '<b>White, light blue or red</b> — China ID card (plain, no shadow).',
        '<b>No shadows or objects</b> — the face must be evenly lit.'
      ])),
     sec('Make It in 30 Seconds', '<p>Don’t measure by hand — use the <a href="{base}/%s" style="color:#4f46e5;font-weight:bold;">PixelFix Passport Photo maker</a>: pick your country, drag the crop to the guide, set the background, and download a printable sheet.</p>' % P)],
    [('What size is a US passport photo?', '2 × 2 inches (51 × 51mm).'),
     ('What about the UK?', '35 × 45mm with a white background.'),
     ('Can I make it at home?', 'Yes — PixelFix applies the exact size preset and a head-position guide.'),
     ('Is it free?', 'One free try; unlock all tools for a one-time $9.99.')],
    'Get Your Passport Photo Right the First Time.',
    'Pick your country, drag to the guide, download — free to try.'),
  tpage('change-passport-photo-background.html',
    'Change Photo Background to White, Blue or Red — Free',
    'Change a photo background to white, blue or red for ID and passport photos — clean cutout, in your browser. Free, nothing uploaded.',
    'Change Photo Background',
    'Swap any photo background to white, blue or red for ID photos — clean, in your browser.',
    P, 'Passport Photo Maker',
    [sec('What It Does', '<p>ID photos need a plain, even background — usually <b>white, light blue or red</b>. PixelFix cuts the person out with a feathered edge and places them on the exact background your application requires, all locally.</p>'),
     sec('How to Do It', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/passport-photo.html" style="color:#4f46e5;font-weight:bold;">PixelFix Passport Photo</a> and upload your photo.',
        'Choose your country preset — it sets the right background.',
        'Pick <b>white, blue or red</b>; adjust the blend if needed.',
        'Download the finished ID photo.'
      ])),
     sec('Why the Feathered Edge Matters', '<p>A hard cutout leaves a visible halo. PixelFix uses <b>feathered edge detection</b> so hair and shoulders blend naturally into the new background — the difference between “edited” and “official”.</p>')],
    [('Is it free?', 'One free try; unlimited use is a one-time $9.99.'),
     ('Which backgrounds are available?', 'White, light blue and red — plus keeping the original.'),
     ('Is my photo uploaded?', 'No — everything runs in your browser.'),
     ('Is it good enough for ID?', 'It meets the background and size requirements of common applications; check your country’s exact spec.')],
    'Change Your Background Now.',
    'Free to try — clean cutout, nothing uploaded.'),
  tpage('remove-background-from-photo.html',
    'Remove Background from Photo — Free, No Upload, In-Browser',
    'Remove the background from any photo in your browser: clean person cutouts with feathered edges, transparent PNG export. Free, nothing uploaded.',
    'Remove Background from Photo',
    'Clean person cutouts with feathered edges — in your browser, nothing uploaded.',
    R, 'Remove Background',
    [sec('Why Do It Locally', '<p>Background removal is exactly the task you don’t want to upload — portraits, ID documents, product shots. PixelFix runs the <b>person segmentation model in your browser</b> (243KB, on-device), so the photo never leaves your device.</p>'),
     sec('How to Remove a Background', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/remove-bg.html" style="color:#4f46e5;font-weight:bold;">PixelFix Remove Background</a> and drop in your photo.',
        'Wait ~1 second — the model detects the person and cuts them out.',
        'Fine-tune with the <b>feather</b> and <b>edge</b> sliders.',
        'Export as a <b>transparent PNG</b> or place it on a white background.'
      ])),
     sec('Great for', '<div class="grid">%s</div>' % ''.join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, p2) for h, p2 in [
        ('Portraits & ID', 'Passport and ID photos with a clean background.'),
        ('E-commerce', 'Product shots on transparent or white.'),
        ('Avatars', 'Profile pictures with a solid background.'),
        ('Design', 'Cutout people for posters and slides.')
      ]))],
    [('Is it really free?', 'One free try; unlock unlimited for a one-time $9.99.'),
     ('Does it work on non-people?', 'It’s optimized for people (SelfieSegmentation); pets and objects work less reliably.'),
     ('Is my photo uploaded?', 'No — the model runs in your browser.'),
     ('What format do I get?', 'Transparent PNG, or JPG on a white background.')],
    'Remove a Background Now.',
    'Free to try — private by design.'),
  tpage('make-transparent-background.html',
    'Make Image Background Transparent — PNG Free, No Upload',
    'Make an image background transparent (PNG) in your browser: cut out people, clean edges, export transparent. Free, private, nothing uploaded.',
    'Make Image Background Transparent',
    'Cut out the subject and export a transparent PNG — right in your browser.',
    R, 'Remove Background',
    [sec('Transparent PNG, Explained', '<p>A transparent PNG keeps the subject and drops the background to “checkerboard” transparency — perfect for logos on any page, avatars, product shots and overlays. PixelFix produces it locally with feathered edges.</p>'),
     sec('How to Make It Transparent', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/remove-bg.html" style="color:#4f46e5;font-weight:bold;">PixelFix Remove Background</a> and upload your image.',
        'Let the model detect and cut out the subject.',
        'Choose <b>Transparent PNG</b> as the export format.',
        'Download and use it anywhere.'
      ])),
     sec('Where Transparent PNGs Help', '<p>Logos and product shots on colored pages, profile pictures over any banner, overlays for slides and video — a transparent background makes the same cutout work anywhere.</p>')],
    [('Is it free?', 'One free try; unlimited is a one-time $9.99.'),
     ('Do I get a PNG?', 'Yes — transparent PNG, or JPG on white.'),
     ('Is it private?', 'Yes — the segmentation runs on your device.'),
     ('Does it work on logos?', 'For people it’s best; simple logos also cut cleanly with the feather tool.')],
    'Make a Transparent PNG Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('image-to-pdf-converter.html',
    'Images to PDF Converter — Free, In Your Browser',
    'Convert images to a single PDF in your browser: JPG, PNG, WebP → PDF, in order, adjustable size. Free, nothing uploaded.',
    'Images to PDF Converter',
    'Turn JPG, PNG and WebP images into one tidy PDF — entirely in your browser.',
    D, 'PDF Tools',
    [sec('Scan, Photos and Docs to PDF', '<p>Emails, applications and sharing all want a single PDF instead of loose images. PixelFix’s PDF tool converts any images into one ordered PDF — useful for scanned documents, photo sets and receipts — without uploading anything.</p>'),
     sec('How to Convert Images to PDF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/pdf-tools.html" style="color:#4f46e5;font-weight:bold;">PixelFix PDF Tools</a> and add your images.',
        'Drag to reorder them.',
        'Choose page size (A4, Letter) and orientation.',
        'Download the combined PDF.'
      ]))],
    [('Is it free?', 'One free try; unlimited is a one-time $9.99.'),
     ('Can I reorder images?', 'Yes — drag and drop before converting.'),
     ('Is my data uploaded?', 'No — the PDF is built in your browser.'),
     ('What formats?', 'JPG, PNG and WebP images → PDF.')],
    'Convert Images to PDF Now.',
    'Free to try — nothing uploaded.'),
  tpage('merge-pdf-free.html',
    'Merge PDF Files Free — Combine PDFs Online, In Your Browser',
    'Merge PDF files into one in your browser: combine PDFs, reorder pages, free. No upload, private.',
    'Merge PDF Files',
    'Combine several PDFs into one — reorder pages, in your browser.',
    D, 'PDF Tools',
    [sec('When You Need to Merge', '<p>Submitting a single application file, combining scans into one document, or bundling chapters — merging PDFs is a daily need. PixelFix does it locally, so even confidential documents stay on your device.</p>'),
     sec('How to Merge', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/pdf-tools.html" style="color:#4f46e5;font-weight:bold;">PixelFix PDF Tools</a> and add your PDFs.',
        'Reorder them by dragging.',
        'Click <b>Merge</b> — the combined PDF is built in your browser.',
        'Download the merged file.'
      ]))],
    [('Is merging free?', 'One free try; unlimited is a one-time $9.99.'),
     ('Are my PDFs uploaded?', 'No — everything runs in your browser.'),
     ('Can I reorder pages?', 'Yes — drag PDFs or pages before merging.'),
     ('Is there a size limit?', 'Your browser handles large files; very large sets may be slower.')],
    'Merge Your PDFs Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('pdf-to-jpg.html',
    'Convert PDF to JPG — Extract Pages as Images Free',
    'Convert PDF pages to JPG images in your browser: extract a page, a range, or all pages. Free, nothing uploaded.',
    'Convert PDF to JPG',
    'Turn PDF pages into JPG images — in your browser, nothing uploaded.',
    D, 'PDF Tools',
    [sec('Why Extract PDF Pages', '<p>Sometimes you need a single page as an image — to send, edit, or reuse in a slide. PixelFix converts any PDF page (or range) to JPG locally, so even sensitive documents stay private.</p>'),
     sec('How to Convert a PDF to JPG', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/pdf-tools.html" style="color:#4f46e5;font-weight:bold;">PixelFix PDF Tools</a> and add your PDF.',
        'Choose a page range or “all pages”.',
        'Pick a resolution.',
        'Download the JPG images.'
      ]))],
    [('Is it free?', 'One free try; unlimited is a one-time $9.99.'),
     ('Can I extract one page?', 'Yes — set the range to a single page.'),
     ('Is it private?', 'Yes — the PDF never leaves your browser.'),
     ('What resolution?', 'Choose output DPI/width when converting.')],
    'Convert a PDF to JPG Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('make-gif-from-photos.html',
    'Make a GIF from Photos — Photo Slideshow GIF, Free',
    'Make an animated GIF from your photos in your browser: add frames, set speed, loop, export. Free, nothing uploaded.',
    'Make a GIF from Photos',
    'Turn several photos into an animated GIF — in your browser, nothing uploaded.',
    G, 'GIF Maker',
    [sec('From Still Photos to a GIF', '<p>A photo slideshow GIF is the easiest way to share a set of memories — a trip, a party, a series of progress shots. PixelFix builds the GIF locally, so even personal photos stay on your device.</p>'),
     sec('How to Make a Photo GIF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/gif-maker.html" style="color:#4f46e5;font-weight:bold;">PixelFix GIF Maker</a> and add your photos in order.',
        'Set frame speed, loop mode and reverse if you like.',
        'Preview the animation.',
        'Export the GIF — free, with a small watermark.'
      ]))],
    [('Is it free?', 'One free try; unlock all tools for a one-time $9.99.'),
     ('How many photos can I add?', 'As many as you like — more frames mean a bigger GIF.'),
     ('Is it private?', 'Yes — the GIF is encoded in your browser.'),
     ('Can I set speed and loop?', 'Yes — frame delay, loop and reverse are all adjustable.')],
    'Make a GIF from Your Photos Now.',
    'Free to try — nothing uploaded.'),
  tpage('add-watermark-to-photos.html',
    'Add Watermark to Photos — Batch Text & Logo, Free',
    'Add a text or logo watermark to photos in your browser: position, opacity, batch apply. Free, nothing uploaded.',
    'Add Watermark to Photos',
    'Stamp a text or logo watermark on your photos — batch, in your browser.',
    W, 'Watermark',
    [sec('Protect Your Work', '<p>Photographers, sellers and creators watermark before publishing so their work can’t be reused without credit. PixelFix adds a text or logo watermark in seconds — across a whole batch, locally.</p>'),
     sec('How to Add a Watermark', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/watermark.html" style="color:#4f46e5;font-weight:bold;">PixelFix Watermark</a> and upload your photos.',
        'Type your text or upload a logo; set size, opacity, position and font.',
        'Preview on one photo.',
        'Apply to the batch and download them all.'
      ]))],
    [('Is it free?', 'One free try; unlock all tools for a one-time $9.99.'),
     ('Can I use a logo?', 'Yes — upload a PNG logo as the watermark.'),
     ('Is it batch?', 'Yes — add the same watermark to a whole folder.'),
     ('Is it private?', 'Yes — everything runs in your browser.')],
    'Watermark Your Photos Now.',
    'Free to try — nothing uploaded.'),
  tpage('scan-document-to-pdf.html',
    'Scan Document to PDF — Straighten & Save Free (Phone or Camera)',
    'Scan a document with your phone or camera in your browser: auto straighten, crop, save as PDF. Free, nothing uploaded.',
    'Scan Document to PDF',
    'Turn a phone photo of any document into a clean, straight PDF.',
    S, 'Document Scanner',
    [sec('Better Than a Photo of a Page', '<p>A scan is straight, cropped and even — a photo of a page usually has an angle and shadows. PixelFix’s scanner <b>auto-detects the four corners, straightens the perspective and crops</b> — in your browser, so the document never leaves your device.</p>'),
     sec('How to Scan a Document', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/document-scanner.html" style="color:#4f46e5;font-weight:bold;">PixelFix Document Scanner</a> and add your photo.',
        'Let auto-detect find the page edges — or drag the corner handles.',
        'Adjust perspective and contrast.',
        'Download the scan as a PDF or JPG.'
      ]))],
    [('Is it free?', 'One free try; unlock all tools for a one-time $9.99.'),
     ('Does it straighten automatically?', 'Yes — four-corner detection plus manual handles.'),
     ('Is my document uploaded?', 'No — everything runs in your browser.'),
     ('What can I export?', 'A straightened PDF or JPG.')],
    'Scan a Document Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('restore-old-photos-free.html',
    'Restore Old Photos Free — Fix Faded & Damaged Photos Online',
    'Restore old photos free in your browser: auto-fix faded colors, blur, noise and scratches. Before/after preview, export full resolution. Nothing uploaded.',
    'Restore Old Photos',
    'Bring faded, blurry, noisy old photos back to life — in your browser, free to try.',
    E, 'Restore Photos',
    [sec('The Scanned Family Photo Problem', '<p>Old scans are faded, low-contrast and dusty. A good restore <b>stretches the tones, balances color, sharpens edges and reduces noise</b> — without the flat “one-click filter” look. PixelFix does all of it locally, so your family photos stay private.</p>'),
     sec('How to Restore a Photo', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/restore.html" style="color:#4f46e5;font-weight:bold;">PixelFix Restore</a> and upload your scan.',
        'Click <b>Auto Fix</b> — it stretches contrast, balances color and sharpens.',
        'Fine-tune with the Brightness, Contrast, Saturation and Sharpen sliders.',
        'Compare before/after with the divider, then export at full resolution.'
      ])),
     sec('What Auto Fix Does', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>Gentle histogram stretch</b> — lifts washed-out tones without crushing blacks.',
        '<b>Grey-world white balance</b> — removes the yellow/blue cast from aged prints.',
        '<b>3×3 median denoise</b> — softens film grain and dust.',
        '<b>Local sharpening</b> — restores edge crispness.'
      ]))],
    [('Is restoring free?', 'One free try; unlock all tools for a one-time $9.99.'),
     ('Is my photo uploaded?', 'No — all processing runs in your browser.'),
     ('Does it work on color photos?', 'Yes — it detects grayscale and skips color steps automatically.'),
     ('Can I get a high-res export?', 'Yes — export at full resolution.')],
    'Restore a Family Photo Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('fix-blurry-photos.html',
    'Fix Blurry Photos — Sharpen Online Free, No Upload',
    'Fix a blurry photo in your browser: sharpen soft edges, reduce noise, restore detail. Before/after preview. Free, nothing uploaded.',
    'Fix Blurry Photos',
    'Sharpen soft, blurry photos and restore detail — in your browser.',
    E, 'Restore Photos',
    [sec('Not Every Blur Is Fatal', '<p>A slightly soft photo can often be saved with <b>targeted sharpening and contrast</b> — especially old scans and phone shots in low light. PixelFix sharpens locally, keeping the original untouched until you export.</p>'),
     sec('How to Sharpen a Photo', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/restore.html" style="color:#4f46e5;font-weight:bold;">PixelFix Restore</a> and upload your photo.',
        'Click <b>Auto Fix</b>, then raise <b>Sharpen</b>.',
        'Add a little Contrast to restore pop.',
        'Compare before/after and export at full resolution.'
      ])),
     sec('The Limit', '<p>Sharpening adds edge contrast — it <b>cannot recreate detail that was never captured</b> (motion blur and extreme focus misses are limited). For those, a light sharpen plus denoise is still the best local option.</p>')],
    [('Is it free?', 'One free try; unlimited is a one-time $9.99.'),
     ('Can I fix motion blur?', 'Light motion blur improves; heavy blur can’t be fully restored locally.'),
     ('Is it private?', 'Yes — everything runs in your browser.'),
     ('What export?', 'Full-resolution JPG or PNG.')],
    'Sharpen a Blurry Photo Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('make-photo-move.html',
    'Make a Photo Move — Ken Burns Effect Free, No Upload',
    'Make a photo move in your browser: slow push-in, pan and fade — the documentary Ken Burns effect — exported as a GIF. Free, nothing uploaded.',
    'Make a Photo Move',
    'Give a still photo slow, cinematic motion — exported as a GIF, in your browser.',
    A, 'Animate Photos',
    [sec('The Ken Burns Effect', '<p>The slow push-in, pan and fade you see in every documentary is the <b>Ken Burns effect</b> — and it’s the fastest way to make an old photo feel alive. PixelFix applies it <b>in your browser</b>, with nothing uploaded.</p>'),
     sec('How to Make a Photo Move', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix Animate</a> and upload your photo.',
        'Pick a motion — <b>Push-in, Pull-back, Pan across, Pan up, Fade</b>.',
        'Preview the animation.',
        'Export a GIF — free, with a small watermark.'
      ])),
     sec('Which Motion for Which Photo', '<div class="grid">%s</div>' % ''.join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, p2) for h, p2 in [
        ('Push-in', 'Slow zoom toward a face — the “memory” feel.'),
        ('Pan across', 'Drift across landscapes and group shots.'),
        ('Pull-back', 'Zoom out to reveal the whole scene.'),
        ('Fade in', 'A soft dissolve, elegant for memorials.')
      ]))],
    [('Is it free?', 'All 5 motion effects are free with a small watermark; a one-time $9.99 removes it.'),
     ('Is my photo uploaded?', 'No — the animation is rendered in your browser.'),
     ('What do I get?', 'An animated GIF, ready to share anywhere.'),
     ('Does it work on old photos?', 'Yes — it’s made for exactly that.')],
    'Make a Photo Move Now.',
    'Free — nothing uploaded, no signup.'),
  tpage('ken-burns-effect-generator.html',
    'Ken Burns Effect Generator — Slow Zoom & Pan Online, Free',
    'Make the Ken Burns effect online for free: slow push-in, pan and fade on any photo, exported as a GIF. In your browser, nothing uploaded.',
    'Ken Burns Effect Generator',
    'Slow push-in, pan and fade — the documentary move, on any photo, for free.',
    A, 'Animate Photos',
    [sec('What the Ken Burns Effect Is', '<p>The Ken Burns effect is the slow zoom and pan used in nearly every documentary — it makes a still photo feel alive and cinematic. PixelFix applies it <b>in your browser</b> and exports an animated GIF you can share anywhere.</p>'),
     sec('How to Make a Ken Burns Video', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix Animate</a> and upload a photo.',
        'Pick <b>Push-in</b>, <b>Pull-back</b>, <b>Pan across</b>, <b>Pan up</b> or <b>Fade</b>.',
        'Preview the motion and adjust.',
        'Export a GIF — free, with a small watermark.'
      ])),
     sec('Which Move for Which Photo', '<div class="grid">%s</div>' % ''.join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, p2) for h, p2 in [
        ('Push-in', 'Slow zoom toward a face — the “memory” feel.'),
        ('Pan across', 'Drift across landscapes and group shots.'),
        ('Pull-back', 'Zoom out to reveal the whole scene.'),
        ('Fade in', 'A soft dissolve, elegant for memorials.')
      ]))],
    [('Is it free?','All 5 motion effects are free with a small watermark; one-time $9.99 removes it.'),
     ('Is my photo uploaded?','No — the animation renders in your browser.'),
     ('What do I get?','An animated GIF.'),
     ('Can I use it for a memorial?','Yes — slow push-ins and fades are exactly what tributes use.')],
    'Make a Ken Burns Video Now.',
    'Free — nothing uploaded, no signup.'),
  tpage('animate-photo-online-free.html',
    'Animate a Photo Online Free — Ken Burns & Face Animation',
    'Animate a photo online for free in your browser: slow Ken Burns motion, plus face animation that adds a blink, smile and breath. Nothing uploaded.',
    'Animate a Photo Online',
    'Give a still photo slow motion — or a real blink and smile — all in your browser.',
    A, 'Animate Photos',
    [sec('Two Ways to Animate', '<p>PixelFix offers two kinds of animation: <b>Ken Burns motion</b> (slow push-in, pan, fade) for any photo, and <b>face animation</b> for portraits with a clear face — a blink, a smile, a breath, rendered locally.</p>'),
     sec('How to Animate', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix Animate</a> and upload a photo.',
        'For motion, pick a Ken Burns effect and preview.',
        'For face animation, wait for the <b>Alive ✨</b> button (appears once a face is detected).',
        'Export a GIF.'
      ])),
     sec('Privacy', '<p>Everything — the motion, the face detection, the export — runs <b>in your browser</b>. Your photo never leaves your device.</p>')],
    [('Is it really free?','Ken Burns effects are free; face animation is free for one try, then one-time $9.99.'),
     ('Is my photo uploaded?','No — all processing is on your device.'),
     ('Does face animation work on any photo?','It needs a clear, face-forward portrait to detect the face.'),
     ('What do I get?','An animated GIF ready to share.')],
    'Animate a Photo Now.',
    'Free — nothing uploaded, no signup.'),
  tpage('compress-png-online.html',
    'Compress PNG Online — Shrink PNG File Size Free',
    'Compress a PNG online in your browser: shrink PNG file size while keeping quality, batch and download. Free, nothing uploaded.',
    'Compress PNG Online',
    'Shrink PNG file size while keeping quality — in your browser, free.',
    C, 'Compress Images',
    [sec('Why PNG Files Get Big', '<p>PNG is lossless — great for screenshots, logos and graphics, but large for photos. Compressing a PNG usually means <b>lowering quality slightly</b> (for photos) or <b>re-encoding to WebP</b> (25–35% smaller with no visible change).</p>'),
     sec('How to Compress a PNG', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/compress-image.html" style="color:#4f46e5;font-weight:bold;">PixelFix Compress</a> and drop in your PNG.',
        'Drag the <b>Quality</b> slider down until the size looks right.',
        'Or set the output to <b>WebP</b> for the biggest savings.',
        'Download — and check the % saved readout.'
      ])),
     sec('PNG vs WebP', '<p>For photos, WebP is visually identical to PNG at a fraction of the size — it’s the 2026 default. For graphics with transparency that must stay PNG, a quality slider on the PNG itself still saves plenty.</p>')],
    [('Is it free?','Yes — PixelFix Compress is free and unlimited.'),
     ('Will I lose quality?','At quality 70–85 the change is invisible on screens for most photos.'),
     ('Can I keep transparency?','PNG output keeps transparency; WebP also supports it.'),
     ('Is it private?','Yes — everything runs in your browser.')],
    'Compress a PNG Now.',
    'Free, unlimited, nothing uploaded.'),
  tpage('visa-photo-maker.html',
    'Visa Photo Maker — Official Visa Photo Sizes, Free',
    'Make official visa photos free in your browser: US, UK, Schengen, China and more preset sizes with correct background. Printable 4×6 sheet. Nothing uploaded.',
    'Visa Photo Maker',
    'Official visa photo sizes, correct background, printable — in your browser.',
    P, 'Passport Photo Maker',
    [sec('Visa Photos Are Picky', '<p>Every visa has exact photo specs — size, background, head position. Getting them wrong means a rejected application. PixelFix bakes in the <b>official size presets</b> and a head-position guide so you pass on the first try.</p>'),
     sec('How to Make a Visa Photo', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/passport-photo.html" style="color:#4f46e5;font-weight:bold;">PixelFix Passport Photo</a> and upload a face-forward photo.',
        'Pick your visa’s size preset (US, UK, Schengen, China, Canada and more).',
        'Drag the crop to the head guide; set the background.',
        'Download a single photo or a printable 4×6 sheet.'
      ])),
     sec('Always Check the Embassy Spec', '<p>Presets cover the common requirements, but visa rules change per country and embassy. Double-check your specific application’s size and background before submitting.</p>')],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Which sizes are included?','US, UK, Schengen/EU, China, Canada, Australia and more.'),
     ('Is my photo uploaded?','No — everything runs in your browser.'),
     ('Can I print it?','Yes — the 4×6 sheet layout works at any photo kiosk.')],
    'Make a Visa Photo Now.',
    'One free try — nothing uploaded.'),
  tpage('cut-out-image-online.html',
    'Cut Out Image Online — Remove & Crop Objects Free',
    'Cut out a person or object from an image online free: remove background, crop, and export transparent. In your browser, nothing uploaded.',
    'Cut Out Image Online',
    'Cut people and objects out of any photo — transparent export, in your browser.',
    R, 'Remove Background',
    [sec('What “Cut Out” Means', '<p>Cutting out an image means separating the subject from its background — for product shots, avatars, collages and designs. PixelFix uses an on-device segmentation model to do it <b>locally</b>, so even sensitive photos stay on your device.</p>'),
     sec('How to Cut Out an Image', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/remove-bg.html" style="color:#4f46e5;font-weight:bold;">PixelFix Remove Background</a> and upload your photo.',
        'Wait ~1 second for the model to detect the subject.',
        'Fine-tune with the feather and edge sliders.',
        'Export a transparent PNG or place it on white.'
      ])),
     sec('Best for People', '<p>The model is optimized for <b>people</b> — portraits, ID photos, e-commerce shots. Simple logos and objects also cut cleanly; complex or furry subjects may need manual cleanup.</p>')],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Is it private?','Yes — the segmentation model runs in your browser.'),
     ('What do I get?','A transparent PNG, or JPG on white.'),
     ('Does it work on products?','Yes — product shots with clean edges work well.')],
    'Cut Out an Image Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('combine-images-into-pdf.html',
    'Combine Images into One PDF — Free & In-Browser',
    'Combine JPG, PNG and WebP images into one PDF in your browser: order, resize and download. Free, nothing uploaded.',
    'Combine Images into One PDF',
    'Turn many images into a single PDF — ordered, in your browser.',
    D, 'PDF Tools',
    [sec('Why Combine Images to PDF', '<p>Emails, applications and archives want one PDF, not ten loose images. Combining JPGs and PNGs into a single PDF is a daily need — scans, receipts, photo sets, documents — and PixelFix does it locally.</p>'),
     sec('How to Combine Images to PDF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/pdf-tools.html" style="color:#4f46e5;font-weight:bold;">PixelFix PDF Tools</a> and add your images.',
        'Drag to reorder them.',
        'Choose page size and orientation.',
        'Download the combined PDF.'
      ]))],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Can I reorder?','Yes — drag images before converting.'),
     ('Is it private?','Yes — the PDF is built in your browser.'),
     ('What formats?','JPG, PNG and WebP images → one PDF.')],
    'Combine Images into a PDF Now.',
    'Free to try — nothing uploaded.'),
  tpage('compress-pdf-online.html',
    'Compress PDF Online — Reduce PDF Size Free',
    'Compress a PDF online in your browser: shrink large PDFs by converting pages to images. Free, nothing uploaded.',
    'Compress PDF Online',
    'Shrink large PDFs — in your browser, free, nothing uploaded.',
    D, 'PDF Tools',
    [sec('Why PDFs Get Too Big', '<p>Scanned documents and photo-filled PDFs balloon in size and get rejected by email limits or slow to share. Compressing by <b>converting pages to compressed images</b> can cut the file by half or more.</p>'),
     sec('How to Compress a PDF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/pdf-tools.html" style="color:#4f46e5;font-weight:bold;">PixelFix PDF Tools</a> and add your PDF.',
        'Choose the pages to process.',
        'Compress and download the smaller PDF.'
      ])),
     sec('The Trade-off', '<p>Compressing a PDF by re-encoding pages trades a little sharpness for size — fine for scans, forms and documents, less ideal for design-heavy PDFs meant to stay print-perfect.</p>')],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('How much smaller will it get?','Often 40–70% for scanned/photo PDFs.'),
     ('Is it private?','Yes — everything runs in your browser.'),
     ('Will text stay readable?','Yes — compression targets images, not text.')],
    'Compress a PDF Now.',
    'Free to try — nothing uploaded.'),
  tpage('enhance-old-photos.html',
    'Enhance Old Photos — Improve Photo Quality Online Free',
    'Enhance old photos free online: fix faded color, low contrast and softness with one click. Before/after preview, full-res export. Nothing uploaded.',
    'Enhance Old Photos',
    'Fix faded color, contrast and softness in old scans — in your browser.',
    E, 'Restore Photos',
    [sec('What “Enhance” Fixes', '<p>Old scans are faded, flat and soft. One-click enhance <b>stretches the tones, balances color, sharpens edges and reduces noise</b> — bringing back the depth the original photo had.</p>'),
     sec('How to Enhance a Photo', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/restore.html" style="color:#4f46e5;font-weight:bold;">PixelFix Restore</a> and upload your scan.',
        'Click <b>Auto Fix</b>.',
        'Fine-tune with the sliders.',
        'Compare before/after, then export at full resolution.'
      ])),
     sec('Grayscale vs Color', '<p>PixelFix detects black-and-white photos and skips the color steps automatically — so a faded B&W portrait gets a gentle, film-appropriate restore, and a faded color photo gets its life back.</p>')],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Is my photo uploaded?','No — all processing runs in your browser.'),
     ('Can I export full resolution?','Yes.'),
     ('Will it fix heavy damage?','It fixes tone, color and softness; deep scratches need manual repair tools.')],
    'Enhance an Old Photo Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('repair-scratched-photos.html',
    'Repair Scratched Photos — Fix Damage Online Free',
    'Repair scratched, dusty or damaged photos free online: reduce noise and scratches, restore faded detail. In your browser, nothing uploaded.',
    'Repair Scratched Photos',
    'Reduce scratches, dust and noise in damaged scans — in your browser.',
    E, 'Restore Photos',
    [sec('What Can Be Fixed', '<p>Scans of old prints carry scratches, dust and grain. A combination of <b>median denoise</b>, gentle contrast stretch and sharpening removes most of it — the photo looks clean without looking plastic.</p>'),
     sec('How to Repair a Photo', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/restore.html" style="color:#4f46e5;font-weight:bold;">PixelFix Restore</a> and upload your scan.',
        'Click <b>Auto Fix</b> and enable <b>Reduce noise</b>.',
        'Adjust contrast and sharpen to taste.',
        'Export the repaired photo at full resolution.'
      ])),
     sec('The Limit', '<p>Noise reduction can smooth small scratches and grain. Large missing areas or heavy tears need manual retouching — beyond what an automatic local tool can do.</p>')],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Is it private?','Yes — everything runs in your browser.'),
     ('Does it fix color fading too?','Yes — the same auto-fix handles faded color and contrast.'),
     ('What about big tears?','Small dust and scratches yes; large missing areas need manual repair.')],
    'Repair a Photo Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('gif-maker-online.html',
    'GIF Maker Online — Create Animated GIFs Free',
    'Make an animated GIF online free: turn images or a photo set into a GIF, set speed and loop, export. In your browser, nothing uploaded.',
    'GIF Maker Online',
    'Turn images into an animated GIF — speed, loop, export — in your browser.',
    G, 'GIF Maker',
    [sec('What You Can Make', '<p>A GIF maker lets you turn stills into motion — photo slideshows, before/after comparisons, memes, product spins. PixelFix builds the GIF locally, so your images never leave your device.</p>'),
     sec('How to Make a GIF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/gif-maker.html" style="color:#4f46e5;font-weight:bold;">PixelFix GIF Maker</a> and add your images in order.',
        'Set frame speed and loop mode.',
        'Preview the animation.',
        'Export the GIF — free, with a small watermark.'
      ]))],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('How many frames?','As many as you like — more frames mean a larger GIF.'),
     ('Is it private?','Yes — the GIF is encoded in your browser.'),
     ('Can I set loop and speed?','Yes — both are adjustable.')],
    'Make a GIF Now.',
    'Free to try — nothing uploaded.'),
  tpage('discord-avatar-gif-maker.html',
    'Discord Avatar GIF Maker — Animated Profile Pictures Free',
    'Make an animated Discord avatar GIF free: turn any image into a looping profile picture, no upload, no signup. Works for PFP sizes, in your browser.',
    'Discord Avatar GIF Maker',
    'Turn any image into a looping animated avatar — for Discord, in your browser.',
    G, 'GIF Maker',
    [sec('Why Animated Avatars', '<p>A moving profile picture stands out in every server. GIF avatars are everywhere on Discord — and making one should be instant and private. PixelFix builds a looping GIF from your image <b>entirely in your browser</b>.</p>'),
     sec('How to Make a Discord Avatar GIF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/gif-maker.html" style="color:#4f46e5;font-weight:bold;">PixelFix GIF Maker</a> and add 2–3 frames of your avatar.',
        'Set a short loop (square frames work best for avatars).',
        'Preview the animation.',
        'Export the GIF — free, with a small watermark.'
      ])),
     sec('Avatar Tips', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>Square works best</b> — Discord crops avatars to a square; start from a square image.',
        '<b>Keep it short</b> — a 1–2 second loop is snappier than a long one.',
        '<b>Bold colors</b> — small GIFs read better with high contrast.',
        '<b>Nothing is uploaded</b> — your avatar image never leaves your device.'
      ]))],
    [('Is it free?','One free try; unlimited GIF making is a one-time $9.99.'),
     ('Is my image uploaded?','No — everything runs in your browser.'),
     ('Does it work for Discord?','Yes — export a square looping GIF and set it as your avatar.'),
     ('What formats?','JPG and PNG images in, animated GIF out.')],
    'Make a Discord Avatar GIF Now.',
    'Free to try — private, nothing uploaded.'),
  tpage('make-gif-online-no-upload.html',
    'Make GIF Online Without Uploading — Private & Free',
    'Make a GIF online without uploading anything: your images stay on your device, the GIF is made in your browser. Free, no account.',
    'Make GIF Online Without Uploading',
    'Your images never leave your device — the GIF is made locally, for free.',
    G, 'GIF Maker',
    [sec('The Privacy Problem with GIF Sites', '<p>Most online GIF makers upload your images to their server — including memes and personal photos you’d rather keep private. PixelFix makes the GIF <b>in your browser</b>; nothing is uploaded, nothing is stored, no account needed.</p>'),
     sec('How to Make a GIF Locally', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/gif-maker.html" style="color:#4f46e5;font-weight:bold;">PixelFix GIF Maker</a> — it loads in your browser, no signup.',
        'Add your images in order.',
        'Set speed and loop; preview.',
        'Export the GIF — done locally, nothing uploaded.'
      ]))],
    [('Is it really no-upload?','Yes — the GIF is encoded entirely in your browser.'),
     ('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Do I need an account?','No — no signup, no email.'),
     ('What can I make?','Looping GIFs from images — avatars, memes, slideshows, before/afters.')],
    'Make a GIF Without Uploading Now.',
    'Free to try — private by design.'),
  tpage('loop-gif-generator.html',
    'Loop GIF Generator — Seamless Looping GIFs Online Free',
    'Make a seamlessly looping GIF online free: perfect loop GIFs for avatars, memes and reaction images, in your browser, nothing uploaded.',
    'Loop GIF Generator',
    'Seamless looping GIFs — for avatars, memes and reactions — in your browser.',
    G, 'GIF Maker',
    [sec('Why Loop Matters', '<p>A GIF that loops cleanly feels like motion, not a slideshow. Looping is everywhere — avatars, meme templates, reaction images, subtle motion designs. PixelFix makes a <b>loop-ready GIF</b> from your images locally.</p>'),
     sec('How to Make a Looping GIF', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/gif-maker.html" style="color:#4f46e5;font-weight:bold;">PixelFix GIF Maker</a> and add your frames.',
        'Set <b>loop</b> on and pick a frame speed that hides the seam.',
        'Preview — a 1–2 second loop hides transitions best.',
        'Export the looping GIF.'
      ])),
     sec('Loop Tips', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>First and last frames</b> — make them similar so the loop feels seamless.',
        '<b>Short beats long</b> — tight loops feel intentional.',
        '<b>Reaction images</b> — a subtle bounce or pulse loops beautifully.'
      ]))],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Is it private?','Yes — the GIF is built in your browser.'),
     ('Can I loop any image set?','Yes — any frames you add will loop continuously.'),
     ('Do I need an account?','No.')],
    'Make a Looping GIF Now.',
    'Free to try — nothing uploaded.'),
  tpage('gif-profile-picture-maker.html',
    'GIF Profile Picture Maker — Animated PFP from Frames, Free',
    'Make an animated profile picture (PFP) GIF free: assemble 2–3 frames into a looping PFP for Discord, forums and games. In your browser, nothing uploaded.',
    'GIF Profile Picture Maker',
    'Assemble a looping animated PFP from your frames — in your browser.',
    G, 'GIF Maker',
    [sec('A Moving PFP Stands Out', '<p>Animated profile pictures are a status symbol — on Discord, forums, gaming profiles and socials. A looping GIF PFP is easy to make from a couple of frames, and PixelFix assembles it <b>locally</b>, so your images stay private.</p>'),
     sec('How to Make an Animated PFP', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/gif-maker.html" style="color:#4f46e5;font-weight:bold;">PixelFix GIF Maker</a>.',
        'Add <b>2–3 frames</b> of your avatar — each a slightly different pose or crop.',
        'Set a short loop and preview.',
        'Export the GIF and set it as your PFP.'
      ])),
     sec('PFP Tips', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>Square frames</b> — most platforms crop PFPs to square.',
        '<b>Subtle motion</b> — a gentle loop beats a violent one at small sizes.',
        '<b>Export small</b> — small GIFs upload faster and stay sharp on avatars.'
      ]))],
    [('Is it free?','One free try; unlimited is a one-time $9.99.'),
     ('Is it private?','Yes — the GIF is encoded in your browser.'),
     ('Does it work for all platforms?','Any platform that accepts GIF avatars — Discord, forums, gaming profiles.'),
     ('Do I need an account?','No.')],
    'Make an Animated PFP Now.',
    'Free to try — nothing uploaded.'),
]

def render(page):
    html = HEAD
    subs = {
        '{title}': page['title'],
        '{meta}': page['meta'],
        '{slug}': page['slug'],
        '{ldjson}': _ld_for(page),
        '{h1}': page['h1'],
        '{hero_p}': page.get('hero_p', ''),
        '{hero_sub}': page['hero_sub'],
        '{sections}': '\n\n'.join(page['sections']),
        '{cta_h2}': page['cta_h2'],
        '{cta_p}': page['cta_p'],
    }
    for k, v in subs.items():
        if k == '{base}':
            continue
        html = html.replace(k, v)
    # {base} last so it resolves inside sections content too
    html = html.replace('{base}', BASE)
    return html

def _ld_for(page):
    import re
    faq_section = [s for s in page['sections'] if s.startswith('<section class="faq">')]
    if not faq_section:
        return ''
    items = re.findall(r'<p><b>(.*?)</b> (.*?)</p>', faq_section[0])
    qa = []
    for q, a in items:
        qa.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"', '\\"'), a.replace('"', '\\"')))
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % ','.join(qa)

def main():
    seen = set()
    for p in PAGES:
        if p['slug'] in seen:
            print('!! duplicate slug', p['slug'])
            continue
        seen.add(p['slug'])
        html = render(p)
        with open(os.path.join(OUT, p['slug']), 'w', encoding='utf-8') as f:
            f.write(html)
        print('wrote', p['slug'], len(html), 'bytes')
    print('done —', len(PAGES), 'pages')

if __name__ == '__main__':
    main()
