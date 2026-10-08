from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

needle = "]]\nmodal:["
count = s.count(needle)
if count != 3:
    raise SystemExit(f'Expected 3 broken join/modal separators, found {count}')

s = s.replace(needle, "]],\nmodal:[", 3)
p.write_text(s, encoding='utf-8')
print('Restored missing commas after FR/EN/ES join blocks')
