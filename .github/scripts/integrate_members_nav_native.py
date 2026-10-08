from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S)
if not nav_match:
    raise SystemExit('Navigation block not found')

nav = nav_match.group(0)

# Remove every existing Members/Membres/Miembros link from the MAIN nav,
# then insert exactly one native, explicitly visible clickable link directly after Art of Life.
nav = re.sub(
    r'\s*<a\b[^>]*href=["\'](?:\./)?members\.html["\'][^>]*>.*?</a>\s*',
    '\n',
    nav,
    flags=re.I|re.S,
)
art = re.search(r'<a\b[^>]*href=["\']#artoflife["\'][^>]*>.*?</a>', nav, flags=re.I|re.S)
if not art:
    raise SystemExit('Art of Life link not found in main nav')

native = ('<a href="members.html" id="membersNavLink" '
          'style="display:inline-flex!important;visibility:visible!important;opacity:1!important;'
          'align-items:center!important;white-space:nowrap!important;color:#d9b762!important;'
          'font-weight:700!important;position:relative!important;z-index:9999!important;">Membres</a>')
nav = nav[:art.end()] + '\n' + native + '\n' + nav[art.end():]
s = s[:nav_match.start()] + nav + s[nav_match.end():]

# Remove obsolete runtime code that could CREATE the Members link dynamically.
s = re.sub(
    r'\n\s*let members=\[\.\.\.nav\.querySelectorAll\(["\']a["\']\)\]\.find\(a=>/members\\\.html\$/i\.test\(a\.getAttribute\(["\']href["\']\)\|\|["\']["\']\)\);\s*',
    '\n',
    s,
    count=1,
    flags=re.S,
)
s = re.sub(
    r'\n\s*if\(!members\s*&&\s*art\)\{.*?members\.href\s*=\s*["\']members\.html["\'];.*?\n\s*\}\s*',
    '\n',
    s,
    count=1,
    flags=re.S,
)

# Remove old standalone observer; translation is handled by the existing nav language sync.
s = re.sub(
    r'\s*<script id=["\']members-nav-translation["\']>.*?</script>\s*',
    '\n',
    s,
    count=1,
    flags=re.S,
)

# Validate the final source itself: exactly one native visible link inside the main nav.
final_nav = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S).group(0)
links = re.findall(r'<a\b[^>]*href=["\'](?:\./)?members\.html["\'][^>]*>', final_nav, flags=re.I)
if len(links) != 1:
    raise SystemExit(f'Expected exactly one native Members link in main nav, found {len(links)}')
if 'id="membersNavLink"' not in final_nav:
    raise SystemExit('Native Members link missing id=membersNavLink')
if 'display:inline-flex!important' not in final_nav:
    raise SystemExit('Members link visibility style missing')

p.write_text(s, encoding='utf-8')
print('OK: Members link is natively integrated and forced visible in the main navigation')
