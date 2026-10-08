from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

# Ensure Members is a real link in the main nav, directly after Art of Life.
nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S)
if not nav_match:
    raise SystemExit('Navigation block not found')
nav = nav_match.group(0)

# Remove any existing Members link from the nav so we can insert exactly one in the right place.
nav = re.sub(r'\s*<a\b[^>]*href=["\']members\.html["\'][^>]*>.*?</a>\s*', '\n', nav, flags=re.I|re.S)
art = re.search(r'<a\b[^>]*href=["\']#artoflife["\'][^>]*>.*?</a>', nav, flags=re.I|re.S)
if not art:
    raise SystemExit('Art of Life link not found in main nav')
link = '<a href="members.html" id="membersNavLink">Membres</a>'
nav = nav[:art.end()] + '\n' + link + nav[art.end():]
s = s[:nav_match.start()] + nav + s[nav_match.end():]

# Remove any runtime block that creates Members dynamically.
patterns = [
    r'\n\s*let members=\[\.\.\.nav\.querySelectorAll\(["\']a["\']\)\]\.find\(a=>/members\\\.html\$/i\.test\(a\.getAttribute\(["\']href["\']\)\|\|["\']["\']\)\);\s*\n\s*if\(!members && art\)\{.*?\n\s*\}\s*',
    r'\n\s*if\(!members && art\)\{.*?members\.href=["\']members\.html["\'];.*?\n\s*\}\s*',
]
for pat in patterns:
    s = re.sub(pat, '\n', s, count=1, flags=re.S)

# Keep translation of the existing native link, but never create it dynamically.
# Any stale standalone members-nav observer is redundant and removed here.
s = re.sub(r'\s*<script id=["\']members-nav-translation["\']>.*?</script>\s*', '\n', s, count=1, flags=re.S)

if s == original:
    print('Native Members nav already clean; no index changes')
else:
    p.write_text(s, encoding='utf-8')
    print('Members integrated natively in main nav; dynamic creation removed')
