from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Idempotent cleanup.
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
  function lang(){return (document.documentElement.lang||'en').toLowerCase().slice(0,2)}
  function holder(el){return el&&(el.closest('label,.field,.form-group,.input-group,.control,.form-field')||el)}
  function visibleInputs(form){return [...form.querySelectorAll('input,select,textarea')].filter(el=>el.type!=='hidden')}
  function norm(x){return (x||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'')}
  function makeRow(form,id,a,b){
    if(!a||!b)return;
    a=holder(a); b=holder(b); if(!a||!b||a===b)return;
    let row=form.querySelector('#'+id);
    if(!row){row=document.createElement('div');row.id=id;row.className='cnv-compact-row';a.parentNode.insertBefore(row,a)}
    if(a.parentNode!==row)row.appendChild(a);
    if(b.parentNode!==row)row.appendChild(b);
  }
  function findByHints(form,hints,exclude=[]){
    const els=visibleInputs(form);
    return els.find(el=>{
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
  function preselect(form,sourceText){
    const sel=form.querySelector('select'); if(!sel)return;
    fixMenu(form);
    const keys=matchChoice(sourceText); if(!keys)return;
    const opt=[...sel.options].find(o=>keys.some(k=>norm(o.textContent+' '+o.value).includes(k)));
    if(opt){sel.value=opt.value;sel.selectedIndex=[...sel.options].indexOf(opt);sel.dispatchEvent(new Event('change',{bubbles:true}))}
  }
  function bind(form){
    if(document.documentElement.dataset.cnvJoinBound==='1')return;
    document.documentElement.dataset.cnvJoinBound='1';
    document.addEventListener('click',function(e){
      const heading=[...document.querySelectorAll('h1,h2,h3,p,div,span')].find(el=>{
        const t=(el.textContent||'').trim();
        return t==='Find your place in the CNV adventure.'||t==='Trouvez votre place dans l’aventure CNV.'||t==='Encuentra tu lugar en la aventura CNV.';
      });
      const section=heading&&(heading.closest('section')||heading.parentElement?.parentElement);
      if(!section||!section.contains(e.target))return;
      const card=e.target.closest('a,button,article,.card,[role="button"],[class*="join"],[class*="card"]')||e.target.parentElement;
      const sourceText=card?(card.innerText||card.textContent||''):'';
      if(sourceText) preselect(form,sourceText);
      setTimeout(()=>{fixMenu(form);layout(form);if(sourceText)preselect(form,sourceText)},80);
      setTimeout(()=>{fixMenu(form);layout(form);if(sourceText)preselect(form,sourceText)},250);
    },true);
  }
  function apply(){const form=document.getElementById('cnvContactForm');if(!form)return;fixMenu(form);layout(form);bind(form)}
  apply();
  new MutationObserver(apply).observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</head>' in s:s=s.replace('</head>',style+'\n</head>',1)
else:s=style+'\n'+s
if '</body>' in s:s=s.replace('</body>',runtime+'\n</body>',1)
else:s+=runtime

p.write_text(s,encoding='utf-8')
print('Join form: Patron→Ambassador, Friend of CNV→Friend, click preselection, compact two-column rows')
