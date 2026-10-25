(function(){
"use strict";
const content={
fr:{title:"Un écosystème complet, pensé à l'échelle humaine.",lead:"Chaque zone a une fonction claire, mais aucune ne fonctionne isolément. Les espaces de vie, de travail, de détente, de nature et de rencontre sont reliés par des parcours doux afin que la journée se déroule sans rupture artificielle."},
en:{title:"A complete ecosystem designed at human scale.",lead:"Each area has a clear purpose, but none works in isolation. Living, working, leisure, nature and social spaces are connected through gentle routes so that the day flows naturally without artificial breaks."},
es:{title:"Un ecosistema completo, diseñado a escala humana.",lead:"Cada zona tiene una función clara, pero ninguna funciona de forma aislada. Los espacios para vivir, trabajar, descansar, disfrutar de la naturaleza y encontrarse están conectados por recorridos suaves para que el día fluya sin rupturas artificiales."}
};
function sync(){
const v=document.getElementById("village");if(!v)return;
const l=(document.documentElement.lang||"fr").slice(0,2);
const t=content[l]||content.fr;
const h=v.querySelector(":scope > h2"),p=v.querySelector(":scope > p.lead");
if(h&&h.textContent!==t.title)h.textContent=t.title;
if(p&&p.textContent!==t.lead)p.textContent=t.lead;
const map=v.querySelector("#cnv-map-embed");
if(map&&p&&p.nextElementSibling!==map)p.insertAdjacentElement("afterend",map);
}
function start(){
sync();
new MutationObserver(sync).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
const v=document.getElementById("village");
if(v)new MutationObserver(sync).observe(v,{childList:true,subtree:true,characterData:true});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",start);else start();
})();