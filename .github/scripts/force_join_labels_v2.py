from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

patterns = {
    'fr': (
        r"join:\['Rejoindre CNV','Trouvez votre place dans l’aventure CNV\.',(?:\['[^']*','[^']*'\],?){6}\]",
        "join:['Rejoindre CNV','Trouvez votre place dans l’aventure CNV.',['01 · Appartenir','Je veux devenir membre'],['02 · Construire','Je veux devenir partenaire'],['03 · Investir','Je veux devenir investisseur'],['04 · Empower','Je veux devenir Patron'],['05 · Soutenir','Je veux devenir ami'],['06 · Contribuer','Je veux être volontaire']]"
    ),
    'en': (
        r"join:\['Join CNV','Find your place in the CNV adventure\.',(?:\['[^']*','[^']*'\],?){6}\]",
        "join:['Join CNV','Find your place in the CNV adventure.',['01 · Belong','I want to become a member'],['02 · Build','I want to become a partner'],['03 · Invest','I want to become an investor'],['04 · Empower','I want to become a Patron'],['05 · Support','I want to become a Friend'],['06 · Contribute','I want to volunteer']]"
    ),
    'es': (
        r"join:\['Únete a CNV','Encuentra tu lugar en la aventura CNV\.',(?:\['[^']*','[^']*'\],?){6}\]",
        "join:['Únete a CNV','Encuentra tu lugar en la aventura CNV.',['01 · Pertenecer','Quiero hacerme miembro'],['02 · Construir','Quiero ser socio'],['03 · Invertir','Quiero ser inversor'],['04 · Empower','Quiero ser Patron'],['05 · Apoyar','Quiero hacerme Amigo'],['06 · Contribuir','Quiero ser voluntario']]"
    )
}

for lang, (pat, repl) in patterns.items():
    s, n = re.subn(pat, repl, s, count=1)
    if n != 1:
        raise SystemExit(f'Could not force {lang} join block; matches={n}')

p.write_text(s, encoding='utf-8')
print('Forced exact FR/EN/ES join labels and order')
