from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Idempotent cleanup
s=re.sub(r'\s*<!-- CNV JOIN INTERESTS START -->.*?<!-- CNV JOIN INTERESTS END -->\s*','\n',s,flags=re.S|re.I)
s=re.sub(r'\s*<style id=["\']cnv-join-interests-style["\']>.*?</style>\s*','\n',s,flags=re.S|re.I)
s=re.sub(r'\s*<script id=["\']cnv-join-interests-i18n["\']>.*?</script>\s*','\n',s,flags=re.S|re.I)

m=re.search(r'<form\b[^>]*\bid=["\']cnvContactForm["\'][^>]*>.*?</form>',s,re.S|re.I)
if not m:
    raise SystemExit('cnvContactForm not found')
form=m.group(0)
sel=re.search(r'<select\b[^>]*>.*?</select>',form,re.S|re.I)
if not sel:
    raise SystemExit('Join form select not found')

items=[
('nature','g1','Live closer to nature'),('balance','g1','Find better balance'),('recharge','g1','Recharge regularly'),('months','g1','Stay several months'),
('wellbeing','g2','Improve my wellbeing'),('retreats','g2','Join retreats'),('creativity','g2','Develop my creativity'),
('community','g3','Join a great community'),('inspiring','g3','Meet inspiring people'),('friendships','g3','Build new friendships'),('family','g3','Live with my family'),
('network','g4','Grow my network'),('remote','g4','Work remotely'),('project','g4','Launch a new project'),
('ecology','g5','Support ecology'),('permaculture','g5','Learn permaculture'),('sports','g5','Practice sports activities'),('culture','g5','Practice cultural activities'),
('contribute','g6','Contribute actively to CNV'),('ambassador','g6','Become a CNV ambassador'),('invest','g6','Invest in CNV')
]

groups=[('g1','Nature & lifestyle'),('g2','Wellbeing & creativity'),('g3','Community & relationships'),('g4','Work & projects'),('g5','Ecology & activities'),('g6','Contribution & development')]

parts=['<!-- CNV JOIN INTERESTS START -->','<section id="cnvJoinInterests" class="cnv-join-interests">','  <h3 data-cnv-interest-title>What are you seeking?</h3>','  <div class="cnv-interest-grid">']
for gid,gtitle in groups:
    parts.append(f'    <fieldset class="cnv-interest-group" data-cnv-interest-group="{gid}">')
    parts.append(f'      <legend data-cnv-interest-group-label="{gid}">{gtitle}</legend>')
    for key,kgid,label in items:
        if kgid!=gid: continue
        parts.append(f'      <label class="cnv-interest-item"><input type="checkbox" name="CNV interests" value="{label}" data-cnv-interest-key="{key}"><span data-cnv-interest-label="{key}">{label}</span></label>')
    parts.append('    </fieldset>')
parts += ['  </div>','</section>','<!-- CNV JOIN INTERESTS END -->']
block='\n'.join(parts)
form=form[:sel.end()]+"\n"+block+form[sel.end():]
s=s[:m.start()]+form+s[m.end():]

style=r'''
<style id="cnv-join-interests-style">
#cnvJoinInterests{grid-column:1/-1!important;width:100%!important;margin:12px 0 14px!important;padding:0!important;box-sizing:border-box!important}
#cnvJoinInterests h3{margin:0 0 10px!important;font-size:15px!important;line-height:1.2!important;font-weight:800!important}
#cnvJoinInterests .cnv-interest-grid{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:10px!important;width:100%!important}
#cnvJoinInterests .cnv-interest-group{margin:0!important;padding:10px 12px!important;border:1px solid #d9b76255!important;border-radius:12px!important;min-width:0!important}
#cnvJoinInterests .cnv-interest-group legend{padding:0 5px!important;font-size:11px!important;font-weight:800!important;line-height:1.2!important;text-transform:uppercase!important;letter-spacing:.04em!important}
#cnvJoinInterests .cnv-interest-item{display:flex!important;align-items:flex-start!important;gap:8px!important;margin:6px 0!important;cursor:pointer!important;line-height:1.2!important;font-size:12px!important}
#cnvJoinInterests .cnv-interest-item input{width:16px!important;height:16px!important;min-width:16px!important;margin:0!important;accent-color:#c7a85b!important}
#cnvJoinInterests .cnv-interest-item span{display:block!important;min-width:0!important}
@media(max-width:700px){#cnvJoinInterests .cnv-interest-grid{grid-template-columns:1fr!important}}
</style>
'''

