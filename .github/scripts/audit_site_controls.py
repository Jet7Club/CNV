from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set(); self.hrefs=[]; self.buttons=[]; self.forms=[]; self.current_form=None
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.add(d['id'])
        if tag=='a' and d.get('href'): self.hrefs.append(d['href'])
        if tag=='button': self.buttons.append(d)
        if tag=='form':
            self.current_form=d
            self.forms.append({'attrs':d,'submit':False})
        if self.current_form and tag in ('button','input'):
            typ=(d.get('type') or '').lower()
            if typ=='submit' or (tag=='button' and typ in ('','submit')):
                self.forms[-1]['submit']=True
    def handle_endtag(self,tag):
        if tag=='form': self.current_form=None


def audit_index(path):
    s=Path(path).read_text(encoding='utf-8')
    p=AuditParser(); p.feed(s)
    errors=[]
    for href in p.hrefs:
        if href.startswith('#') and len(href)>1 and href[1:] not in p.ids:
            errors.append(f'Broken internal link {href}')
    required_ids=['places','members','cnvContactForm']
    for rid in required_ids:
        if rid not in p.ids: errors.append(f'Missing required id #{rid}')
    if not any(f['attrs'].get('id')=='cnvContactForm' for f in p.forms):
        errors.append('CNV contact form missing')
    elif not any(f['attrs'].get('id')=='cnvContactForm' and f['submit'] for f in p.forms):
        errors.append('CNV contact form has no submit control')
    for token in ['EN','ES','FR','Find your place in the CNV adventure.','Trouvez votre place dans l’aventure CNV.','Encuentra tu lugar en la aventura CNV.']:
        if token not in s: errors.append(f'Missing critical text: {token}')
    for token in ['cnv-join-layout-runtime','cnv-full-translation-audit-20261010','cnv-normalize-visible-asterisks']:
        if token not in s: errors.append(f'Missing stability runtime: {token}')
    if 'STYLE,NOSCRIPT' in s: errors.append('Known bad STYLE,NOSCRIPT regex still present')
    if s.count('id="cnv-join-layout-runtime"')!=1: errors.append('Join layout runtime duplicated or missing')
    return errors


def audit_members(path):
    s=Path(path).read_text(encoding='utf-8')
    errors=[]
    for token in ['let lang="en",ed="visionary"','VISIONARY EDITION','VILLAGE EDITION','WEEK EDITION','MONTH EDITION','YEAR EDITION','Annual share of CNV royalties']:
        if token not in s: errors.append(f'Members missing critical token: {token}')
    for fn in ['function L(','function E(','function R(','function C(','function TB(']:
        if fn not in s: errors.append(f'Members missing handler: {fn}')
    if '[q("roy"),...x.map(()=> "✓")' not in s: errors.append('Visionary royalties are not enabled for every level')
    if 'ed==="visionary"?(i===3?"r":i===4?"b":"")' not in s: errors.append('Visionary header colors incorrect')
    if 'ed==="visionary"?(j===4?"r":j===5?"b":"")' not in s: errors.append('Visionary body colors incorrect')
    return errors

errs=audit_index('index.html')+audit_members('members.html')
if errs:
    print('CNV CONTROL AUDIT FAILED')
    for e in errs: print(' -',e)
    sys.exit(1)
print('CNV CONTROL AUDIT OK: internal links, critical buttons, form, languages, Members editions and Visionary table')
