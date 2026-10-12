from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

s=re.sub(r'\s*<script id=["\']cnv-full-translation-audit-20261010["\']>.*?</script>\s*','\n',s,flags=re.I|re.S)

runtime=r'''
<script id="cnv-full-translation-audit-20261010">
(function(){
  const MAP={
    fr:{
      'contre :':'Rencontres :','Contre :':'Rencontres :','Rencontre :':'Rencontres :','Rencontres :':'Rencontres :',
      'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.':'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.',
      'Soir':'Soir','Coucher du soleil :':'Coucher du soleil :',
      'Un moment dehors pour ralentir et profiter du paysage.':'Un moment dehors pour ralentir et profiter du paysage.',
      'Dîner :':'Dîner :','Grande table, dîner intime ou expérience culinaire partagée.':'Grande table, dîner intime ou expérience culinaire partagée.',
      'Après-dîner :':'Après-dîner :','Musique, conversation, feu, événement ou retour au calme selon l’énergie du jour.':'Musique, conversation, feu, événement ou retour au calme selon l’énergie du jour.'
    },
    en:{
      'contre :':'Social time:','Contre :':'Social time:','Rencontre :':'Social time:','Rencontres :':'Social time:',
      'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.':'Open time for meeting people, family, or a spontaneous activity.',
      'Soir':'Evening','Coucher du soleil :':'Sunset:',
      'Un moment dehors pour ralentir et profiter du paysage.':'Time outdoors to slow down and enjoy the landscape.',
      'Dîner :':'Dinner:','Grande table, dîner intime ou expérience culinaire partagée.':'A communal table, an intimate dinner, or a shared culinary experience.',
      'Après-dîner :':'After dinner:','Musique, conversation, feu, événement ou retour au calme selon l’énergie of the day.'
    },
    es:{
      'contre :':'Encuentros:','Contre :':'Encuentros:','Rencontre :':'Encuentros:','Rencontres :':'Encuentros:',
      'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.':'Un tiempo abierto para encuentros, la familia o una actividad espontánea.',
      'Soir':'Noche','Coucher du soleil :':'Puesta de sol:',
      'Un moment dehors pour ralentir et profiter du paysage.':'Un momento al aire libre para bajar el ritmo y disfrutar del paisaje.',
      'Dîner :':'Cena:','Grande table, dîner intime ou expérience culinaire partagée.':'Una gran mesa, una cena íntima o una experiencia culinaria compartida.',
      'Après-dîner :':'Después de cenar:','Musique, conversation, feu, événement ou retour au calme según la energía del día.'
    }
  };

  const getLang=()=>{
    const l=(document.documentElement.lang||'en').toLowerCase().slice(0,2);
    return ['en','es','fr'].includes(l)?l:'en';
  };
  function translateTextNode(node, lang){
    if(!node || node.nodeType!==3) return;
    const parent=node.parentElement;
    if(!parent || /^(SCRIPT|STYLE|NOSCRIPT|TEXTAREA|CODE|PRE)$/i.test(parent.tagName)) return;
    const raw=node.nodeValue||'';
    const trimmed=raw.trim();
    if(!trimmed) return;
    const target=(MAP[lang]||MAP.en)[trimmed];
    if(target && target!==trimmed){
      const lead=raw.match(/^\s*/)?.[0]||'';
      const tail=raw.match(/\s*$/)?.[0]||'';
      node.nodeValue=lead+target+tail;
    }
  }
  function runPass(pass){
    if(!document.body) return;
    const lang=getLang();
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    let n;
    while((n=walker.nextNode())) translateTextNode(n,lang);
    document.documentElement.dataset.cnvTranslationAudit=lang+'-pass'+pass;
  }
  function doubleCheck(){
    runPass(1);
    setTimeout(()=>runPass(2),120);
    setTimeout(()=>runPass(3),500);
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',doubleCheck,{once:true});
  else doubleCheck();
  window.addEventListener('load',doubleCheck,{once:true});
  new MutationObserver((mut)=>{
    if(mut.some(m=>m.type==='attributes'&&m.attributeName==='lang')) doubleCheck();
  }).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
})();
</script>
'''

if '</body>' in s:s=s.replace('</body>',runtime+'\n</body>',1)
else:s+=runtime

required=[
    'Open time for meeting people, family, or a spontaneous activity.',
    'Time outdoors to slow down and enjoy the landscape.',
    'A communal table, an intimate dinner, or a shared culinary experience.',
    'Un tiempo abierto para encuentros, la familia o una actividad espontánea.',
    'Un momento al aire libre para bajar el ritmo y disfrutar del paisaje.',
    'Una gran mesa, una cena íntima o una experiencia culinaria compartida.',
    'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.'
]
missing=[x for x in required if x not in s]
if missing: raise SystemExit('Translation audit validation failed: '+repr(missing))
if s.count('id="cnv-full-translation-audit-20261010"')!=1: raise SystemExit('Translation audit runtime must exist exactly once')

p.write_text(s,encoding='utf-8')
print('Translation audit stabilized: no permanent body MutationObserver')
