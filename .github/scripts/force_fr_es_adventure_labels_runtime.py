from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='cnv-fr-es-adventure-labels-runtime-20261008'
if marker in s:
    print('already patched')
    raise SystemExit(0)

js=r'''
<script id="cnv-fr-es-adventure-labels-runtime-20261008">
(function(){
  const labels={
    fr:['Appartenir','Construire','Investir','Empower','Soutenir','Contribuer'],
    es:['Pertenecer','Construir','Invertir','Empower','Apoyar','Contribuir'],
    en:['Belong','Build','Invest','Empower','Support','Contribute']
  };
  function lang(){return (document.documentElement.lang||'en').toLowerCase().slice(0,2)}
  function apply(){
    const l=labels[lang()]||labels.en;
    const heading=[...document.querySelectorAll('h1,h2,h3,p,div,span')].find(el=>{
      const t=(el.textContent||'').trim();
      return t==='Find your place in the CNV adventure.'||t==='Trouvez votre place dans l’aventure CNV.'||t==='Encuentra tu lugar en la aventura CNV.';
    });
    if(!heading)return;
    const section=heading.closest('section')||heading.parentElement?.parentElement||document;
    const candidates=[...section.querySelectorAll('h3,strong,b')].filter(el=>/^\s*0?[1-6]\s*[·.-]?\s*/.test((el.textContent||'').trim()));
    if(candidates.length>=6){
      candidates.slice(0,6).forEach((el,i)=>{el.textContent=String(i+1).padStart(2,'0')+' · '+l[i]});
      return;
    }
    const all=[...section.querySelectorAll('*')].filter(el=>{
      const t=(el.textContent||'').trim();
      return /^(0?[1-6]\s*[·.-]?\s*)?(Belong|Build|Invest|Empower|Support|Contribute|Appartenir|Construire|Investir|Soutenir|Contribuer|Pertenecer|Construir|Invertir|Apoyar|Contribuir)$/i.test(t);
    });
    all.slice(0,6).forEach((el,i)=>{el.textContent=String(i+1).padStart(2,'0')+' · '+l[i]});
  }
  apply();
  new MutationObserver(apply).observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</body>' in s:
    s=s.replace('</body>',js+'\n</body>',1)
else:
    s+=js
p.write_text(s,encoding='utf-8')
print('Injected runtime enforcement for FR/ES/EN adventure labels')
