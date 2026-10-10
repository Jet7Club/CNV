from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

repls={
    '3 000 € à 8 000 € * *':'3 000 € à 8 000 € *',
    '300 € à 800 € * *':'300 € à 800 € *',
    '3 000 € à 8 000 € **':'3 000 € à 8 000 € *',
    '300 € à 800 € **':'300 € à 800 € *',
    '3 000 € à 8 000 € * * *':'3 000 € à 8 000 € *',
    '300 € à 800 € * * *':'300 € à 800 € *',
}
for old,new in repls.items():
    s=s.replace(old,new)

p.write_text(s,encoding='utf-8')
print('Member prices normalized to a single asterisk')
