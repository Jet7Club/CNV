from pathlib import Path
import re

p = Path('index.html')
html = p.read_text(encoding='utf-8')

m = re.search(r'<form\b[^>]*\bid=["\']cnvContactForm["\'][^>]*>.*?</form>', html, re.S | re.I)
if not m:
    raise SystemExit('cnvContactForm introuvable')

form = m.group(0)
form = re.sub(r'\s+action=(["\'])https://formsubmit\.co/(?:ajax/)?jet7club@proton\.me\1', '', form, flags=re.I)
form = re.sub(r'\s+method=(["\'])post\1', '', form, flags=re.I)
form = re.sub(r'<input\b[^>]*\bname=(["\'])_next\1[^>]*>\s*', '', form, flags=re.I)
html = html[:m.start()] + form + html[m.end():]

html = re.sub(r'<script id="CNV_FORM_AJAX_REDIRECT">.*?</script>\s*', '', html, flags=re.S | re.I)

js = '''<script id="CNV_FORM_AJAX_REDIRECT">
(function(){
  "use strict";
  const ENDPOINT="https://formsubmit.co/ajax/jet7club@proton.me";
  const HOME="https://www.cnvillages.com/";
  document.addEventListener("submit",async function(e){
    const form=e.target;
    if(!form||form.id!=="cnvContactForm") return;
    e.preventDefault();
    e.stopPropagation();
    const button=form.querySelector("#contactSend,button[type='submit'],input[type='submit']");
    if(button) button.disabled=true;
    const payload={};
    for(const [k,v] of new FormData(form).entries()) if(typeof v==="string") payload[k]=v;
    payload._subject=payload._subject||"CNV — Nouveau message";
    payload._template=payload._template||"table";
    payload._captcha="false";
    try{
      const r=await fetch(ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(payload)});
      const data=await r.json().catch(()=>({}));
      if(!r.ok||data.success===false) throw new Error(data.message||("HTTP "+r.status));
      window.location.replace(HOME);
    }catch(err){
      console.error("CNV FormSubmit error",err);
      alert("Envoi impossible. Merci de réessayer.");
      if(button) button.disabled=false;
    }
  },true);
})();
</script>'''

if not re.search(r'</body>', html, re.I):
    raise SystemExit('</body> introuvable')
html = re.sub(r'</body>', js + '\n</body>', html, count=1, flags=re.I)
p.write_text(html, encoding='utf-8')

check = p.read_text(encoding='utf-8')
assert 'https://formsubmit.co/ajax/jet7club@proton.me' in check
assert 'window.location.replace(HOME)' in check
assert check.count('id="CNV_FORM_AJAX_REDIRECT"') == 1
print('OK: AJAX redirect installed')
