from pathlib import Path
import re, html

index_path = Path('index.html')
members_path = Path('members.html')
s = index_path.read_text(encoding='utf-8')
members = members_path.read_text(encoding='utf-8')

# MAIN NAV: exactly one Members link immediately after Art of Life.
nav_match = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S)
if not nav_match:
    raise SystemExit('Navigation block not found')
nav = nav_match.group(0)
nav = re.sub(r'\s*<a\b[^>]*href=["\'](?:\./)?members\.html["\'][^>]*>.*?</a>\s*', '\n', nav, flags=re.I|re.S)
nav = re.sub(r'\s*<a\b[^>]*href=["\']#members["\'][^>]*>.*?</a>\s*', '\n', nav, flags=re.I|re.S)
art = re.search(r'<a\b[^>]*href=["\']#artoflife["\'][^>]*>.*?</a>', nav, flags=re.I|re.S)
if not art:
    raise SystemExit('Art of Life link not found in main nav')
link = ('<a href="#members" id="membersNavLink" '
        'style="display:inline-flex!important;visibility:visible!important;opacity:1!important;'
        'align-items:center!important;white-space:nowrap!important;color:#d9b762!important;'
        'font-weight:700!important;position:relative!important;z-index:9999!important;">Members</a>')
nav = nav[:art.end()] + '\n' + link + '\n' + nav[art.end():]
s = s[:nav_match.start()] + nav + s[nav_match.end():]

# Remove obsolete runtime patches that can recreate a duplicate Members link.
s = re.sub(r'\s*<script id=["\']members-nav-translation["\']>.*?</script>\s*', '\n', s, flags=re.I|re.S)
s = re.sub(r'\s*<script id=["\']cnv-mobile-nav-script-20261008["\']>.*?</script>\s*', '\n', s, flags=re.I|re.S)
s = re.sub(r'\s*<script id=["\']cnv-nav-language-final-20261010["\']>.*?</script>\s*', '\n', s, flags=re.I|re.S)

# Remove previous Members embed so this script is repeatable.
s = re.sub(r'\s*<!-- CNV MEMBERS EMBED START -->.*?<!-- CNV MEMBERS EMBED END -->\s*', '\n', s, flags=re.I|re.S)

# Embed members.html, isolated from the large main-page CSS/JS.
members_embedded = re.sub(r'<nav\b[^>]*>.*?</nav>', '', members, count=1, flags=re.I|re.S)
members_embedded = re.sub(r'<html\b([^>]*)lang=["\']?fr["\']?', r'<html\1lang="en"', members_embedded, count=1, flags=re.I)
members_embedded = members_embedded.replace('let lang="fr",ed="life";', 'let lang="en",ed="life";')

# Geographic-price markers requested for Local membership.
members_embedded = members_embedded.replace('3 000 € à 8 000 €', '3 000 € à 8 000 € *')
members_embedded = members_embedded.replace('300 € à 800 €', '300 € à 800 € *')
members_embedded = members_embedded.replace('600 € à 1 600 €', '600 € à 1600 € *')
members_embedded = members_embedded.replace('1 200 € à 3 200 €', '1200 € à 3200 € *')

# Show the geographic note below both the cards and the table whenever the selected edition contains a starred price.
geo_runtime = r'''
<script id="cnv-members-geographic-note">
(function(){
  function applyGeoNote(){
    try{
      const d=(typeof D!=='undefined' && typeof ed!=='undefined')?D[ed]:null;
      const hasStar=!!(d && d.p && d.p.some(v=>String(v).includes('*')));
      const geo=(typeof q==='function')?q('geo'):'* En fonction de la zone géographique';
      const cardsNote=document.getElementById('en');
      const tableNote=document.getElementById('gn');
      if(hasStar){
        if(cardsNote) cardsNote.textContent=geo;
        if(tableNote) tableNote.textContent=geo;
      }else{
        if(cardsNote && ed!=='visionary') cardsNote.textContent='';
        if(tableNote) tableNote.textContent='';
      }
    }catch(e){}
  }
  if(typeof R==='function'){
    const originalR=R;
    R=function(){originalR();applyGeoNote();};
  }
  if(typeof L==='function'){
    const originalL=L;
    L=function(x,b){originalL(x,b);applyGeoNote();};
  }
  if(typeof E==='function'){
    const originalE=E;
    E=function(x){originalE(x);applyGeoNote();};
  }
  applyGeoNote();
})();
</script>
'''
if '</body>' in members_embedded:
    members_embedded = members_embedded.replace('</body>', geo_runtime+'\n</body>', 1)
else:
    members_embedded += geo_runtime

escaped = html.escape(members_embedded, quote=True)
section = f'''\n<!-- CNV MEMBERS EMBED START -->
<section id="members" class="cnv-members-embedded" style="padding:0;margin:0;background:#07110d;scroll-margin-top:90px;">
  <iframe id="cnvMembersFrame" title="CNV Members" srcdoc="{escaped}" style="display:block;width:100%;min-height:2400px;border:0;background:#07110d;" loading="eager"></iframe>
</section>
<script id="cnv-members-height-sync">
(function(){{
  const f=document.getElementById('cnvMembersFrame');
  if(!f)return;
  const fit=()=>{{try{{const d=f.contentDocument;if(d)f.style.height=Math.max(1200,d.documentElement.scrollHeight,d.body?d.body.scrollHeight:0)+'px';}}catch(e){{}}}};
  f.addEventListener('load',()=>{{fit();setTimeout(fit,100);setTimeout(fit,500);}});
  window.addEventListener('resize',fit);
}})();
</script>
<!-- CNV MEMBERS EMBED END -->\n'''

