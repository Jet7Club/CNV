from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

anchors = [
    "Des images pour ressentir l’atmosphère",
    "Des images pour ressentir l'atmosphère",
]

pos = -1
for a in anchors:
    pos = s.find(a)
    if pos != -1:
        break

if pos == -1:
    raise SystemExit('Gallery chapter title not found')

# Limit the edit to the gallery chapter area following the title.
end = min(len(s), pos + 25000)
chunk = s[pos:end]

patterns = [
    r'<button\b[^>]*>\s*Tout\s*</button>',
    r'<button\b[^>]*(?:data-filter|data-cat|data-category)=["\'](?:all|tout)["\'][^>]*>.*?</button>',
]

removed = 0
for pat in patterns:
    chunk, n = re.subn(pat, '', chunk, count=1, flags=re.I | re.S)
    if n:
        removed += n
        break

if removed != 1:
    raise SystemExit('Could not uniquely remove the Tout button in the gallery chapter')

s = s[:pos] + chunk + s[end:]
p.write_text(s, encoding='utf-8')
print('Removed Tout button from gallery chapter')
