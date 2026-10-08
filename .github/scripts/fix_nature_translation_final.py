from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = "const pullTitle={fr:'L'abondance de la nature.',en:'L'abondance de la nature.',es:'Lujo sin rigidez.'}[l];"
new = "const pullTitle={fr:\"L'abondance de la nature.\",en:'Nature in abundance.',es:'La abundancia de la naturaleza.'}[l];"
if old not in s:
    raise SystemExit('Expected pullTitle block not found')
s = s.replace(old, new, 1)

old_hack = """  // Fix the known EN mixed-language sentence without disturbing markup.\n  document.querySelectorAll('strong,b,h1,h2,h3,h4,p,div,span').forEach(el=>{\n    if(el.children.length===0 && el.textContent.trim()==='L'abondance de la nature.') el.textContent='Nature in abundance.';\n  });\n"""
if old_hack in s:
    s = s.replace(old_hack, '', 1)

p.write_text(s, encoding='utf-8')
print('Fixed FR/EN/ES nature title translations and removed the forced-English DOM hack')
