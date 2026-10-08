from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if 'id="membersNavLink"' in s or "id='membersNavLink'" in s:
    print('Members nav link already present; no change.')
    raise SystemExit(0)

nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S)
if not nav_match:
    raise SystemExit('Navigation block not found')

nav = nav_match.group(0)
art = re.search(r'<a\b[^>]*href=["\']#artoflife["\'][^>]*>.*?</a>', nav, flags=re.I|re.S)
places = re.search(r'<a\b[^>]*href=["\']#places["\'][^>]*>.*?</a>', nav, flags=re.I|re.S)
if not art or not places or art.end() > places.start():
    raise SystemExit('Could not locate Art of Life followed by Destinations in nav')

link = '<a href="members.html" id="membersNavLink">Membres</a>'
nav2 = nav[:art.end()] + '\n' + link + '\n' + nav[art.end():]
s = s[:nav_match.start()] + nav2 + s[nav_match.end():]

translator = r'''<script id="members-nav-translation">
(function(){
  const labels={fr:'Membres',en:'Members',es:'Miembros'};
  function updateMembersNav(){
    const a=document.getElementById('membersNavLink');
    if(!a)return;
    const lang=(document.documentElement.lang||'fr').toLowerCase().slice(0,2);
    a.textContent=labels[lang]||labels.fr;
  }
  updateMembersNav();
  new MutationObserver(updateMembersNav).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>'''

if '</body>' in s:
    s = s.replace('</body>', translator + '\n</body>', 1)
else:
    s += '\n' + translator

p.write_text(s, encoding='utf-8')
print('Inserted Members link between Art of Life and Destinations.')
