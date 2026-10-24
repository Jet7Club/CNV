from pathlib import Path
import re
p=Path("index.html")
s=p.read_text(encoding="utf-8")
assets=Path("assets")
logo=assets/"LOGO CNV.png"
docs={"fr":assets/"CNV_Reglement_Interieur_Premium_FR_Sans_Signature.pdf","en":assets/"CNV_Community_Charter_Premium_EN_No_Signature.pdf","es":assets/"CNV_Reglamento_Interno_Premium_ES_Sin_Firma.pdf"}
missing=[str(x) for x in [logo,*docs.values()] if not x.is_file()]
if missing: raise SystemExit("Missing files: "+", ".join(missing))
if 'id="cnv-charter-link"' not in s:
    m=re.search(r'(<section\b[^>]*\bid=["\']artoflife["\'][^>]*>)(.*?)(</section>)',s,re.I|re.S)
    if not m: raise SystemExit("Art de vivre section not found")
    button='<div class="cnv-charter-cta" style="text-align:center;padding:28px 16px"><a id="cnv-charter-link" href="assets/CNV_Reglement_Interieur_Premium_FR_Sans_Signature.pdf" target="_blank" rel="noopener noreferrer" style="display:inline-block;background:#174b35;color:#fff;border:1px solid #cba455;border-radius:999px;padding:14px 28px;text-decoration:none;font-weight:700">Règlement intérieur ↗</a></div>'
    s=s[:m.end(2)]+button+s[m.end(2):]
if 'id="cnv-charter-runtime"' not in s:
    js='''<script id="cnv-charter-runtime">(function(){
const map={fr:["Règlement intérieur","assets/CNV_Reglement_Interieur_Premium_FR_Sans_Signature.pdf"],en:["Community Charter","assets/CNV_Community_Charter_Premium_EN_No_Signature.pdf"],es:["Reglamento interno","assets/CNV_Reglamento_Interno_Premium_ES_Sin_Firma.pdf"]};
function sync(){const a=document.getElementById("cnv-charter-link");if(!a)return;
const lang=(document.documentElement.lang||localStorage.getItem("lang")||"fr").toLowerCase().slice(0,2);
const item=map[lang]||map.fr;a.textContent=item[0]+" ↗";a.href=item[1];}
document.addEventListener("DOMContentLoaded",sync);new MutationObserver(sync).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});window.addEventListener("storage",sync);
})();</script>'''
    s=s.replace("</body>",js+"</body>")
header=re.search(r'<header\b[^>]*>.*?</header>',s,re.I|re.S)
if header:
    h=header.group()
    im=re.search(r'<img\b[^>]*(?:class=["\'][^"\']*logo|alt=["\'][^"\']*(?:CNV|Chill Natural))[^>]*>',h,re.I|re.S)
    if im:
        tag=im.group()
        new=re.sub(r'\bsrc=["\'][^"\']*["\']','src="assets/LOGO%20CNV.png"',tag,count=1)
        s=s[:header.start()]+h.replace(tag,new,1)+s[header.end():]
p.write_text(s,encoding="utf-8")
print("CNV charter and logo integrated")
