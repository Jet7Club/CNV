from pathlib import Path
import re
p=Path("index.html")
s=p.read_text(encoding="utf-8")
assets=Path("assets")
logo=assets/"logo-cnv-2026.png"
docs={"fr":assets/"reglement-interieur-fr.pdf","en":assets/"community-charter-en.pdf","es":assets/"reglamento-interno-es.pdf"}
missing=[str(x) for x in [logo,*docs.values()] if not x.is_file()]
if missing:
    raise SystemExit("Missing assets, refusing incomplete deployment: "+", ".join(missing))
if 'id="cnv-charter-link"' not in s:
    match=re.search(r'(<section\\b[^>]*\\bid=["\\\']artoflife["\\\'][^>]*>)(.*?)(</section>)',s,re.I|re.S)
    if not match: raise SystemExit("Art of Life section not found")
    block='''<div class="cnv-charter-cta" style="text-align:center;padding:28px 16px"><a id="cnv-charter-link" href="assets/reglement-interieur-fr.pdf" target="_blank" rel="noopener noreferrer" style="display:inline-block;background:#174b35;color:#fff;border:1px solid #cba455;border-radius:999px;padding:14px 28px;text-decoration:none;font-weight:700">Règlement intérieur ↗</a></div>'''
    s=s[:match.end(2)]+block+s[match.end(2):]
if 'id="cnv-charter-runtime"' not in s:
    runtime='''<script id="cnv-charter-runtime">(function(){
const map={fr:["Règlement intérieur","assets/reglement-interieur-fr.pdf"],en:["Community Charter","assets/community-charter-en.pdf"],es:["Reglamento interno","assets/reglamento-interno-es.pdf"]};
function sync(){const a=document.getElementById("cnv-charter-link");if(!a)return;
const lang=(document.documentElement.lang||localStorage.getItem("lang")||"fr").toLowerCase().slice(0,2);
const item=map[lang]||map.fr;a.textContent=item[0]+" ↗";a.href=item[1];}
document.addEventListener("DOMContentLoaded",sync);new MutationObserver(sync).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});window.addEventListener("storage",sync);
})();</script>'''
    s=s.replace("</body>",runtime+"</body>")
# Replace existing header logo image only when recognizable.
header=re.search(r'<header\\b[^>]*>.*?</header>',s,re.I|re.S)
if header:
    h=header.group(0)
    im=re.search(r'<img\\b[^>]*(?:class=["\\\'][^"\\\']*logo|alt=["\\\'][^"\\\']*(?:CNV|Chill Natural))[^>]*>',h,re.I|re.S)
    if im:
        tag=im.group(0)
        if re.search(r'\\bsrc=["\\\'][^"\\\']*["\\\']',tag):
            new=re.sub(r'\\bsrc=["\\\'][^"\\\']*["\\\']','src="assets/logo-cnv-2026.png"',tag,count=1)
            s=s[:header.start()]+h.replace(tag,new,1)+s[header.end():]
p.write_text(s,encoding="utf-8")
print("CNV logo and trilingual charter link integrated")
