from pathlib import Path

# Rebuild trigger: Visionary royalties + Ambassador red + Investor blue.
p=Path('members.html')
s=p.read_text(encoding='utf-8')

old='[q("roy"),...x.map(()=> "—"),iv[8]]'
new='[q("roy"),...x.map(()=> "✓"),iv[8]]'
if old not in s and new not in s:
    raise SystemExit('Visionary royalties row not found')
s=s.replace(old,new,1)

old_head='${ed!=="visionary"&&i===0?"g":i===4?"r":i===5?"b":""}'
new_head='${ed==="visionary"?(i===3?"r":i===4?"b":""):(i===0?"g":i===4?"r":i===5?"b":"")}'
if old_head not in s and new_head not in s:
    raise SystemExit('Visionary header color logic not found')
s=s.replace(old_head,new_head,1)

old_body='${ed!=="visionary"&&j===1?"g":j===5?"r":j===6?"b":""}'
new_body='${ed==="visionary"?(j===4?"r":j===5?"b":""):(j===1?"g":j===5?"r":j===6?"b":"")}'
if old_body not in s and new_body not in s:
    raise SystemExit('Visionary body color logic not found')
s=s.replace(old_body,new_body,1)

old_card='<li><b>${q("pe")}</b> · ${pl(life.pe[i])}</li></ul></article>`'
new_card='<li><b>${q("pe")}</b> · ${pl(life.pe[i])}</li><li><b>${q("roy")}</b></li></ul></article>`'
if old_card in s:
    s=s.replace(old_card,new_card,1)

checks=[
    '[q("roy"),...x.map(()=> "✓"),iv[8]]',
    'ed==="visionary"?(i===3?"r":i===4?"b":"")',
    'ed==="visionary"?(j===4?"r":j===5?"b":"")'
]
missing=[x for x in checks if x not in s]
if missing:
    raise SystemExit('Visionary checks failed: '+repr(missing))

p.write_text(s,encoding='utf-8')
print('Visionary royalties enabled for every level; Ambassador red; Investor blue')
