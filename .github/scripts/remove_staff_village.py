from pathlib import Path
import re
p=Path("index.html")
s=p.read_text(encoding="utf-8")
before=s
patterns=[
(r"8([\\s\\u00a0-]+)micro([\\s\\u00a0-]+)villages",r"7\\1micro\\2villages"),
(r"8([\\s\\u00a0-]+)micro([\\s\\u00a0-]+)pueblos",r"7\\1micro\\2pueblos"),
(r"8([\\s\\u00a0-]+)micro([\\s\\u00a0-]+)aldeas",r"7\\1micro\\2aldeas"),
(r"8([\\s\\u00a0-]+)micro([\\s\\u00a0-]+)villaggi",r"7\\1micro\\2villaggi"),
(r",?\\s*Staff\\s*(?:and|et|y)\\s*Senior",", Senior"),
(r",?\\s*Staff\\s*,\\s*Senior",", Senior"),
(r",?\\s*Senior\\s*(?:and|et|y)\\s*Staff",", Senior"),
(r",?\\s*Senior\\s*,\\s*Staff",", Senior"),
(r",?\\s*Village\\s+du\\s+personnel\\s*(?:et|,)\\s*",", "),
(r",?\\s*Staff Village\\s*(?:and|et|y|,)\\s*",", "),
(r",?\\s*Village Staff\\s*(?:et|y|,)\\s*",", "),
]
for pat,repl in patterns:
 s,n=re.subn(pat,repl,s,flags=re.I)
 if n: print("REPLACED",n,pat)
# Explicitly handle enumeration when Staff is last, without removing legitimate employment references.
s=re.sub(r"(Luxury,\\s*Natural,\\s*Glamping,\\s*Family,\\s*Young,\\s*Free Camp),?\\s*Staff\\s+and\\s+Senior",r"\\1 and Senior",s,flags=re.I)
s=re.sub(r"(Luxury,\\s*Natural,\\s*Glamping,\\s*Family,\\s*Young,\\s*Free Camp),?\\s*Staff\\s+et\\s+Senior",r"\\1 et Senior",s,flags=re.I)
s=re.sub(r"(Luxury,\\s*Natural,\\s*Glamping,\\s*Family,\\s*Young,\\s*Free Camp),?\\s*Staff\\s+y\\s+Senior",r"\\1 y Senior",s,flags=re.I)
if s!=before:
 p.write_text(s,encoding="utf-8")
 print("Updated index.html; changed characters",len(before)-len(s))
else:
 print("No matching source strings in index.html")
for term in ("8 micro-villages","Staff and Senior","Staff et Senior","Staff y Senior"):
 print("REMAINING",term,s.lower().count(term.lower()))
