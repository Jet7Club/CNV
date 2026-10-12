from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

s=re.sub(r'\s*<style id=["\']cnv-join-layout-style["\']>.*?</style>\s*','\n',s,flags=re.S|re.I)
s=re.sub(r'\s*<script id=["\']cnv-join-layout-runtime["\']>.*?</script>\s*','\n',s,flags=re.S|re.I)

style=r'''
<style id="cnv-join-layout-style">
#cnvContactForm .cnv-compact-row{
  display:grid!important;
  grid-template-columns:minmax(0,1fr) minmax(0,1fr)!important;
  gap:14px!important;
  align-items:start!important;
  width:100%!important;
  max-width:none!important;
  margin:0 0 14px!important;
  grid-column:1/-1!important;
  flex:0 0 100%!important;
  box-sizing:border-box!important;
}
#cnvContactForm .cnv-compact-row>*{min-width:0!important;width:100%!important;margin:0!important;box-sizing:border-box!important}
#cnvContactForm .cnv-compact-row input,#cnvContactForm .cnv-compact-row label{width:100%!important;max-width:none!important;box-sizing:border-box!important}
#cnvContactForm input,#cnvContactForm select,#cnvContactForm textarea{max-width:100%;box-sizing:border-box}
#cnv-row-contact,#cnv-row-social{grid-column:1/-1!important;width:100%!important}
@media(max-width:700px){#cnvContactForm .cnv-compact-row{grid-template-columns:1fr!important}}
</style>
'''

