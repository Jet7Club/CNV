from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')
repls={
"['04 · Empower','Je veux devenir Patron']":"['04 · Empower','Je veux devenir Ambassadeur']",
"['04 · Empower','I want to become a Patron']":"['04 · Empower','I want to become an Ambassador']",
"['04 · Empower','Quiero ser Patron']":"['04 · Empower','Quiero ser Embajador']",
}
changed=0
for old,new in repls.items():
    n=s.count(old)
    if n:
        s=s.replace(old,new)
        changed+=n
if changed<3:
    raise SystemExit(f'Expected at least 3 replacements, got {changed}')
p.write_text(s,encoding='utf-8')
print(f'Updated Empower subtitles to Ambassador equivalents in {changed} occurrence(s)')