runtime=r'''
<script id="cnv-join-interests-i18n">
(function(){
 const copy={
  en:{title:'What are you seeking?',groups:{g1:'Nature & lifestyle',g2:'Wellbeing & creativity',g3:'Community & relationships',g4:'Work & projects',g5:'Ecology & activities',g6:'Contribution & development'},items:{nature:'Live closer to nature',balance:'Find better balance',recharge:'Recharge regularly',months:'Stay several months',wellbeing:'Improve my wellbeing',retreats:'Join retreats',creativity:'Develop my creativity',community:'Join a great community',inspiring:'Meet inspiring people',friendships:'Build new friendships',family:'Live with my family',network:'Grow my network',remote:'Work remotely',project:'Launch a new project',ecology:'Support ecology',permaculture:'Learn permaculture',sports:'Practice sports activities',culture:'Practice cultural activities',contribute:'Contribute actively to CNV',ambassador:'Become a CNV ambassador',invest:'Invest in CNV'}},
  fr:{title:'Que recherchez-vous chez CNV ?',groups:{g1:'Nature & qualité de vie',g2:'Bien-être & créativité',g3:'Communauté & relations',g4:'Travail & projets',g5:'Écologie & activités',g6:'Contribution & développement'},items:{nature:'Vivre proche de la nature',balance:'Retrouver un meilleur équilibre',recharge:'Me ressourcer régulièrement',months:'Séjourner plusieurs mois',wellbeing:'Améliorer mon bien-être',retreats:'Participer à des retraites',creativity:'Développer ma créativité',community:'Rejoindre une belle communauté',inspiring:'Rencontrer des personnes inspirantes',friendships:'Créer de nouvelles amitiés',family:'Vivre avec ma famille',network:'Développer mon réseau',remote:'Travailler à distance',project:'Lancer un nouveau projet',ecology:'Participer à l’écologie',permaculture:'Apprendre la permaculture',sports:'Pratiquer des activités sportives',culture:'Pratiquer des activités culturelles',contribute:'Contribuer activement à CNV',ambassador:'Devenir ambassadeur CNV',invest:'Investir dans CNV'}},
  es:{title:'¿Qué buscas en CNV?',groups:{g1:'Naturaleza & calidad de vida',g2:'Bienestar & creatividad',g3:'Comunidad & relaciones',g4:'Trabajo & proyectos',g5:'Ecología & actividades',g6:'Contribución & desarrollo'},items:{nature:'Vivir cerca de la naturaleza',balance:'Encontrar mejor equilibrio',recharge:'Recargarme regularmente',months:'Quedarme varios meses',wellbeing:'Mejorar mi bienestar',retreats:'Participar en retiros',creativity:'Desarrollar mi creatividad',community:'Unirme a una comunidad',inspiring:'Conocer personas inspiradoras',friendships:'Crear nuevas amistades',family:'Vivir con mi familia',network:'Desarrollar mi red',remote:'Trabajar a distancia',project:'Lanzar un nuevo proyecto',ecology:'Participar en ecología',permaculture:'Aprender permacultura',sports:'Practicar actividades deportivas',culture:'Practicar actividades culturales',contribute:'Contribuir activamente a CNV',ambassador:'Ser embajador CNV',invest:'Invertir en CNV'}}
 };
 function apply(){
  const l=(document.documentElement.lang||'en').toLowerCase().slice(0,2); const c=copy[l]||copy.en;
  const title=document.querySelector('[data-cnv-interest-title]'); if(title)title.textContent=c.title;
  document.querySelectorAll('[data-cnv-interest-group-label]').forEach(el=>{const k=el.dataset.cnvInterestGroupLabel;if(c.groups[k])el.textContent=c.groups[k]});
  document.querySelectorAll('[data-cnv-interest-label]').forEach(el=>{const k=el.dataset.cnvInterestLabel;if(c.items[k])el.textContent=c.items[k]});
  document.querySelectorAll('[data-cnv-interest-key]').forEach(el=>{const k=el.dataset.cnvInterestKey;if(c.items[k])el.value=c.items[k]});
 }
 apply();
 new MutationObserver(apply).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</head>' in s:s=s.replace('</head>',style+'\n</head>',1)
else:s=style+'\n'+s
if '</body>' in s:s=s.replace('</body>',runtime+'\n</body>',1)
else:s+=runtime

if s.count('id="cnvJoinInterests"')!=1: raise SystemExit('Interest block missing or duplicated')
if 'Pratiquer des activités sportives' not in s or 'Pratiquer des activités culturelles' not in s: raise SystemExit('Required activity choices missing')
if '>Autre<' in s: raise SystemExit('Unexpected Other option in interest block')

p.write_text(s,encoding='utf-8')
print('Added 21 grouped CNV interest checkboxes after Become/Devenir select in EN FR ES')