# POSITION: Members immediately before Destinations (#places), therefore after Art de vivre.
places = re.search(r'<section\b[^>]*\bid=["\']places["\'][^>]*>', s, flags=re.I|re.S)
if not places:
    places = re.search(r'<[^>]+\bid=["\']places["\'][^>]*>', s, flags=re.I|re.S)
if not places:
    raise SystemExit('Destinations section #places not found')
s = s[:places.start()] + section + s[places.start():]

# English is the source/default language.
s = re.sub(r'<html\b([^>]*?)lang=["\'][^"\']+["\']', r'<html\1lang="en"', s, count=1, flags=re.I)

# Clean runtime controller: labels, mobile menu, language order/default.
runtime = r'''
<script id="cnv-nav-language-final-20261010">
(function(){
  const nav=document.querySelector('.top nav')||document.querySelector('nav');
  if(!nav)return;
  const labels={
    en:{members:'Members',dest:'Destinations'},
    es:{members:'Miembros',dest:'Destinos'},
    fr:{members:'Membres',dest:'Destinations'}
  };
  const lang=()=>((document.documentElement.lang||'en').toLowerCase().slice(0,2));
  function syncLabels(){
    const l=labels[lang()]||labels.en;
    [...nav.querySelectorAll('a')].filter(a=>a.getAttribute('href')==='#members').forEach(a=>a.textContent=l.members);
    [...nav.querySelectorAll('a')].filter(a=>a.getAttribute('href')==='#places').forEach(a=>a.textContent=l.dest);
    const mm=document.getElementById('cnvMobileMenu');
    if(mm){
      [...mm.querySelectorAll('a')].filter(a=>a.getAttribute('href')==='#members').forEach(a=>a.textContent=l.members);
      [...mm.querySelectorAll('a')].filter(a=>a.getAttribute('href')==='#places').forEach(a=>a.textContent=l.dest);
    }
  }
  [...nav.querySelectorAll('a')].filter(a=>/members\.html$/i.test(a.getAttribute('href')||'')).forEach(a=>a.remove());
  const members=[...nav.querySelectorAll('a')].filter(a=>a.getAttribute('href')==='#members');
  members.slice(1).forEach(a=>a.remove());

  let actions=document.querySelector('.head-actions');
  let btn=document.getElementById('cnvMenuBtn');
  if(actions && !btn){
    btn=document.createElement('button');
    btn.id='cnvMenuBtn'; btn.type='button'; btn.setAttribute('aria-label','Menu'); btn.setAttribute('aria-expanded','false'); btn.innerHTML='<span></span>';
    actions.appendChild(btn);
  }
  let mm=document.getElementById('cnvMobileMenu');
  if(!mm){ mm=document.createElement('div'); mm.id='cnvMobileMenu'; document.body.appendChild(mm); }
  mm.innerHTML=''; [...nav.querySelectorAll('a')].forEach(a=>mm.appendChild(a.cloneNode(true)));
  if(btn && !btn.dataset.cnvBound){
    btn.dataset.cnvBound='1';
    btn.addEventListener('click',()=>{const o=mm.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false')});
    mm.addEventListener('click',e=>{if(e.target.closest('a')){mm.classList.remove('open');btn.setAttribute('aria-expanded','false')}});
  }

  function reorderLanguages(){
    const controls=[...document.querySelectorAll('button,a')].filter(el=>['EN','ES','FR'].includes((el.textContent||'').trim().toUpperCase()));
    const groups=new Map();
    controls.forEach(el=>{if(el.parentElement){const arr=groups.get(el.parentElement)||[];arr.push(el);groups.set(el.parentElement,arr);}});
    groups.forEach((els,parent)=>{
      const by={}; els.forEach(el=>by[(el.textContent||'').trim().toUpperCase()]=el);
      ['EN','ES','FR'].forEach(k=>{if(by[k])parent.appendChild(by[k]);});
    });
    return controls;
  }
  const controls=reorderLanguages();
  document.documentElement.lang='en';
  const en=controls.find(el=>(el.textContent||'').trim().toUpperCase()==='EN');
  if(en && !sessionStorage.getItem('cnv-default-lang-applied')){
    sessionStorage.setItem('cnv-default-lang-applied','1');
    try{en.click();}catch(e){}
  }
  document.documentElement.lang='en';
  syncLabels();
  new MutationObserver(syncLabels).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''
if '</body>' in s:
    s=s.replace('</body>',runtime+'\n</body>',1)
else:
    s+=runtime

# Validate final structure.
final_nav = re.search(r'<nav\b[^>]*>.*?</nav>', s, flags=re.I|re.S).group(0)
if len(re.findall(r'href=["\']#members["\']', final_nav, flags=re.I)) != 1:
    raise SystemExit('Expected exactly one #members link in main nav')
if re.search(r'href=["\'](?:\./)?members\.html["\']', final_nav, flags=re.I):
    raise SystemExit('Legacy members.html nav link remains')
if not re.search(r'href=["\']#artoflife["\'].*?href=["\']#members["\'].*?href=["\']#places["\']', final_nav, flags=re.I|re.S):
    raise SystemExit('Nav order must be Art of Life -> Members -> Destinations')
member_pos=s.find('<!-- CNV MEMBERS EMBED START -->')
places_pos=s.find('id="places"')
if member_pos < 0 or places_pos < 0 or member_pos > places_pos:
    raise SystemExit('Members section is not immediately before Destinations')
if 'cnv-nav-language-final-20261010' not in s:
    raise SystemExit('Language/navigation controller missing')

index_path.write_text(s, encoding='utf-8')
print('OK: geographic Local prices starred and geographic note shown under cards and tables')
