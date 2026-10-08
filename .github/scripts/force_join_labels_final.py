from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

blocks={
'fr': "join:['Rejoindre CNV','Trouvez votre place dans l’aventure CNV.',['01 · Appartenir','Je veux devenir membre'],['02 · Construire','Je veux devenir partenaire'],['03 · Investir','Je veux devenir investisseur'],['04 · Empower','Je veux devenir Ambassadeur'],['05 · Soutenir','Je veux devenir ami'],['06 · Contribuer','Je veux être volontaire']]",
'en': "join:['Join CNV','Find your place in the CNV adventure.',['01 · Belong','I want to become a member'],['02 · Build','I want to become a partner'],['03 · Invest','I want to become an investor'],['04 · Empower','I want to become an Ambassador'],['05 · Support','I want to become a Friend'],['06 · Contribute','I want to volunteer']]",
'es': "join:['Únete a CNV','Encuentra tu lugar en la aventura CNV.',['01 · Pertenecer','Quiero hacerme miembro'],['02 · Construir','Quiero ser socio'],['03 · Invertir','Quiero ser inversor'],['04 · Empower','Quiero ser Embajador'],['05 · Apoyar','Quiero hacerme Amigo'],['06 · Contribuir','Quiero ser voluntario']]"
}
patterns={
'fr': r"join:\['Rejoindre CNV','Trouvez votre place dans l’aventure CNV\.'[^\n]*",
'en': r"join:\['Join CNV','Find your place in the CNV adventure\.'[^\n]*",
'es': r"join:\['Únete a CNV','Encuentra tu lugar en la aventura CNV\.'[^\n]*"
}
for lang in ('fr','en','es'):
    s,n=re.subn(patterns[lang],blocks[lang],s,count=1)
    if n!=1:
        raise SystemExit(f'{lang} join block replacement failed: {n}')

p.write_text(s,encoding='utf-8')
print('Forced final CNV join labels/order in FR EN ES')
