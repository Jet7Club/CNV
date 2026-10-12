from pathlib import Path
import re

p=Path('members.html')
s=p.read_text(encoding='utf-8')

new_m='''const M={visionary:{fr:["ÉDITION VISIONNAIRE","10 000 cartes à vie à émettre","Sur invitation uniquement"],en:["VISIONARY EDITION","10,000 lifetime cards to be issued","Invitation only"],es:["EDICIÓN VISIONARIA","10.000 tarjetas de por vida por emitir","Solo por invitación"]},life:{fr:["ÉDITION VILLAGE","5 000 cartes à vie pour chaque village","Sur invitation uniquement"],en:["VILLAGE EDITION","5,000 lifetime cards for each village","Invitation only"],es:["EDICIÓN VILLAGE","5.000 tarjetas de por vida para cada pueblo","Solo por invitación"]},week:{fr:["ÉDITION SEMAINE","Cartes annuelles","Quota annuel limité"],en:["WEEK EDITION","Annual cards","Limited annual quota"],es:["EDICIÓN SEMANA","Tarjetas anuales","Cupo anual limitado"]},month:{fr:["ÉDITION MOIS","Cartes annuelles","Quota annuel limité"],en:["MONTH EDITION","Annual cards","Limited annual quota"],es:["EDICIÓN MES","Tarjetas anuales","Cupo anual limitado"]},year:{fr:["ÉDITION ANNÉE","Cartes annuelles","Quota annuel limité"],en:["YEAR EDITION","Annual cards","Limited annual quota"],es:["EDICIÓN AÑO","Tarjetas anuales","Cupo anual limitado"]}};'''

s,n=re.subn(r'const M=\{visionary:.*?\};',new_m,s,count=1,flags=re.S)
if n!=1:
    raise SystemExit('Edition labels block not found')

s=s.replace('let lang="en",ed="life";','let lang="en",ed="visionary";',1)
s=s.replace('let lang="fr",ed="life";','let lang="fr",ed="visionary";',1)
s=s.replace("let lang='en',ed='life';","let lang='en',ed='visionary';",1)
s=s.replace("let lang='fr',ed='life';","let lang='fr',ed='visionary';",1)

# Add green slow-blinking annual quota badge style.
if '.annual-quota{' not in s:
    s=s.replace('.invite-line{display:block;', '.annual-quota{display:block;margin-top:8px;padding:6px 10px;border-radius:999px;background:linear-gradient(160deg,#174d2e,#0d2d1b);border:1px solid #57d282cc;color:#eaffef;font-size:11px;font-weight:800;line-height:1.25;animation:aq 7.5s ease-in-out infinite}@keyframes aq{0%,100%{opacity:1}50%{opacity:.5}}.invite-line{display:block;',1)

# Render annual quota badge for week/month/year while preserving red invitation badge for visionary/life.
old='''eds.innerHTML=["visionary","life","week","month","year"].map(k=>{const m=M[k][lang];return `<button class="${ed===k?"on":""}" onclick="E('${k}')"><strong>${m[0]}</strong><small>${m[1]}</small>${(k==="visionary"||k==="life")?`<span class=invite-line>${m[2]}</span>`:""}</button>`}).join("");'''
new='''eds.innerHTML=["visionary","life","week","month","year"].map(k=>{const m=M[k][lang];const badge=(k==="visionary"||k==="life")?`<span class=invite-line>${m[2]}</span>`:(k==="week"||k==="month"||k==="year")?`<span class=annual-quota>${m[2]}</span>`:"";return `<button class="${ed===k?"on":""}" onclick="E('${k}')"><strong>${m[0]}</strong><small>${m[1]}</small>${badge}</button>`}).join("");'''
if old in s:
    s=s.replace(old,new,1)
elif 'class=annual-quota' not in s:
    raise SystemExit('Edition button rendering block not found')

required=[
'VISIONARY EDITION','10,000 lifetime cards to be issued','Invitation only',
'VILLAGE EDITION','5,000 lifetime cards for each village',
'WEEK EDITION','MONTH EDITION','YEAR EDITION','Annual cards','Limited annual quota',
'ÉDITION VISIONNAIRE','ÉDITION VILLAGE','ÉDITION SEMAINE','ÉDITION MOIS','ÉDITION ANNÉE','Cartes annuelles','Quota annuel limité',
'EDICIÓN VISIONARIA','EDICIÓN VILLAGE','EDICIÓN SEMANA','EDICIÓN MES','EDICIÓN AÑO','Tarjetas anuales','Cupo anual limitado',
'annual-quota'
]
missing=[x for x in required if x not in s]
if missing:
    raise SystemExit('Missing translated labels/styles: '+repr(missing))
if 'ed="visionary"' not in s and "ed='visionary'" not in s:
    raise SystemExit('Visionary is not the default edition')

p.write_text(s,encoding='utf-8')
print('Updated annual edition buttons EN/ES/FR with slow green quota badges')
