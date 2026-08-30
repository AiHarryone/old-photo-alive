# -*- coding: utf-8 -*-
"""Generate SEO landing pages for PixelFix. Run with `py gen_seo_pages.py`."""
import os

OUT = r'D:\claude\old-photo-alive\seo'
os.makedirs(OUT, exist_ok=True)

BASE = 'https://aiharryone.github.io/pixelfix'

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="msvalidate.01" content="E62785F51D89A3BD3AFBB2BC2BB07BF9">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{base}/seo/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PixelFix">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{base}/seo/{slug}">
<meta property="og:image" content="{base}/assets/demo.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta}">
<meta name="twitter:image" content="{base}/assets/demo.jpg">
<script type="application/ld+json">
{ldjson}
</script>
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  :root{--bg:#f6f8fb;--card:#fff;--ink:#111827;--muted:#6b7280;--accent:#4f46e5;--accent2:#2563eb;--accent-soft:#eef2ff;--green:#059669;--green-soft:#ecfdf5;--amber:#d97706;--amber-soft:#fffbeb;--line:#e5e7eb;--shadow:0 10px 30px rgba(17,24,39,.08);--radius:16px;}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;font-size:16px;}
  .wrap{max-width:880px;margin:0 auto;padding:0 22px;}
  header{background:#fff;position:sticky;top:0;z-index:50;border-bottom:1px solid var(--line);}
  nav{display:flex;justify-content:space-between;align-items:center;padding:14px 0;flex-wrap:wrap;gap:10px;}
  .logo{font-weight:800;font-size:20px;letter-spacing:-.3px;color:var(--ink);}
  .logo em{font-style:normal;color:var(--accent);}
  .nav-links{display:flex;align-items:center;gap:18px;flex-wrap:wrap;}
  .nav-links a{color:var(--muted);font-weight:600;text-decoration:none;font-size:14px;}
  .nav-links a:hover{color:var(--ink);}
  .btn{display:inline-block;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;text-decoration:none;padding:11px 22px;border-radius:999px;font-weight:700;font-size:14px;transition:.15s;border:none;cursor:pointer;box-shadow:0 4px 14px rgba(79,70,229,.3);}
  .btn:hover{transform:translateY(-1px);}
  .btn.ghost{background:#fff;color:var(--ink);box-shadow:none;border:1.5px solid var(--line);}
  .hero{text-align:center;padding:48px 0 30px;}
  .hero .eyebrow{display:inline-flex;align-items:center;gap:8px;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:7px 16px;font-weight:700;font-size:13px;margin-bottom:18px;}
  .hero h1{font-size:38px;line-height:1.15;letter-spacing:-.8px;margin-bottom:14px;font-weight:800;}
  .hero h1 span{color:var(--accent);}
  .hero p{font-size:18px;color:var(--muted);max-width:640px;margin:0 auto;}
  .hero .sub{font-size:14px;color:var(--muted);margin-top:12px;font-weight:600;}
  .hero .cta-row{margin-top:26px;}
  section{padding:28px 0;}
  h2{color:var(--ink);margin-bottom:16px;font-size:24px;letter-spacing:-.4px;font-weight:800;}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;}
  .card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px;box-shadow:var(--shadow);}
  .card h3{color:var(--ink);margin-bottom:8px;font-size:17px;}
  .card p{font-size:15px;color:var(--muted);}
  ul.tips{margin:8px 0 8px 22px;}
  ul.tips li{margin:8px 0;}
  ol.steps{margin:8px 0 8px 22px;}
  ol.steps li{margin:8px 0;}
  .example{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px;box-shadow:var(--shadow);margin-bottom:14px;}
  .example b{color:var(--ink);}
  .chip{display:inline-block;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:6px 14px;margin:4px 4px 0 0;font-size:14px;font-weight:600;}
  .cta{text-align:center;background:linear-gradient(135deg,#4f46e5,#2563eb);color:#fff;border-radius:var(--radius);padding:40px 26px;margin:20px 0;box-shadow:0 14px 40px rgba(79,70,229,.35);}
  .cta h2{color:#fff;margin-bottom:10px;}
  .cta p{margin-bottom:22px;font-size:16px;opacity:.92;}
  .cta .btn{background:#fff;color:var(--accent);font-size:17px;padding:14px 34px;box-shadow:0 6px 18px rgba(0,0,0,.15);}
  .faq p{margin-bottom:10px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;}
  .faq b{color:var(--ink);}
  .note{font-size:13px;color:var(--muted);}
  .related{margin-top:36px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:26px;}
  .related h2{font-size:20px;margin-bottom:12px;}
  .related a{display:inline-block;background:var(--accent-soft);color:var(--accent);border:1px solid transparent;border-radius:999px;padding:6px 14px;margin:4px 6px 0 0;text-decoration:none;font-size:14px;font-weight:600;}
  .related a:hover{background:#e0e7ff;}
  footer{background:#fff;border-top:1px solid var(--line);padding:24px 0;text-align:center;font-size:14px;color:var(--muted);}
  footer a{color:var(--ink);font-weight:600;text-decoration:none;}
  @media(max-width:600px){.hero h1{font-size:28px;}.btn{display:block;margin:8px 0;text-align:center;}.nav-links{gap:12px;}}
</style>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "26b749ec88b5405bb9524de7d3deb750"}'></script><!-- End Cloudflare Web Analytics -->
</head>
<body>
<header>
  <div class="wrap nav">
    <div class="logo">Pixel<em>Fix</em></div>
    <div class="nav-links">
      <a href="{base}/index.html">Tools</a>
      <a href="{base}/compress-image.html">Compress</a>
      <a href="{base}/restore.html">Restore</a>
      <a href="{base}/index.html#tool">Animate</a>
      <a class="btn" href="{base}/index.html">Unlock All – $9.99</a>
    </div>
  </div>
</header>

<div class="wrap">
  <div class="hero">
    <div class="eyebrow">🔒 100% in your browser · nothing uploaded · no signup</div>
    <h1>{h1}</h1>
    <p>{hero_p}</p>
    <p class="sub">{hero_sub}</p>
    <div class="cta-row">
      <a class="btn" href="{base}/index.html" style="font-size:17px;padding:14px 30px;">Try It Free — No Signup →</a>
    </div>
  </div>

  {sections}

  <div class="cta">
    <h2>{cta_h2}</h2>
    <p>{cta_p}</p>
    <a class="btn" href="{base}/index.html">Animate Your Photo Now — Free →</a>
  </div>

  <div class="related">
    <h2>More Ways to Bring Photos to Life</h2>
    {related}
    <p style="margin-top:14px;font-size:13px;color:var(--muted);">Every tool above runs entirely in your browser — your photos never leave your device.</p>
  </div>
</div>

<footer>
  <a href="{base}/index.html">PixelFix</a> · <a href="{base}/restore.html">Restore</a> · <a href="{base}/passport-photo.html">Passport</a> · <a href="{base}/compress-image.html">Compress</a> · <a href="{base}/remove-bg.html">Remove BG</a> · <a href="{base}/pdf-tools.html">PDF</a> · Ai_harryone@outlook.com
</footer>
</body>
</html>
'''

def faq_block(items):
    ps = ''.join('<p><b>%s</b> %s</p>' % (q, a) for q, a in items)
    return '<section class="faq">\n<h2>FAQ</h2>\n%s</section>' % ps

def ldjson(items):
    qa = []
    for q, a in items:
        qa.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"','\\"'), a.replace('"','\\"')))
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % ','.join(qa)

def sec(title, body):
    return '<section>\n<h2>%s</h2>\n%s\n</section>' % (title, body)

def card(h3, p):
    return '<div class="card"><h3>%s</h3><p>%s</p></div>' % (h3, p)

# ---- Page content ----

PAGES = [
  {
    'slug': 'animate-old-photos.html',
    'title': 'Animate Old Photos — Free Browser Tool (No Upload, No Signup)',
    'meta': 'Animate old photos in your browser for free: slow push-ins, pans and fades on any family photo. Nothing is uploaded, no account needed. Export as a GIF in seconds.',
    'h1': 'Animate Old Photos — Free, in Your Browser',
    'hero_p': 'Give a faded family photo slow, quiet motion — push-in, pan, fade — right in your browser. Your photo never leaves your device.',
    'hero_sub': 'Free · No signup · No upload · Works on JPG & PNG',
    'sections': [
      sec('What “Animating an Old Photo” Really Means', '<p>Animating a still photo is just <b>motion applied to an image</b> — a slow zoom toward a face, a gentle drift across a scene, a soft dissolve. It’s the classic <b>Ken Burns effect</b>: the same move used in nearly every documentary, and it’s what makes an old photo feel alive instead of frozen.</p><p style="margin-top:10px;">Unlike AI face-reanimation services, the effect is applied <b>entirely in your browser</b>. You upload nothing, sign up for nothing, and your photos are never sent to a server.</p>'),
      sec('How to Animate an Old Photo in 30 Seconds', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix</a> on any device.',
        'Upload or drag in a photo (JPG or PNG, 1000px+ scans animate best).',
        'Pick a motion — <b>Push-in</b> (slow zoom), <b>Pull-back</b>, <b>Pan across</b>, <b>Pan up</b>, or <b>Fade in</b>.',
        'Hit <b>Export</b> — you get an animated GIF, ready to share.'
      ])),
      sec('Which Motion Suits Which Photo', '''
        <div class="example"><b>Push-in</b> — a slow zoom toward the subject. The classic “memory” feel for portraits and weddings.</div>
        <div class="example"><b>Pan across</b> — a horizontal drift. Great for landscapes and wide group shots.</div>
        <div class="example"><b>Pan up</b> — a vertical rise. Lovely for tall portraits or statues.</div>
        <div class="example"><b>Pull-back</b> — zoom out to reveal the whole scene. Perfect for a final shot in a tribute.</div>
        <div class="example"><b>Fade in</b> — a soft dissolve from a warm field. Minimal and elegant for memorials.</div>
      '''),
      sec('Tips That Make Animated Photos Look Good', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>Use your highest-resolution scan.</b> A clear 1000px+ image animates far more smoothly than a phone photo of a print.',
        '<b>Pick a photo with a clear subject</b> — a face, a couple, a landmark. Busy group shots are harder to animate well.',
        '<b>Slow is emotional.</b> For memorials and tributes, a 3–4 second slow push-in beats a quick zoom every time.',
        '<b>Crop first.</b> Most of the magic is choosing what the camera slowly moves toward — decide that before you animate.'
      ])),
      faq_block([
        ('Is animating old photos free?', 'Yes — all 5 motion effects are free with a small watermark. Unlimited Alive (face animation) plus watermark-free 720p export is a one-time $9.99, no subscription.'),
        ('Are my photos uploaded to a server?', 'No. Everything runs in your browser. Your photo never leaves your device.'),
        ('What formats can I animate?', 'JPG and PNG. GIF output for sharing.'),
        ('Do I need an account?', 'No signup, no email, no account. Open the page and it works.')
      ]),
    ],
    'cta_h2': 'Bring One of Your Photos to Life Now.',
    'cta_p': 'Free to try — no signup, no upload. Your first animation takes 30 seconds.',
  },
  {
    'slug': 'revive-old-photos.html',
    'title': 'Revive Old Photos — Bring Them Back to Life in Your Browser (Free)',
    'meta': 'Revive old photos and bring a loved one back to life: gentle motion plus real face animation (blink, smile, breathe). Runs 100% in your browser, nothing uploaded. Free to try.',
    'h1': 'Revive Old Photos — Bring Them Back to Life',
    'hero_p': 'Not just motion — a real face coming alive: a blink, a faint smile, a soft breath. Done in your browser, on your device, with the photo never uploaded.',
    'hero_sub': 'Try Alive once free · One-time $9.99 to unlock unlimited',
    'sections': [
      sec('Why “Revive Old Photos” Is a Search on People’s Minds', '<p>“Revive old photos” is one of the most-searched photo animation requests — usually for the same reason: someone has a photo of a parent or grandparent, and they want to feel that person close again. A slow push-in already does something. A photo that <b>blinks, smiles, and breathes</b> does something else entirely.</p>'),
      sec('Two Ways PixelFix Brings a Photo to Life', '<div class="grid">%s</div>' % (
        card('Ken Burns Motion', 'A slow push-in or pan — the classic, elegant way to make any old photo feel like a living memory. All 5 effects are free.') +
        card('Alive Face Animation', 'A face detected in the photo <b>blinks, smiles and breathes</b> — the closest most of us get to seeing someone again. One free try, then unlock unlimited for a one-time $9.99.') +
        card('100% Private', 'Face detection and animation run on your device with MediaPipe — the photo never leaves your browser.') +
        card('GIF Export', 'Share the result as an animated GIF, wherever you share memories.')
      )),
      sec('How to Use the Alive Effect', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix</a> and upload a clear, face-forward photo.',
        'Wait for the <b>Alive ✨</b> button to appear (it shows once a face is detected — faces occupying 1/3 of the frame work best).',
        'Click it and preview the animation — blink, smile, breath.',
        'Export a GIF. Your first Alive is free; unlimited Alive + clean 720p is a one-time $9.99.'
      ])),
      sec('Photos That Revive Best', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>One clear face, looking at the camera</b> — a large, well-lit portrait is ideal.',
        '<b>Face roughly a third of the frame</b> — too small and detection struggles, too close and it crops oddly.',
        '<b>Good contrast</b> — old faded prints still work, but a sharper scan of the print beats a photo of it.',
        '<b>No heavy shadows over the eyes</b> — the blink animation needs to see the eyes.'
      ])),
      faq_block([
        ('Is reviving old photos free?', 'The 5 Ken Burns motion effects are free. The Alive face animation is free for one try, then a one-time $9.99 unlocks it forever — no subscription.'),
        ('Does it use a cloud AI?', 'No. Face detection and animation run locally in your browser. Your photo never leaves your device.'),
        ('Why does my photo need a clear face?', 'The Alive effect animates real facial landmarks (eyes, mouth, jaw). No face detected, no animation to apply — that’s why a clear face-forward shot works best.'),
        ('Can I use it commercially?', 'Yes — anything you export is yours to use.')
      ]),
    ],
    'cta_h2': 'See a Loved One Move Again.',
    'cta_p': 'Free to try — one photo, one blink, and you’ll understand.',
  },
  {
    'slug': 'ken-burns-effect.html',
    'title': 'Ken Burns Effect — Make Any Photo Slowly Move in Your Browser (Free)',
    'meta': 'Make a Ken Burns effect for any photo in your browser: slow zoom, pan and fade with smooth motion. Free, no signup, no upload. Export as GIF.',
    'h1': 'Ken Burns Effect — the Slow Motion That Makes Photos Feel Alive',
    'hero_p': 'The documentary-maker’s move — a slow push-in, a drifting pan — applied to your own photos in seconds. Free, in your browser.',
    'hero_sub': 'Free · No signup · No upload',
    'sections': [
      sec('What Is the Ken Burns Effect?', '<p>The <b>Ken Burns effect</b> is a slow, continuous zoom or pan applied to a still photograph, named after the documentary filmmaker who made it famous. It’s the quiet, cinematic motion you see in nearly every documentary, memorial video and history show — and it’s the single most effective way to make an old photo feel alive.</p>'),
      sec('Why It Works on Old Photos', '<p>A still photo is a frozen moment; motion is what a memory feels like. The Ken Burns effect <b>guides the viewer’s eye</b> — a slow push toward a face pulls you into the emotion, a gentle pan across a scene tells a wider story. It’s simple, subtle, and almost always the right choice for family photos.</p>'),
      sec('The 5 Effects You Get Free', '''
        <div class="example"><b>Push-in</b> — a slow zoom toward the subject. The classic “memory” move.</div>
        <div class="example"><b>Pull-back</b> — zoom out to reveal the whole scene. Great for final shots.</div>
        <div class="example"><b>Pan across</b> — a horizontal drift, perfect for wide group photos and landscapes.</div>
        <div class="example"><b>Pan up</b> — a vertical rise for tall portraits and buildings.</div>
        <div class="example"><b>Fade in</b> — a gentle dissolve from a warm field. Elegant and minimal.</div>
      '''),
      sec('How to Make a Ken Burns Effect in 30 Seconds', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix</a>.',
        'Upload any photo — the tool applies the effect live as you choose.',
        'Tap between Push-in, Pull-back, Pan across, Pan up and Fade to preview each.',
        'Export an animated GIF. All 5 effects are free with a small watermark.'
      ])),
      sec('Ken Burns in a Tribute Video', '<p>If you’re assembling a memorial or family-history video, the standard trick is to give each photo a different motion so the sequence doesn’t feel repetitive: <b>push-in on one, pan across the next, fade on the third</b>. PixelFix makes each clip in seconds, and everything stays on your device until you’re ready to assemble it.</p>'),
      faq_block([
        ('What is the Ken Burns effect?', 'A slow, continuous zoom or pan applied to a still photo — the documentary technique that makes photographs feel alive and cinematic.'),
        ('Is it free?', 'Yes — all 5 motion effects are free with a small watermark. One-time $9.99 removes it and unlocks unlimited Alive face animation.'),
        ('Do I need video software?', 'No — the effect is applied and exported as a GIF directly in your browser.'),
        ('Can I use it for a memorial video?', 'Absolutely — slow push-ins and fades are exactly what memorial slideshows are made of.')
      ]),
    ],
    'cta_h2': 'Make Any Photo Move in 30 Seconds.',
    'cta_p': 'Free to try — all five effects, no signup, no upload.',
  },
  {
    'slug': 'family-history-video.html',
    'title': 'Family History Video — Turn Old Family Photos into a Tribute Slideshow',
    'meta': 'Turn old family photos into a gentle, moving family history video: animate scanned photos with slow motion in your browser. Free, private, no upload.',
    'h1': 'Family History Video — Let Old Family Photos Move',
    'hero_p': 'Scan the shoebox, drop the photos in, and give them the slow motion they deserve — a tribute to your family’s history, made privately in your browser.',
    'hero_sub': 'Free to try · Runs on your device · Nothing uploaded',
    'sections': [
      sec('The Problem with Family History Photos', '<p>Most family history sits in shoeboxes and albums — still, silent, easy to skip. When you want to <b>tell your family’s story</b>, a slideshow of static photos holds attention for seconds. A slideshow where each photo <b>slowly moves</b> — pushing in, drifting across — becomes something you watch, and then send to every relative.</p>'),
      sec('How to Build a Family History Video', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        '<b>Collect your best photos</b> — 8–15 sharp scans, in chronological order if you can.',
        'Animate each in <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix</a>: vary the motion (push-in, pan, fade) so the sequence feels alive.',
        'Export each as a GIF, then drop them into any video editor in order.',
        'Add captions or narration between clips — names, dates, one line of story each.',
        'Export the finished video and share it with the family.'
      ])),
      sec('A Photo Sequence That Tells a Story', '''
        <div class="example"><b>Open on a wide shot</b> — the family farm, the old house. A slow pan across establishes where the story lives.</div>
        <div class="example"><b>Move to a portrait</b> — a push-in on the person the story is about.</div>
        <div class="example"><b>Cut to a moment</b> — a wedding, a reunion, a favorite day. Fade in, hold, fade out.</div>
        <div class="example"><b>Close with the descendant</b> — the family continuing. A gentle pull-back to end on the whole picture.</div>
      '''),
      sec('Privacy Matters More Here Than Anywhere', '<p>Family photos are the most personal thing you own. That’s why PixelFix processes everything <b>in your browser</b> — the scans of your grandparents never touch a server, never sit in someone else’s cloud, and never get used to train a model. The animation, the face detection, the GIF export: all on your device.</p>'),
      faq_block([
        ('How do I turn photos into a video?', 'Animate each photo in PixelFix (export as GIF), then assemble the GIFs in any free video editor. No cloud service ever sees your photos.'),
        ('Is it free?', 'Yes — all 5 motion effects are free. A one-time $9.99 removes the watermark and unlocks unlimited Alive face animation.'),
        ('Can I use photos of people who have passed?', 'Yes — this is exactly what the tool is for. The Alive face animation is one free try if you want to see a loved one blink, smile and breathe.'),
        ('Do my photos get uploaded?', 'Never. Everything runs locally in your browser.')
      ]),
    ],
    'cta_h2': 'Start Your Family’s Tribute Today.',
    'cta_p': 'Free to try — turn your first family photo into a moving memory in 30 seconds.',
  },
  {
    'slug': 'memorial-video-maker.html',
    'title': 'Memorial Video Maker — Animate Photos of a Loved One (Private, Free to Try)',
    'meta': 'Make a gentle memorial video from photos of a loved one: slow motion plus optional face animation, processed privately in your browser. Nothing uploaded. Free to try.',
    'h1': 'Memorial Video Maker — Photos of a Loved One, Gently Moving',
    'hero_p': 'For a memorial service or a private tribute: photos of someone you love, animated with slow, quiet motion. Done privately, on your device, with nothing uploaded.',
    'hero_sub': 'Free to try · Private by design · No account',
    'sections': [
      sec('Why Motion Belongs in a Memorial', '<p>At a memorial, a still photo is a reminder; a photo that <b>slowly moves</b> is a presence. A slow push-in toward your father’s face, a gentle pan across your grandmother’s garden — motion turns a slideshow into a tribute, and it does it without a single word.</p><p style="margin-top:10px;">This is a hard moment, and you shouldn’t have to hand your most private photos to a cloud app to honor someone. PixelFix runs entirely in your browser.</p>'),
      sec('What You Can Create', '<div class="grid">%s</div>' % (
        card('Gentle Motion', 'Slow push-ins, pans and fades — the classic memorial slideshow feel. All 5 effects free.') +
        card('Alive Face Animation', 'A loved one’s photo that blinks, smiles and breathes — one free try, then one-time $9.99.') +
        card('Private Processing', 'Every pixel stays on your device. No upload, no cloud, no account.') +
        card('GIF Export', 'Export each tribute clip as a GIF and assemble them in any video editor.')
      )),
      sec('How to Make a Memorial Video', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Choose 10–15 of your favorite, clearest photos.',
        'Animate each in <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix</a> — slow push-ins and fades read best.',
        'Vary the motion between photos so the sequence breathes.',
        'Export GIFs and assemble them in a video editor, usually set to a piece of music.',
        'Keep it private or share it with family — your call, because it never left your device.'
      ])),
      sec('When the Photo Has a Face', '<p>If a photo shows your loved one clearly and facing the camera, the <b>Alive</b> effect can make them blink, smile and breathe — often the single most moving moment in a tribute. It works locally with a face-detection model that runs in your browser. Try it once free, and if it’s right for your tribute, unlock unlimited for a one-time $9.99.</p>'),
      faq_block([
        ('Is a memorial video maker really free?', 'Yes — all 5 motion effects are free with a small watermark. One-time $9.99 removes it and unlocks unlimited Alive face animation.'),
        ('Are the photos uploaded?', 'No. Everything — face detection, animation, GIF export — runs in your browser. The photos never leave your device.'),
        ('Can the face actually move?', 'The Alive effect animates a detected face — blink, smile, breath. It’s most effective on clear, face-forward photos.'),
        ('Can I use it for a funeral service?', 'Yes — this is exactly the use it was built for. Export clips and assemble them for the service or the memory table.')
      ]),
    ],
    'cta_h2': 'Give Your Memories the Motion They Deserve.',
    'cta_p': 'Free to try, private by design — animate your first photo now.',
  },
  {
    'slug': 'old-photo-gif-maker.html',
    'title': 'Old Photo GIF Maker — Animate Any Old Photo & Export a GIF (Free)',
    'meta': 'Turn an old photo into an animated GIF in your browser: slow zoom, pan and fade, exported as a shareable GIF. Free, no signup, nothing uploaded.',
    'h1': 'Old Photo GIF Maker — from Still Photo to Living GIF',
    'hero_p': 'A slow push-in. A gentle pan. The motion of a memory, exported as a GIF you can share anywhere — made in your browser, nothing uploaded.',
    'hero_sub': 'Free · No signup · Exports as GIF',
    'sections': [
      sec('Why a GIF?', '<p>A GIF is the most shareable video format there is: it plays everywhere — messaging apps, social media, email, memorial pages — with no player, no log-in, no clicking “play.” An animated old photo as a GIF lets a memory move wherever you send it.</p>'),
      sec('How to Make an Old Photo GIF in 30 Seconds', '<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % x for x in [
        'Open <a href="{base}/index.html" style="color:#4f46e5;font-weight:bold;">PixelFix</a> and upload your photo.',
        'Preview a motion: Push-in, Pull-back, Pan across, Pan up or Fade in.',
        'Hit <b>Export GIF</b> — the tool renders the animation locally.',
        'Save the GIF and share it anywhere that accepts images.'
      ])),
      sec('GIFs That Look Right', '<ul class="tips">%s</ul>' % ''.join('<li>%s</li>' % x for x in [
        '<b>Keep the motion slow</b> — a 3–4 second slow push-in reads as emotional; a fast zoom reads as a tech demo.',
        '<b>One clear subject</b> — the eye follows what moves; give it one thing to follow.',
        '<b>Start from a good scan</b> — GIF compresses in flat color areas, so a sharp, high-contrast scan exports cleaner.',
        '<b>Match the mood to the motion</b> — push-in for portraits, pan across for landscapes, fade for endings.'
      ])),
      sec('When to Add Alive', '<p>If your photo has a clear face, wait a moment for the <b>Alive ✨</b> button to appear — it animates a real blink, smile and breath. It’s free for one try, and a one-time $9.99 unlocks unlimited Alive plus a clean, watermark-free 720p export.</p>'),
      faq_block([
        ('How do I turn a photo into a GIF?', 'Upload it to PixelFix, pick a motion, and hit Export GIF — the animation is rendered locally in your browser.'),
        ('Is it free?', 'Yes — all 5 motion effects export free with a small watermark. One-time $9.99 removes the watermark and unlocks unlimited Alive face animation.'),
        ('Where can I share the GIF?', 'Anywhere — messaging apps, social media, email, memorial and family pages. GIFs play everywhere.'),
        ('Does it upload my photo?', 'No. The photo is processed entirely on your device.')
      ]),
    ],
    'cta_h2': 'Turn a Photo into a GIF That Moves.',
    'cta_p': 'Free to try — export your first animated photo GIF in 30 seconds.',
  },
]

def related_links(slug):
    items = []
    items.append('<a href="{base}/restore.html">Restore Old Photos</a>')
    items.append('<a href="{base}/index.html">Animate Old Photos</a>')
    for p in PAGES:
        if p['slug'] != slug:
            label = p['h1'].split(' — ')[0]
            items.append('<a href="{base}/seo/%s">%s</a>' % (p['slug'], label))
    items.append('<a href="{base}/seo/revive-old-photos.html">Revive Old Photos</a>')
    return '\n    '.join(items)

def render(page):
    html = HEAD
    subs = {
        '{title}': page['title'],
        '{meta}': page['meta'],
        '{base}': BASE,
        '{slug}': page['slug'],
        '{ldjson}': _ld_for(page),
        '{h1}': page['h1'],
        '{hero_p}': page['hero_p'],
        '{hero_sub}': page['hero_sub'],
        '{sections}': '\n\n'.join(page['sections']),
        '{cta_h2}': page['cta_h2'],
        '{cta_p}': page['cta_p'],
        '{related}': related_links(page['slug']),
    }
    for k, v in subs.items():
        if k == '{base}':
            continue
        html = html.replace(k, v)
    # replace {base} LAST so it also resolves inside {sections}/{related} content
    html = html.replace('{base}', BASE)
    return html

def _ld_for(page):
    import re
    faq_section = [s for s in page['sections'] if s.startswith('<section class="faq">')]
    if not faq_section:
        return ''
    items = re.findall(r'<p><b>(.*?)</b> (.*?)</p>', faq_section[0])
    return ldjson(items)

if __name__ == '__main__':
    for p in PAGES:
        html = render(p)
        with open(os.path.join(OUT, p['slug']), 'w', encoding='utf-8') as f:
            f.write(html)
        print('wrote', p['slug'], len(html), 'bytes')
    print('done —', len(PAGES), 'pages')
