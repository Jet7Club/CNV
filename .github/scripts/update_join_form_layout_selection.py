from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

s=re.sub(r'\s*<style id=["\']cnv-join-layout-style["\']>.*?</style>\s*','\n',s,flags=re.S|re.I)
s=re.sub(r'\s*<script id=["\']cnv-join-layout-runtime["\']>.*?</script>\s*','\n',s,flags=re.S|re.I)

style=r'''
<style id="cnv-join-layout-style">
#cnvContactForm .cnv-compact-row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start;width:100%;margin:0 0 14px}
#cnvContactForm .cnv-compact-row>*{min-width:0;width:100%!important;margin:0!important}
#cnvContactForm .cnv-compact-row input,#cnvContactForm .cnv-compact-row label{width:100%!important}
#cnvContactForm input,#cnvContactForm select,#cnvContactForm textarea{max-width:100%}
@media(max-width:700px){#cnvContactForm .cnv-compact-row{grid-template-columns:1fr}}
</style>
'''

runtime=r'''
<script id="cnv-join-layout-runtime">
(function(){
  const labels={
    en:{amb:'Ambassador',friend:'Friend'},
    fr:{amb:'Ambassadeur',friend:'Ami'},
    es:{amb:'Embajador',friend:'Amigo'}
  };
  const norm=x=>(x||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  const lang=()=>{
    const l=(document.documentElement.lang||'en').toLowerCase().slice(0,2);
    return ['en','fr','es'].includes(l)?l:'en';
  };
  const holder=el=>el&&(el.closest('label,.field,.form-group,.input-group,.control,.form-field')||el);
  const visibleInputs=form=>[...form.querySelectorAll('input,select,textarea')].filter(el=>el.type!=='hidden');

  function makeRow(form,id,a,b){
    if(!a||!b)return;
    a=holder(a); b=holder(b); if(!a||!b||a===b)return;
    let row=form.querySelector('#'+id);
    if(!row){row=document.createElement('div');row.id=id;row.className='cnv-compact-row';a.parentNode.insertBefore(row,a)}
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
    const l=labels[lang()]||labels.en;
    const sel=form.querySelector('select'); if(!sel)return;
    [...sel.options].forEach(o=>{
      const t=norm(o.textContent+' '+o.value);
      if(t.includes('patron')||t.includes('patran')||t.includes('ambassador')||t.includes('ambassadeur')||t.includes('embajador')){
        o.textContent=l.amb;
        if(t.includes('patron')||t.includes('patran')) o.value=l.amb;
      }
      if(t.includes('ami de cnv')||t.includes('friend of cnv')||t.includes('amigo de cnv')||t==='ami'||t==='friend'||t==='amigo'){
        o.textContent=l.friend;
        if(t.includes(' de cnv')||t.includes(' of cnv')) o.value=l.friend;
      }
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
  function matchChoice(text){
    const t=norm(text);
    if(/ambassador|ambassadeur|embajador|patron|empower/.test(t))return ['ambassador','ambassadeur','embajador'];
    if(/investor|investisseur|inversor|invest/.test(t))return ['investor','investisseur','inversor'];
    if(/partner|partenaire|socio|build|construire|construir/.test(t))return ['partner','partenaire','socio'];
    if(/friend|ami|amigo|support|soutenir|apoyar/.test(t))return ['friend','ami','amigo'];
    if(/volunteer|volontaire|voluntario|contribute|contribuer|contribuir/.test(t))return ['volunteer','volontaire','voluntario'];
    if(/member|membre|miembro|belong|appartenir|pertenecer/.test(t))return ['member','membre','miembro'];
    return null;
  }
  function preselect(form,keys){
    if(!keys)return;
    const sel=form.querySelector('select'); if(!sel)return;
    fixMenu(form);
    const opt=[...sel.options].find(o=>keys.some(k=>norm(o.textContent+' '+o.value).includes(k)));
    if(opt){sel.value=opt.value;sel.dispatchEvent(new Event('change',{bubbles:true}))}
  }
  function apply(form,keys){
    if(!form)return;
    fixMenu(form); layout(form); preselect(form,keys);
  }
  function currentForm(){return document.getElementById('cnvContactForm')}

  document.addEventListener('click',function(e){
    const card=e.target.closest('a,button,article,.card,[role="button"],[class*="join"],[class*="card"]')||e.target.parentElement;
    const keys=card?matchChoice(card.innerText||card.textContent||''):null;
    [0,80,220,500].forEach(ms=>setTimeout(()=>apply(currentForm(),keys),ms));
  },true);

  function onReady(){apply(currentForm(),null)}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',onReady,{once:true}); else onReady();
  window.addEventListener('load',onReady,{once:true});
  new MutationObserver(()=>apply(currentForm(),null)).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</head>' in s:s=s.replace('</head>',style+'\n</head>',1)
else:s=style+'\n'+s
if '</body>' in s:s=s.replace('</body>',runtime+'\n</body>',1)
else:s+=runtime

p.write_text(s,encoding='utf-8')
print('Join form stabilized: compact rows, menu labels, click preselection, no subtree observer')
