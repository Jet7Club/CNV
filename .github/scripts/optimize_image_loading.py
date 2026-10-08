from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Add lightweight browser hints to images. Keep the first three eager for the header/hero.
count=0
seen=0

def repl(m):
    global seen,count
    tag=m.group(0)
    seen+=1
    if seen<=3:
        if 'decoding=' not in tag:
            tag=tag[:-1]+' decoding="async">'
            count+=1
        return tag
    changed=False
    if 'loading=' not in tag:
        tag=tag[:-1]+' loading="lazy">'
        changed=True
    if 'decoding=' not in tag:
        tag=tag[:-1]+' decoding="async">'
        changed=True
    if changed:
        count+=1
    return tag

s=re.sub(r'<img\b[^>]*>',repl,s,flags=re.I)

# Ensure images do not exceed their boxes while decoding/loading.
marker='cnv-image-loading-stability-20261008'
css='''\n<style id="cnv-image-loading-stability-20261008">\nimg{max-width:100%;height:auto}\n</style>\n'''
if marker not in s:
    if '</head>' in s:
        s=s.replace('</head>',css+'</head>',1)
    else:
        s=css+s

p.write_text(s,encoding='utf-8')
print(f'Optimized {count} image tag(s) for faster, more stable loading')
