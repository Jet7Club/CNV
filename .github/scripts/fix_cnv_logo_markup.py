from pathlib import Path
import re
p=Path("index.html")
s=p.read_text(encoding="utf-8")
old='src="assets/LOGO%20CNV.png"/ decoding="async"'
new='src="assets/LOGO%20CNV.png" decoding="async"'
if old in s:
    s=s.replace(old,new)
else:
    s=re.sub(r'(src="assets/LOGO%20CNV\.png")\s*/\s*(decoding="async")',r'\1 \2',s)
if 'id="cnv-charter-link"' not in s:
    raise SystemExit("Charter button missing: refusing to proceed")
p.write_text(s,encoding="utf-8")
print("CNV header logo HTML corrected")
