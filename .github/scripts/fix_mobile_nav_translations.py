from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

marker='cnv-mobile-nav-fix-20261008'
if marker in s:
    print('already patched')
    raise SystemExit(0)

css=r'''
<style id="cnv-mobile-nav-fix-20261008">
#cnvMenuBtn{display:none;width:42px;height:42px;border:1px solid rgba(255,255,255,.35);border-radius:12px;background:rgba(5,27,22,.68);color:#fff;align-items:center;justify-content:center;cursor:pointer;padding:0}
#cnvMenuBtn span,#cnvMenuBtn span:before,#cnvMenuBtn span:after{display:block;width:20px;height:2px;background:#fff;border-radius:2px;content:"";position:relative}
#cnvMenuBtn span:before{position:absolute;top:-6px;left:0}#cnvMenuBtn span:after{position:absolute;top:6px;left:0}
#cnvMobileMenu{display:none;position:fixed;z-index:90;top:82px;left:0;right:0;background:rgba(5,27,22,.98);backdrop-filter:blur(18px);padding:18px 22px 24px;border-top:1px solid rgba(255,255,255,.12);box-shadow:0 18px 40px rgba(0,0,0,.28)}
#cnvMobileMenu.open{display:block}#cnvMobileMenu a{display:block;color:#fff;text-decoration:none;text-transform:uppercase;letter-spacing:.12em;font-size:13px;padding:13px 4px;border-bottom:1px solid rgba(255,255,255,.10)}#cnvMobileMenu a:hover{color:#e0c58f}
@media(max-width:980px){#cnvMenuBtn{display:flex!important}.head-actions{gap:8px}.top>nav{display:none!important}}
</style>
'''

js=r'''
<script id="cnv-mobile-nav-script-20261008">
(function(){
  const nav=document.querySelector('.top nav')||document.querySelector('nav');
  if(!nav)return;
  let art=[...nav.querySelectorAll('a')].find(a=>a.getAttribute('href')==='#artoflife');
  let members=[...nav.querySelectorAll('a')].find(a=>/members\.html$/i.test(a.getAttribute('href')||''));
  if(!members && art){
    members=document.createElement('a');
    members.href='members.html';
    members.id='membersNavLink';
    members.textContent='Members';
    art.insertAdjacentElement('afterend',members);
  }

  const labels={
    en:{members:'Members',dest:'Destinations'},
    fr:{members:'Membres',dest:'Destinations'},
    es:{members:'Miembros',dest:'Destinos'}
  };
  function lang(){return (document.documentElement.lang||'en').toLowerCase().slice(0,2)}
  function syncLabels(){
    const l=labels[lang()]||labels.en;
    const m=[...nav.querySelectorAll('a')].find(a=>/members\.html$/i.test(a.getAttribute('href')||''));
    if(m)m.textContent=l.members;
    const d=[...nav.querySelectorAll('a')].find(a=>a.getAttribute('href')==='#places');
    if(d)d.textContent=l.dest;
    const mm=document.getElementById('cnvMobileMenu');
    if(mm){
      const md=[...mm.querySelectorAll('a')].find(a=>a.getAttribute('href')==='#places'); if(md)md.textContent=l.dest;
      const mmem=[...mm.querySelectorAll('a')].find(a=>/members\.html$/i.test(a.getAttribute('href')||'')); if(mmem)mmem.textContent=l.members;
    }
  }

  let actions=document.querySelector('.head-actions');
  if(actions && !document.getElementById('cnvMenuBtn')){
    const b=document.createElement('button'); b.id='cnvMenuBtn'; b.type='button'; b.setAttribute('aria-label','Menu'); b.setAttribute('aria-expanded','false'); b.innerHTML='<span></span>'; actions.appendChild(b);
    const menu=document.createElement('div'); menu.id='cnvMobileMenu';
    [...nav.querySelectorAll('a')].forEach(a=>menu.appendChild(a.cloneNode(true)));
    document.body.appendChild(menu);
    b.addEventListener('click',()=>{const o=menu.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false')});
    menu.addEventListener('click',e=>{if(e.target.closest('a')){menu.classList.remove('open');b.setAttribute('aria-expanded','false')}});
  }

  // Fix the known EN mixed-language sentence without disturbing markup.
  document.querySelectorAll('strong,b,h1,h2,h3,h4,p,div,span').forEach(el=>{
    if(el.children.length===0 && el.textContent.trim()==='Le luxe sans rigidité.') el.textContent='Luxury without rigidity.';
  });
  syncLabels();
  new MutationObserver(syncLabels).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</head>' in s:
    s=s.replace('</head>',css+'\n</head>',1)
else:
    s=css+s
if '</body>' in s:
    s=s.replace('</body>',js+'\n</body>',1)
else:
    s+=js
p.write_text(s,encoding='utf-8')
print('patched index.html: mobile menu + Members + ES Destinos + EN luxury sentence')
