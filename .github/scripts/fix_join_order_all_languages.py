from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
"join:['Rejoindre CNV','Trouvez votre place dans l’aventure CNV.',['01 · Appartenir','Je veux devenir membre'],['02 · Contribuer','Je veux être volontaire'],['03 · Soutenir','Je veux devenir ami'],['04 · Patron','Je veux devenir Patron'],['05 · Construire','Je veux devenir partenaire'],['06 · Investir','Je veux devenir investisseur']]":
"join:['Rejoindre CNV','Trouvez votre place dans l’aventure CNV.',['01 · Appartenir','Je veux devenir membre'],['02 · Construire','Je veux devenir partenaire'],['03 · Investir','Je veux devenir investisseur'],['04 · Empower','Je veux devenir Patron'],['05 · Soutenir','Je veux devenir ami'],['06 · Contribuer','Je veux être volontaire']]",

"join:['Join CNV','Find your place in the CNV adventure.',['01 · Belong','I want to become a member'],['02 · Contribute','I want to volunteer'],['03 · Support','I want to become a Friend'],['04 · Empower','I want to become a Patron'],['05 · Build','I want to become a partner'],['06 · Invest','I want to become an investor']]":
"join:['Join CNV','Find your place in the CNV adventure.',['01 · Belong','I want to become a member'],['02 · Build','I want to become a partner'],['03 · Invest','I want to become an investor'],['04 · Empower','I want to become a Patron'],['05 · Support','I want to become a Friend'],['06 · Contribute','I want to volunteer']]",

"join:['Únete a CNV','Encuentra tu lugar en la aventura CNV.',['01 · Pertenecer','Quiero hacerme miembro'],['02 · Contribuir','Quiero ser voluntario'],['03 · Apoyar','Quiero hacerme Amigo'],['04 · Patron','Quiero ser Patron'],['05 · Construir','Quiero ser socio'],['06 · Invertir','Quiero ser inversor']]":
"join:['Únete a CNV','Encuentra tu lugar en la aventura CNV.',['01 · Pertenecer','Quiero hacerme miembro'],['02 · Construir','Quiero ser socio'],['03 · Invertir','Quiero ser inversor'],['04 · Empower','Quiero ser Patron'],['05 · Apoyar','Quiero hacerme Amigo'],['06 · Contribuir','Quiero ser voluntario']]"
}

changed = 0
for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new, 1)
        changed += 1

if changed != 3:
    raise SystemExit(f'Expected 3 language blocks, changed {changed}')

p.write_text(s, encoding='utf-8')
print('Updated CNV join card order in FR/EN/ES')
