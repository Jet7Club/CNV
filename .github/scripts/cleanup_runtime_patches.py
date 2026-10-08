from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
original = s

# 1) Remove the older standalone Members translation observer.
# The newer mobile-nav script already owns the desktop/mobile Members label,
# so keeping both observers creates duplicate work on each language change.
s, n_members = re.subn(
    r'\s*<script id=["\']members-nav-translation["\']>.*?</script>\s*',
    '\n',
    s,
    count=1,
    flags=re.S,
)

# 2) Remove the obsolete one-off "Luxury without rigidity" DOM scan from the
# mobile navigation script. Nature-abundance translations now live in the
# translation data and should not be patched by scanning the whole document.
mobile_pat = r'(<script id=["\']cnv-mobile-nav-script-20261008["\']>)(.*?)(</script>)'
m = re.search(mobile_pat, s, flags=re.S)
n_luxury = 0
if m:
    body = m.group(2)
    body2, n_luxury = re.subn(
        r'\n\s*// Fix the known EN mixed-language sentence without disturbing markup\.\s*\n\s*document\.querySelectorAll\([^\n]*\)\.forEach\(el=>\{.*?\}\);\s*\n',
        '\n',
        body,
        count=1,
        flags=re.S,
    )
    if n_luxury:
        s = s[:m.start()] + m.group(1) + body2 + m.group(3) + s[m.end():]

# 3) Defensive cleanup: remove duplicate copies of our injected stability style,
# retaining the first one only.
style_pat = r'<style id=["\']cnv-image-loading-stability-20261008["\']>.*?</style>'
styles = list(re.finditer(style_pat, s, flags=re.S))
n_style_dupes = 0
if len(styles) > 1:
    for mm in reversed(styles[1:]):
        s = s[:mm.start()] + s[mm.end():]
        n_style_dupes += 1

if s == original:
    print('Runtime cleanup already applied; no index changes')
else:
    p.write_text(s, encoding='utf-8')
    print(f'Runtime cleanup applied: members_observer={n_members}, stale_luxury_scan={n_luxury}, duplicate_styles={n_style_dupes}')
