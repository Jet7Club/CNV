from pathlib import Path
import re, html

index_path = Path('index.html')
members_path = Path('members.html')
s = index_path.read_text(encoding='utf-8')
members = members_path.read_text(encoding='utf-8')

# 1) Main navigation: one native anchor to the embedded Members section.
nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S)
if not nav_match:
    raise SystemExit('Navigation block not found')
nav = nav_match.group(0)
nav = re.sub(
    r'\s*<a\b[^>]*href=["\'](?:\./)?members\.html["\'][^>]*>.*?</a>\s*',
    '\n', nav, flags=re.I|re.S,
)
nav = re.sub(
    r'\s*<a\b[^>]*href=["\']#members["\'][^>]*>.*?</a>\s*',
    '\n', nav, flags=re.I|re.S,
)
art = re.search(r'<a\b[^>]*href=["\']#artoflife["\'][^>]*>.*?</a>', nav, flags=re.I|re.S)
if not art:
    raise SystemExit('Art of Life link not found in main nav')
link = ('<a href="#members" id="membersNavLink" '
        'style="display:inline-flex!important;visibility:visible!important;opacity:1!important;'
        'align-items:center!important;white-space:nowrap!important;color:#d9b762!important;'
        'font-weight:700!important;position:relative!important;z-index:9999!important;">Membres</a>')
nav = nav[:art.end()] + '\n' + link + '\n' + nav[art.end():]
s = s[:nav_match.start()] + nav + s[nav_match.end():]

# 2) Remove any prior embedded Members block so the script is idempotent.
s = re.sub(
    r'\s*<!-- CNV MEMBERS EMBED START -->.*?<!-- CNV MEMBERS EMBED END -->\s*',
    '\n', s, flags=re.I|re.S,
)

# 3) Embed the complete members.html document into index.html via srcdoc.
# This keeps its CSS/JS isolated and avoids collisions with the 19 MB main page.
# The members page's own sticky nav is removed because the main CNV nav remains visible.
members_embedded = re.sub(r'<nav\b[^>]*>.*?</nav>', '', members, count=1, flags=re.I|re.S)
escaped = html.escape(members_embedded, quote=True)
section = f'''\n<!-- CNV MEMBERS EMBED START -->
<section id="members" class="cnv-members-embedded" style="padding:0;margin:0;background:#07110d;scroll-margin-top:90px;">
  <iframe id="cnvMembersFrame" title="CNV Members" srcdoc="{escaped}" style="display:block;width:100%;min-height:2400px;border:0;background:#07110d;" loading="eager"></iframe>
</section>
<script id="cnv-members-height-sync">
(function(){{
  const f=document.getElementById('cnvMembersFrame');
  if(!f)return;
  const fit=()=>{{
    try{{
      const d=f.contentDocument;
      if(d) f.style.height=Math.max(1200,d.documentElement.scrollHeight,d.body?d.body.scrollHeight:0)+'px';
    }}catch(e){{}}
  }};
  f.addEventListener('load',()=>{{fit();setTimeout(fit,100);setTimeout(fit,500);}});
  window.addEventListener('resize',fit);
}})();
</script>
<!-- CNV MEMBERS EMBED END -->\n'''

# Insert before footer when possible, otherwise before </body>.
footer = re.search(r'<footer\b', s, flags=re.I)
if footer:
    s = s[:footer.start()] + section + s[footer.start():]
else:
    body_end = re.search(r'</body>', s, flags=re.I)
    if not body_end:
        raise SystemExit('Could not find footer or </body> insertion point')
    s = s[:body_end.start()] + section + s[body_end.start():]

# 4) Remove obsolete runtime Members-link creator/translator if present.
s = re.sub(
    r'\s*<script id=["\']members-nav-translation["\']>.*?</script>\s*',
    '\n', s, count=1, flags=re.I|re.S,
)

# 5) Validate the final source.
final_nav = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S).group(0)
if len(re.findall(r'href=["\']#members["\']', final_nav, flags=re.I)) != 1:
    raise SystemExit('Expected exactly one #members link in main nav')
if re.search(r'href=["\'](?:\./)?members\.html["\']', final_nav, flags=re.I):
    raise SystemExit('members.html link still present in main nav')
if s.count('<!-- CNV MEMBERS EMBED START -->') != 1 or 'id="cnvMembersFrame"' not in s:
    raise SystemExit('Embedded Members section validation failed')

index_path.write_text(s, encoding='utf-8')
print('OK: members.html embedded into index.html; main nav points to #members')