runtime=r'''
<script id="cnv-join-layout-runtime">
(function(){
  const labels={
    en:{member:'Become a member',partner:'Become a partner',investor:'Become an investor',ambassador:'Become an Ambassador',friend:'Become a Friend',volunteer:'Become a volunteer'},
    fr:{member:'Devenir membre',partner:'Devenir partenaire',investor:'Devenir investisseur',ambassador:'Devenir Ambassadeur',friend:'Devenir Ami',volunteer:'Devenir volontaire'},
    es:{member:'Convertirse en miembro',partner:'Convertirse en socio',investor:'Convertirse en inversor',ambassador:'Convertirse en Embajador',friend:'Convertirse en Amigo',volunteer:'Convertirse en voluntario'}
  };
  const norm=x=>(x||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  const lang=()=>{
    const l=(document.documentElement.lang||'en').toLowerCase().slice(0,2);
    return ['en','fr','es'].includes(l)?l:'en';
  };
  const holder=el=>el&&(el.closest('label,.field,.form-group,.input-group,.control,.form-field')||el);
  const visibleInputs=form=>[...form.querySelectorAll('input,select,textarea')].filter(el=>el.type!=='hidden');

  function semantic(text){
    const t=norm(text);
    if(/ambassador|ambassadeur|embajador|patron|empower/.test(t))return 'ambassador';
    if(/investor|investisseur|inversor|invest/.test(t))return 'investor';
    if(/partner|partenaire|socio|build|construire|construir/.test(t))return 'partner';
    if(/friend|ami|amigo|support|soutenir|apoyar/.test(t))return 'friend';
    if(/volunteer|volontaire|voluntario|contribute|contribuer|contribuir/.test(t))return 'volunteer';
    if(/member|membre|miembro|belong|appartenir|pertenecer/.test(t))return 'member';
    return null;
  }

  function makeRow(form,id,a,b){
    if(!a||!b)return;
    a=holder(a); b=holder(b); if(!a||!b||a===b)return;
    let row=form.querySelector('#'+id);
    if(!row){
      row=document.createElement('div');
      row.id=id; row.className='cnv-compact-row';
      const parent=a.parentNode;
      parent.insertBefore(row,a);
    }
    if(a.parentNode!==row)row.appendChild(a);
    if(b.parentNode!==row)row.appendChild(b);
  }

  function findByHints(form,hints,exclude=[]){
    return visibleInputs(form).find(el=>{
      const hay=norm([el.name,el.id,el.placeholder,el.getAttribute('aria-label')].filter(Boolean).join(' '));
      return hints.some(h=>hay.includes(h))&&!exclude.includes(el);
    });
  }

  function fixMenu(form){
    const sel=form.querySelector('select'); if(!sel)return;
    const l=labels[lang()]||labels.en;
    [...sel.options].forEach(o=>{
      const kind=semantic(o.textContent+' '+o.value);
      if(kind&&l[kind]) o.textContent=l[kind];
    });
  }

  function layout(form){
    const inputs=visibleInputs(form);
    const email=form.querySelector('input[type="email"]')||findByHints(form,['email','mail']);
    const cell=form.querySelector('[data-cnv-extra-input="cell"]')||form.querySelector('input[type="tel"]')||findByHints(form,['telephone','phone','whatsapp','mobile','cell']);
    const linkedin=form.querySelector('[data-cnv-extra-input="linkedin"]')||findByHints(form,['linkedin']);
    const instagram=form.querySelector('[data-cnv-extra-input="instagram"]')||findByHints(form,['instagram']);
    let first=findByHints(form,['prenom','firstname','first-name','first_name','first name']);
    let last=findByHints(form,['nom','lastname','last-name','last_name','surname','last name'],first?[first]:[]);
    if(!first||!last){
      const candidates=inputs.filter(el=>el.tagName==='INPUT'&&['text',''].includes(el.type)&&el!==instagram&&el!==linkedin);
      if(!first)first=candidates[0];
      if(!last)last=candidates.find(el=>el!==first);
    }
    makeRow(form,'cnv-row-name',first,last);
    makeRow(form,'cnv-row-contact',cell,email);
    makeRow(form,'cnv-row-social',linkedin,instagram);
  }

  function preselect(form,kind){
    if(!form||!kind)return;
    const sel=form.querySelector('select'); if(!sel)return;
    fixMenu(form);
    const opt=[...sel.options].find(o=>semantic(o.textContent+' '+o.value)===kind);
    if(opt){
      sel.selectedIndex=[...sel.options].indexOf(opt);
      sel.value=opt.value;
      sel.dispatchEvent(new Event('change',{bubbles:true}));
    }
  }

  function currentForm(){return document.getElementById('cnvContactForm')}
  function joinSection(){
    const headings=[...document.querySelectorAll('h1,h2,h3,h4,p')];
    const h=headings.find(el=>{
      const t=(el.textContent||'').trim();
      return t==='Find your place in the CNV adventure.'||t==='Trouvez votre place dans l’aventure CNV.'||t==='Encuentra tu lugar en la aventura CNV.';
    });
    return h&&(h.closest('section')||h.parentElement?.parentElement||h.parentElement);
  }

  let pendingKind=null;
  document.addEventListener('click',function(e){
    const form=currentForm();
    if(form&&form.contains(e.target)) return;
    const section=joinSection();
    if(!section||!section.contains(e.target)) return;

    let node=e.target;
    let kind=null;
    while(node&&node!==section&&node!==document.body){
      kind=semantic(node.innerText||node.textContent||'');
      if(kind)break;
      node=node.parentElement;
    }
    if(!kind)return;
    pendingKind=kind;
    [0,60,140,260,450,700].forEach(ms=>setTimeout(()=>{
      const f=currentForm();
      if(!f)return;
      fixMenu(f); layout(f); preselect(f,pendingKind);
    },ms));
  },true);

  function apply(){
    const f=currentForm();
    if(!f)return;
    fixMenu(f); layout(f);
    if(pendingKind)preselect(f,pendingKind);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply,{once:true}); else apply();
  window.addEventListener('load',apply,{once:true});
  new MutationObserver(apply).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</head>' in s:s=s.replace('</head>',style+'\n</head>',1)
else:s=style+'\n'+s
if '</body>' in s:s=s.replace('</body>',runtime+'\n</body>',1)
else:s+=runtime

p.write_text(s,encoding='utf-8')
print('Join form fixed: exact two-field rows, scoped card preselection, uniform Become/Devenir/Convertirse labels')
