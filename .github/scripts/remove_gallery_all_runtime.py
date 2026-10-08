from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='cnv-remove-gallery-all-20261008'

js=r'''<script id="cnv-remove-gallery-all-20261008">
(function(){
  const labels=new Set(['tout','all','todos','todo']);
  const cats=['sanctuaire','spa','permaculture','activités','activites','coworking','restauration','vie nocturne','nightlife'];

  function norm(v){
    return (v||'').trim().toLowerCase();
  }

  function looksLikeGalleryControls(el){
    let node=el.parentElement;
    for(let depth=0; node && depth<5; depth++, node=node.parentElement){
      const txt=norm(node.innerText || node.textContent);
      let hits=0;
      for(const c of cats){ if(txt.includes(c)) hits++; }
      if(hits>=3) return true;
    }
    return false;
  }

  function removeTout(){
    let removed=0;
    const controls=[...document.querySelectorAll('button,a,[role="button"]')];
    for(const el of controls){
      const t=norm(el.textContent);
      const f=norm(el.getAttribute('data-filter')||el.getAttribute('data-cat')||el.getAttribute('data-category'));
      if((labels.has(t)||labels.has(f)) && looksLikeGalleryControls(el)){
        el.remove();
        removed++;
      }
    }
    return removed;
  }

  function run(){
    removeTout();
    setTimeout(removeTout,100);
    setTimeout(removeTout,500);
    setTimeout(removeTout,1500);
  }

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',run,{once:true});
  } else {
    run();
  }

  new MutationObserver(removeTout).observe(document.documentElement,{subtree:true,childList:true});
})();
</script>'''

pat=r'<script id=["\']cnv-remove-gallery-all-20261008["\']>.*?</script>'
if re.search(pat,s,flags=re.S):
    s=re.sub(pat,lambda m: js,s,count=1,flags=re.S)
    print('Replaced existing gallery Tout remover with definitive version')
elif '</body>' in s:
    s=s.replace('</body>',js+'\n</body>',1)
    print('Injected definitive gallery Tout remover')
else:
    s+='\n'+js+'\n'
    print('Appended definitive gallery Tout remover')

p.write_text(s,encoding='utf-8')
