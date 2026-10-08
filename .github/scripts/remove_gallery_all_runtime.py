from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
marker='cnv-remove-gallery-all-20261008'
if marker in s:
    print('already patched')
    raise SystemExit(0)

js=r'''
<script id="cnv-remove-gallery-all-20261008">
(function(){
  const titles=[
    "Des images pour ressentir l’atmosphère",
    "Des images pour ressentir l'atmosphère",
    "Images to feel the atmosphere",
    "Imágenes para sentir la atmósfera"
  ];
  const labels=new Set(['tout','all','todos','todo']);
  function removeAllButton(){
    const heading=[...document.querySelectorAll('h1,h2,h3,h4,p,div,span')].find(el=>titles.includes((el.textContent||'').trim()));
    if(!heading)return false;
    const section=heading.closest('section')||heading.parentElement?.parentElement||document;
    const controls=[...section.querySelectorAll('button,a,[role="button"]')];
    for(const el of controls){
      const t=(el.textContent||'').trim().toLowerCase();
      const f=(el.getAttribute('data-filter')||el.getAttribute('data-cat')||el.getAttribute('data-category')||'').trim().toLowerCase();
      if(labels.has(t)||['all','tout','todos','todo'].includes(f)){
        el.remove();
        return true;
      }
    }
    return false;
  }
  removeAllButton();
  const obs=new MutationObserver(()=>removeAllButton());
  obs.observe(document.documentElement,{subtree:true,childList:true});
})();
</script>
'''

if '</body>' in s:
    s=s.replace('</body>',js+'\n</body>',1)
else:
    s+=js
p.write_text(s,encoding='utf-8')
print('Injected gallery All/Tout button remover')
