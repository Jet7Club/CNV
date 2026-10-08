from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
    # EN visible legacy order -> requested order
    '02 · Contribute': '02 · Build',
    '03 · Support': '03 · Invest',
    '05 · Build': '05 · Support',
    '06 · Invest': '06 · Contribute',
    # FR visible legacy order -> requested order
    '02 · Contribuer': '02 · Construire',
    '03 · Soutenir': '03 · Investir',
    '05 · Construire': '05 · Soutenir',
    '06 · Investir': '06 · Contribuer',
    # ES visible legacy order -> requested order
    '02 · Contribuir': '02 · Construir',
    '03 · Apoyar': '03 · Invertir',
    '05 · Construir': '05 · Apoyar',
    '06 · Invertir': '06 · Contribuir',
}

changed = 0
for old, new in replacements.items():
    n = s.count(old)
    if n:
        s = s.replace(old, new)
        changed += n

# Also enforce the exact translation data blocks if present.
exact = {
    "join:['Rejoindre CNV','Trouvez votre place dans l’aventure CNV.": "fr",
    "join:['Join CNV','Find your place in the CNV adventure.": "en",
    "join:['Únete a CNV','Encuentra tu lugar en la aventura CNV.": "es",
}

expected = {
'fr': "join:['Rejoindre CNV','Trouvez votre place dans l’aventure CNV.',['01 · Appartenir','Je veux devenir membre'],['02 · Construire','Je veux devenir partenaire'],['03 · Investir','Je veux devenir investisseur'],['04 · Empower','Je veux devenir Ambassadeur'],['05 · Soutenir','Je veux devenir ami'],['06 · Contribuer','Je veux être volontaire']],",
'en': "join:['Join CNV','Find your place in the CNV adventure.',['01 · Belong','I want to become a member'],['02 · Build','I want to become a partner'],['03 · Invest','I want to become an investor'],['04 · Empower','I want to become an Ambassador'],['05 · Support','I want to become a Friend'],['06 · Contribute','I want to volunteer']],",
'es': "join:['Únete a CNV','Encuentra tu lugar en la aventura CNV.',['01 · Pertenecer','Quiero hacerme miembro'],['02 · Construir','Quiero ser socio'],['03 · Invertir','Quiero ser inversor'],['04 · Empower','Quiero ser Embajador'],['05 · Apoyar','Quiero hacerme Amigo'],['06 · Contribuir','Quiero ser voluntario']],",
}

lines = s.splitlines(True)
for i, line in enumerate(lines):
    for prefix, lang in exact.items():
        if prefix in line:
            nl = '\n' if line.endswith('\n') else ''
            if line.rstrip('\n') != expected[lang]:
                lines[i] = expected[lang] + nl
                changed += 1
            break
s = ''.join(lines)

if changed == 0:
    print('No changes needed; visible labels and translation blocks already exact')
else:
    p.write_text(s, encoding='utf-8')
    print(f'Applied {changed} visible/order correction(s)')
