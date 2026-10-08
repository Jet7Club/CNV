from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

repls = {
    "['04 · Empower','Je veux devenir Ambassadeur']": "['04 · Valoriser','Je veux devenir Ambassadeur']",
    "['04 · Empower','Quiero ser Embajador']": "['04 · Potenciar','Quiero ser Embajador']",
    "fr:['Appartenir','Construire','Investir','Empower','Soutenir','Contribuer']": "fr:['Appartenir','Construire','Investir','Valoriser','Soutenir','Contribuer']",
    "es:['Pertenecer','Construir','Invertir','Empower','Apoyar','Contribuir']": "es:['Pertenecer','Construir','Invertir','Potenciar','Apoyar','Contribuir']",
}

changed = 0
for old,new in repls.items():
    if old in s:
        s = s.replace(old,new)
        changed += 1

if changed == 0:
    raise SystemExit('No Empower FR/ES labels found to translate')

p.write_text(s, encoding='utf-8')
print(f'Updated {changed} FR/ES Empower label occurrence(s)')
