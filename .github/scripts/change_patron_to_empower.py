from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
anchor = 'Find your place in the CNV adventure.'
pos = s.find(anchor)
if pos == -1:
    raise SystemExit('Anchor not found')
end = min(len(s), pos + 50000)
chunk = s[pos:end]
old = 'Patron'
idx = chunk.find(old)
if idx == -1:
    print('Patron not found near CNV adventure block; maybe already changed')
    raise SystemExit(0)
chunk = chunk[:idx] + 'Empower' + chunk[idx+len(old):]
s = s[:pos] + chunk + s[end:]
p.write_text(s, encoding='utf-8')
print('Changed card 4 Patron to Empower in CNV adventure block')
