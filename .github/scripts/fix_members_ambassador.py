from pathlib import Path
p=Path('members.html')
s=p.read_text(encoding='utf-8')
old='const N={fr:["Local","Duo","Famille","Social","Patron"],en:["Local","Duo","Family","Social","Patron"],es:["Local","Dúo","Familia","Social","Patron"]};'
new='const N={fr:["Local","Duo","Famille","Social","Ambassadeur"],en:["Local","Duo","Family","Social","Ambassador"],es:["Local","Dúo","Familia","Social","Embajador"]};'
if old not in s:
    raise SystemExit('Expected members label block not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('Updated members page: Patron -> Ambassadeur/Ambassador/Embajador')
