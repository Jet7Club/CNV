from pathlib import Path
p=Path("index.html")
s=p.read_text(encoding="utf-8")
marker="cnv-personalized-day.js"
if marker not in s:
    snippet='\n<link rel="stylesheet" href="assets/cnv-personalized-day.css">\n<script defer src="assets/cnv-personalized-day.js"></script>\n'
    if "</head>" in s: s=s.replace("</head>",snippet+"</head>",1)
    elif "</body>" in s: s=s.replace("</body>",snippet+"</body>",1)
    else: raise SystemExit("Missing HTML insertion point")
    p.write_text(s,encoding="utf-8")
    print("CNV personalized day integrated")
else: print("Already integrated")
