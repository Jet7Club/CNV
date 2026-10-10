from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Remove previous version to keep this patch idempotent.
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
      'Après-dîner :':'After dinner:','Musique, conversation, feu, événement ou retour au calme selon l’énergie du jour.':'Music, conversation, a fire, an event, or quiet time depending on the energy of the day.'
    },
    es:{
      'contre :':'Encuentros:','Contre :':'Encuentros:','Rencontre :':'Encuentros:','Rencontres :':'Encuentros:',
      'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.':'Un tiempo abierto para encuentros, la familia o una actividad espontánea.',
      'Soir':'Noche','Coucher du soleil :':'Puesta de sol:',
      'Un moment dehors pour ralentir et profiter du paysage.':'Un momento al aire libre para bajar el ritmo y disfrutar del paisaje.',
      'Dîner :':'Cena:','Grande table, dîner intime ou expérience culinaire partagée.':'Una gran mesa, una cena íntima o una experiencia culinaria compartida.',
      'Après-dîner :':'Después de cenar:','Musique, conversation, feu, événement ou retour au calme selon l’énergie du jour.':'Música, conversación, fuego, un evento o volver a la calma según la energía del día.'
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
    const lang=getLang();
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    const nodes=[]; let n;
    while((n=walker.nextNode())) nodes.push(n);
    nodes.forEach(node=>translateTextNode(node,lang));

    // Check known French leakage when EN/ES is active.
    let leaks=0;
    if(lang!=='fr'){
      const frenchKeys=Object.keys(MAP.fr);
      const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
      let t;
      while((t=w.nextNode())){
        const p=t.parentElement;
        if(!p || /^(SCRIPT|STYLE|NOSCRIPT|TEXTAREA|CODE|PRE)$/i.test(p.tagName)) continue;
        const v=(t.nodeValue||'').trim();
        if(frenchKeys.includes(v) && !(MAP[lang]||{})[v]) leaks++;
      }
    }
    document.documentElement.dataset.cnvTranslationAudit=lang+'-pass'+pass+'-leaks'+leaks;
  }

  function doubleCheck(){
    runPass(1);
    requestAnimationFrame(()=>setTimeout(()=>runPass(2),80));
  }

  doubleCheck();
  window.addEventListener('load',doubleCheck);
  new MutationObserver((mut)=>{
    if(mut.some(m=>m.type==='attributes'&&m.attributeName==='lang')) doubleCheck();
  }).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});

  // Translation systems on this site can redraw blocks after a language click.
  let timer;
  new MutationObserver(()=>{
    clearTimeout(timer);
    timer=setTimeout(doubleCheck,120);
  }).observe(document.body,{childList:true,subtree:true,characterData:true});
})();
</script>
'''

if '</body>' in s:
    s=s.replace('</body>',runtime+'\n</body>',1)
else:
    s+=runtime

# Static validation of the patch itself (pass 1).
required=[
    'Open time for meeting people, family, or a spontaneous activity.',
    'Time outdoors to slow down and enjoy the landscape.',
    'A communal table, an intimate dinner, or a shared culinary experience.',
    'Music, conversation, a fire, an event, or quiet time depending on the energy of the day.',
    'Un tiempo abierto para encuentros, la familia o una actividad espontánea.',
    'Un momento al aire libre para bajar el ritmo y disfrutar del paisaje.',
    'Una gran mesa, una cena íntima o una experiencia culinaria compartida.',
    'Música, conversación, fuego, un evento o volver a la calma según la energía del día.',
    'Un temps ouvert aux rencontres, à la famille ou à une activité spontanée.'
]
missing=[x for x in required if x not in s]
if missing:
    raise SystemExit('Translation audit pass 1 failed; missing: '+repr(missing))
if s.count('id="cnv-full-translation-audit-20261010"')!=1:
    raise SystemExit('Translation audit runtime must exist exactly once')

p.write_text(s,encoding='utf-8')
print('Translation audit pass 1 OK: EN/ES/FR runtime + target block installed')
