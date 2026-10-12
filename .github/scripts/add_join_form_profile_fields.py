from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

m=re.search(r'<form\b[^>]*\bid=["\']cnvContactForm["\'][^>]*>.*?</form>',s,re.S|re.I)
if not m:
    raise SystemExit('cnvContactForm not found')
form=m.group(0)

# Remove previous injected block/runtime/style so this script stays idempotent.
form=re.sub(r'\s*<!-- CNV JOIN EXTRA FIELDS START -->.*?<!-- CNV JOIN EXTRA FIELDS END -->\s*','\n',form,flags=re.S|re.I)
s=s[:m.start()]+form+s[m.end():]
s=re.sub(r'\s*<script id=["\']cnv-join-extra-fields-i18n["\']>.*?</script>\s*','\n',s,flags=re.S|re.I)
s=re.sub(r'\s*<style id=["\']cnv-join-extra-fields-style["\']>.*?</style>\s*','\n',s,flags=re.S|re.I)

m=re.search(r'<form\b[^>]*\bid=["\']cnvContactForm["\'][^>]*>.*?</form>',s,re.S|re.I)
form=m.group(0)

block=r'''
<!-- CNV JOIN EXTRA FIELDS START -->
<div id="cnvJoinExtraFields" class="cnv-join-extra-fields">
  <label>
    <span data-cnv-extra-label="cell">Cell / WhatsApp *</span>
    <input type="tel" name="Cell / WhatsApp" required autocomplete="tel" data-cnv-extra-input="cell" placeholder="Cell / WhatsApp">
  </label>
  <label>
    <span data-cnv-extra-label="linkedin">LinkedIn</span>
    <input type="url" name="LinkedIn" autocomplete="url" data-cnv-extra-input="linkedin" placeholder="https://www.linkedin.com/in/...">
  </label>
  <label>
    <span data-cnv-extra-label="instagram">Instagram</span>
    <input type="text" name="Instagram" data-cnv-extra-input="instagram" placeholder="@instagram">
  </label>
  <label class="cnv-intro-field">
    <span data-cnv-extra-label="intro">Quick introduction *</span>
    <textarea name="Quick introduction" required rows="3" data-cnv-extra-input="intro" placeholder="Tell us briefly who you are and what brings you to CNV..."></textarea>
  </label>
</div>
<!-- CNV JOIN EXTRA FIELDS END -->
'''

submit=re.search(r'<(?:button\b[^>]*\btype=["\']submit["\'][^>]*>|input\b[^>]*\btype=["\']submit["\'][^>]*>)',form,re.I|re.S)
if submit:
    form=form[:submit.start()]+block+'\n'+form[submit.start():]
else:
    form=form.replace('</form>',block+'\n</form>',1)

s=s[:m.start()]+form+s[m.end():]

runtime=r'''
<script id="cnv-join-extra-fields-i18n">
(function(){
  const copy={
    en:{cell:'Cell / WhatsApp *',linkedin:'LinkedIn',instagram:'Instagram',intro:'Quick introduction *',cellPh:'Cell / WhatsApp',linkedinPh:'https://www.linkedin.com/in/...',instagramPh:'@instagram',introPh:'Tell us briefly who you are and what brings you to CNV...'},
    fr:{cell:'Téléphone / WhatsApp *',linkedin:'LinkedIn',instagram:'Instagram',intro:'Présentation rapide *',cellPh:'Téléphone / WhatsApp',linkedinPh:'https://www.linkedin.com/in/...',instagramPh:'@instagram',introPh:'Présentez-vous brièvement et dites-nous ce qui vous amène vers CNV...'},
    es:{cell:'Móvil / WhatsApp *',linkedin:'LinkedIn',instagram:'Instagram',intro:'Presentación breve *',cellPh:'Móvil / WhatsApp',linkedinPh:'https://www.linkedin.com/in/...',instagramPh:'@instagram',introPh:'Cuéntanos brevemente quién eres y qué te acerca a CNV...'}
  };
  function apply(){
    const l=(document.documentElement.lang||'en').toLowerCase().slice(0,2);
    const c=copy[l]||copy.en;
    document.querySelectorAll('[data-cnv-extra-label]').forEach(el=>{const k=el.getAttribute('data-cnv-extra-label');if(c[k])el.textContent=c[k];});
    const cell=document.querySelector('[data-cnv-extra-input="cell"]'); if(cell)cell.placeholder=c.cellPh;
    const li=document.querySelector('[data-cnv-extra-input="linkedin"]'); if(li)li.placeholder=c.linkedinPh;
    const ig=document.querySelector('[data-cnv-extra-input="instagram"]'); if(ig)ig.placeholder=c.instagramPh;
    const intro=document.querySelector('[data-cnv-extra-input="intro"]'); if(intro)intro.placeholder=c.introPh;
  }
  apply();
  new MutationObserver(apply).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''
if '</body>' in s:
    s=s.replace('</body>',runtime+'\n</body>',1)
else:
    s+=runtime

style=r'''
<style id="cnv-join-extra-fields-style">
#cnvContactForm{
  max-height:72vh!important;
  overflow-y:auto!important;
  overflow-x:hidden!important;
  padding-right:12px!important;
  scrollbar-gutter:stable;
  scrollbar-width:auto;
  scrollbar-color:#c7a85b #efe7d7;
}
#cnvContactForm::-webkit-scrollbar{width:12px}
#cnvContactForm::-webkit-scrollbar-track{background:#efe7d7;border-radius:10px}
#cnvContactForm::-webkit-scrollbar-thumb{background:#c7a85b;border-radius:10px;border:2px solid #efe7d7}
#cnvContactForm input,#cnvContactForm select,#cnvContactForm textarea{padding:10px 12px!important}
#cnvContactForm textarea{min-height:78px!important}
#cnvJoinExtraFields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 14px;margin:10px 0 12px}
#cnvJoinExtraFields label{display:flex;flex-direction:column;gap:5px;min-width:0}
#cnvJoinExtraFields .cnv-intro-field{grid-column:1/-1}
#cnvJoinExtraFields input,#cnvJoinExtraFields textarea{width:100%;border-radius:12px;border:1px solid #d9b76255;background:#ffffff08;color:inherit}
#cnvJoinExtraFields textarea{resize:vertical}
#cnvContactForm button[type="submit"],#cnvContactForm input[type="submit"]{position:sticky;bottom:0;z-index:4}
@media(max-width:700px){
  #cnvContactForm{max-height:76vh!important;padding-right:8px!important}
  #cnvJoinExtraFields{grid-template-columns:1fr!important}
  #cnvJoinExtraFields label{grid-column:1/-1!important}
}
</style>
'''
if '</head>' in s:
    s=s.replace('</head>',style+'\n</head>',1)
else:
    s=style+'\n'+s

check=re.search(r'<form\b[^>]*\bid=["\']cnvContactForm["\'][^>]*>.*?</form>',s,re.S|re.I).group(0)
required=['name="Cell / WhatsApp"','name="Quick introduction"','name="LinkedIn"','name="Instagram"','required']
missing=[x for x in required if x not in check]
if missing:
    raise SystemExit('Missing fields: '+repr(missing))
if '#cnvContactForm{' not in s or 'overflow-y:auto' not in s or 'position:sticky' not in s:
    raise SystemExit('Scrollable form safeguards missing')

p.write_text(s,encoding='utf-8')
print('Made CNV join form compact, vertically scrollable, with visible scrollbar and sticky submit')
