from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Remove previous version so this stays idempotent.
s = re.sub(r'\s*<script id=["\']cnv-members-language-sync["\']>.*?</script>\s*', '\n', s, flags=re.I|re.S)

script = r'''
<script id="cnv-members-language-sync">
(function(){
  const frame=document.getElementById('cnvMembersFrame');
  if(!frame)return;
  function currentLang(){
    return (document.documentElement.lang||'en').toLowerCase().slice(0,2);
  }
  function syncMembersLanguage(){
    const l=currentLang();
    if(!['en','es','fr'].includes(l))return;
    try{
      const w=frame.contentWindow;
      if(w && typeof w.L==='function') w.L(l,null);
    }catch(e){}
  }
  frame.addEventListener('load',syncMembersLanguage);
  new MutationObserver(syncMembersLanguage).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
  syncMembersLanguage();
})();
</script>
'''

if '</body>' in s:
    s = s.replace('</body>', script + '\n</body>', 1)
else:
    s += script

p.write_text(s, encoding='utf-8')
print('OK: Members language synced with main site EN/ES/FR')
