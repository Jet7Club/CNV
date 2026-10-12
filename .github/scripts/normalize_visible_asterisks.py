from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Remove previous runtime patch so this remains idempotent.
s=re.sub(r'\s*<script id=["\']cnv-normalize-visible-asterisks["\']>.*?</script>\s*','\n',s,flags=re.I|re.S)

runtime=r'''
<script id="cnv-normalize-visible-asterisks">
(function(){
  function normalize(){
    if(!document.body) return;
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    let n;
    while((n=walker.nextNode())){
      const p=n.parentElement;
      if(!p || /^(SCRIPT|STYLE|NOSCRIPT|TEXTAREA|CODE|PRE)$/i.test(p.tagName)) continue;
      if((n.nodeValue||'').includes('**')) n.nodeValue=n.nodeValue.replace(/\*\*/g,'*');
    }
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',normalize,{once:true});
  else normalize();
  window.addEventListener('load',normalize,{once:true});
})();
</script>
'''

if '</body>' in s:
    s=s.replace('</body>',runtime+'\n</body>',1)
else:
    s+=runtime

p.write_text(s,encoding='utf-8')
print('Visible double asterisks normalized safely without permanent DOM scanning')
