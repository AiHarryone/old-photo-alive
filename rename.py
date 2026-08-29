# -*- coding: utf-8 -*-
import io, glob

# Display-name replacements (repo paths stay lowercase old-photo-alive)
REPLACEMENTS = [
    ('OldPhoto Alive', 'PixelFix'),
    ('OldPhotoAlive', 'PixelFix'),
    ('OldPhoto', 'PixelFix'),
    ('old photo alive', 'PixelFix'),
    ('OldPhotoAlive · Free', 'PixelFix'),
]

def fix(s):
    for old, new in REPLACEMENTS:
        s = s.replace(old, new)
    return s

files = glob.glob('*.html') + ['README.md', 'promotion/gen_seo_pages.py']
for fn in files:
    s = io.open(fn, encoding='utf-8').read()
    fixed = fix(s)
    if fixed != s:
        io.open(fn, 'w', encoding='utf-8').write(fixed)
        print('renamed', fn)
