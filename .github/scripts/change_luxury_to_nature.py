from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
    'Le luxe sans rigidité.': "L'abondance de la nature.",
    'Luxury without rigidity.': 'Nature in abundance.',
    'El lujo sin rigidez.': 'La abundancia de la naturaleza.',
}

changed = 0
for old, new in replacements.items():
    n = s.count(old)
    if n:
        s = s.replace(old, new)
        changed += n

if not changed:
    print('No matching phrase found; no change made')
    raise SystemExit(0)

p.write_text(s, encoding='utf-8')
print(f'Replaced {changed} occurrence(s) with nature abundance wording')
