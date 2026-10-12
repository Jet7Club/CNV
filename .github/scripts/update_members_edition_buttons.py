from pathlib import Path
import re

p=Path('members.html')
s=p.read_text(encoding='utf-8')

new_m='''const M={visionary:{fr:["ÉDITION VISIONNAIRE","10 000 cartes à vie à émettre","Sur invitation uniquement"],en:["VISIONARY EDITION","10,000 lifetime cards to be issued","Invitation only"],es:["EDICIÓN VISIONARIA","10.000 tarjetas de por vida por emitir","Solo por invitación"]},life:{fr:["ÉDITION VILLAGE","5 000 cartes à vie pour chaque village","Sur invitation uniquement"],en:["VILLAGE EDITION","5,000 lifetime cards for each village","Invitation only"],es:["EDICIÓN VILLAGE","5.000 tarjetas de por vida para cada pueblo","Solo por invitación"]},week:{fr:["ÉDITION SEMAINE ANNUELLE","Quota annuel limité"],en:["ANNUAL WEEK EDITION","Limited annual quota"],es:["EDICIÓN SEMANA ANUAL","Cupo anual limitado"]},month:{fr:["ÉDITION MOIS ANNUELLE","Quota annuel limité"],en:["ANNUAL MONTH EDITION","Limited annual quota"],es:["EDICIÓN MES ANUAL","Cupo anual limitado"]},year:{fr:["ÉDITION ANNÉE ANNUELLE","Quota annuel limité"],en:["ANNUAL YEAR EDITION","Limited annual quota"],es:["EDICIÓN AÑO ANUAL","Cupo anual limitado"]}};'''

s,n=re.subn(r'const M=\{visionary:.*?\};',new_m,s,count=1,flags=re.S)
if n!=1:
    raise SystemExit('Edition labels block not found')

s=s.replace('let lang="en",ed="life";','let lang="en",ed="visionary";',1)
s=s.replace('let lang="fr",ed="life";','let lang="fr",ed="visionary";',1)
s=s.replace("let lang='en',ed='life';","let lang='en',ed='visionary';",1)
s=s.replace("let lang='fr',ed='life';","let lang='fr',ed='visionary';",1)

required=[
'VISIONARY EDITION','10,000 lifetime cards to be issued','Invitation only',
'VILLAGE EDITION','5,000 lifetime cards for each village',
'ANNUAL WEEK EDITION','ANNUAL MONTH EDITION','ANNUAL YEAR EDITION',
'ÉDITION VISIONNAIRE','ÉDITION VILLAGE','ÉDITION SEMAINE ANNUELLE','ÉDITION MOIS ANNUELLE','ÉDITION ANNÉE ANNUELLE',
'EDICIÓN VISIONARIA','EDICIÓN VILLAGE','EDICIÓN SEMANA ANUAL','EDICIÓN MES ANUAL','EDICIÓN AÑO ANUAL',
'Quota annuel limité','Limited annual quota','Cupo anual limitado'
]
missing=[x for x in required if x not in s]
if missing:
    raise SystemExit('Missing translated labels: '+repr(missing))
if 'ed="visionary"' not in s and "ed='visionary'" not in s:
    raise SystemExit('Visionary is not the default edition')

p.write_text(s,encoding='utf-8')
print('Updated Members edition buttons in EN/ES/FR and set Visionary default')
