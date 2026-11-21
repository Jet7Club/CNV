(function(){
"use strict";
const zones={
en:[
["Housing & Micro-Villages","Nature, Young, Free Camp and Owner Village, which includes Senior Village."],
["Spa & Wellness","Thermal circuit, pools, hot tubs, massages, yoga, Tai Chi, Qi Gong and Zen gardens."],
["Sport & Culture","Tree-top adventures, mountain biking, sports, art workshops, theatre, music and outdoor cinema."],
["Work & Collaboration","Coworking, Business Club, incubator, networking, conferences and AI training."],
["Permaculture","Food forest, organic gardens, composting, rainwater harvesting, food processing and preservation, and a permaculture school."],
["Dining & Gastronomy","Restaurants, communal dining, guest chefs, cooking workshops and farmers' markets."],
["Natural Sanctuary","Biodiversity, protected forest, quiet spaces, nature trails and wildlife watching."],
["Nightlife & Entertainment","DJs, concerts, festivals, two dance floors, bars and lounges, with acoustic management."]
],
es:[
["Alojamientos y microaldeas","Nature, Young, Free Camp y Owner Village, que incluye Senior Village."],
["Spa y bienestar","Circuito termal, piscinas, jacuzzis, masajes, yoga, Tai Chi, Qi Gong y jardines zen."],
["Deporte y cultura","Circuitos de aventura en árboles, bicicleta de montaña, deportes, talleres artísticos, teatro, música y cine al aire libre."],
["Trabajo y colaboración","Espacios de trabajo compartido, club empresarial, incubadora, contactos profesionales, conferencias y formación en IA."],
["Permacultura","Bosque comestible, huertos ecológicos, compostaje, captación de lluvia, transformación y conservación de cosechas y escuela de permacultura."],
["Gastronomía y restauración","Restaurantes, mesas compartidas, chefs invitados, talleres de cocina y mercados de productores."],
["Santuario natural","Biodiversidad, bosque protegido, silencio, senderos naturales y observación de fauna."],
["Ocio nocturno y entretenimiento","DJ, conciertos, festivales, dos pistas de baile, bares y salones, con control acústico."]
],
fr:[
["Hébergement et micro-villages","Nature, Young, Free Camp et Owner Village, qui intègre Senior Village."],
["Spa et bien-être","Parcours thermal, bassins, massages, yoga, tai-chi, qi gong et jardins zen."],
["Sport et culture","Accrobranche, VTT, sports, ateliers artistiques, théâtre, musique et cinéma en plein air."],
["Travail et collaboration","Espaces de travail partagés, club d’affaires, incubateur, conférences et formations en IA."],
["Agriculture et permaculture","Forêt nourricière, potagers bio, compostage, récupération d’eau et école de permaculture."],
["Restauration et gastronomie","Restaurants, grandes tablées, chefs invités, ateliers culinaires et marchés de producteurs."],
["Sanctuaire naturel","Biodiversité, forêt protégée, silence, sentiers et observation de la faune."],
["Vie nocturne","DJ, concerts, festivals, pistes de danse, bars et salons, avec maîtrise acoustique."]
]
};
const coords=[[18,51],[64,23],[76,36],[39,49],[42,19],[53,43],[18,15],[85,65]];
const translations={fr:{title:"Carte interactive",subtitle:"Explorez les 8 zones et leurs principaux équipements",zone:"ZONE SÉLECTIONNÉE",note:"Implantation conceptuelle : les emplacements ne représentent pas un plan géographique définitif.",area:"Superficie"},en:{title:"Interactive map",subtitle:"Explore the 8 zones and their main facilities",zone:"SELECTED ZONE",note:"Conceptual layout: positions are not a final geographic plan.",area:"Area"},es:{title:"Mapa interactivo",subtitle:"Explora las 8 zonas y sus principales instalaciones",zone:"ZONA SELECCIONADA",note:"Distribución conceptual: las posiciones no son un plano geográfico definitivo.",area:"Superficie"}};
const zoneTypes=["housing","wellness","activities","business","agriculture","lifestyle","nature","entertainment"];
const typeColors={nature:"#62cf81",agriculture:"#b2d76e",wellness:"#bd91ed",lifestyle:"#f2b46c",activities:"#f4d35e",business:"#73c9f2",entertainment:"#ee79a6",housing:"#f49a74"};
function lang(){let v=(document.documentElement.lang||"fr").slice(0,2);return translations[v]?v:"fr";}
function el(tag,cls,txt){const n=document.createElement(tag);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n;}
function removeStaffVillage(){const scopes=[document.getElementById("village"),document.getElementById("housing"),document.querySelector('[id*="micro-village"]')].filter(Boolean);for(const scope of scopes){for(const node of scope.querySelectorAll("h2,h3,h4,h5,.card-title,.village-title")){if(!/^staff(?:\s+village)?$|^village\s+(?:du\s+)?personnel$|^staff\s+micro.village$/i.test((node.textContent||"").trim()))continue;const card=node.closest("article,.card,.village-card,.housing-card,li");if(card&&!card.contains(document.getElementById("cnv-zone-map-v2")))card.remove();else node.remove();}}}
function mount(){
if(document.getElementById("cnv-zone-map-v2"))return;
const target=document.getElementById("cnv-map-embed")||document.getElementById("village")||document.querySelector('[id*="village"]')||document.querySelector('a[href="#village"]')?.closest("section")||document.querySelector("main");if(!target)return;
const style=el("style");style.textContent=`
#village > .master{display:none!important}#cnv-zone-map-v2{background:#082e25;color:#f7f5ed;padding:clamp(18px,3vw,36px);border-radius:28px;margin:30px auto;max-width:1250px;font-family:inherit}
#cnv-zone-map-v2 .cz-title{font:normal clamp(27px,3vw,42px) Georgia,serif;color:#eac982;margin:0 0 8px}
#cnv-zone-map-v2 .cz-sub{color:#d4e3d9;margin:0 0 20px}
#cnv-zone-map-v2 .cz-layout{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(260px,1fr);gap:24px}
#cnv-zone-map-v2 .cz-map{position:relative;aspect-ratio:1.15;background:radial-gradient(ellipse at 44% 48%,#37654b,#124938 62%,#092e25);border-radius:22px;overflow:hidden}
#cnv-zone-map-v2 .cz-map svg{position:absolute;inset:0;width:100%;height:100%}
#cnv-zone-map-v2 .cz-pin{position:absolute;transform:translate(-50%,-50%);width:27px;height:27px;border-radius:50%;background:var(--zone-color,#205844);border:2px solid #fff;color:#082e25;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:bold;cursor:pointer;padding:0}
#cnv-zone-map-v2 .cz-pin[aria-pressed="true"]{background:#e7c77d;color:#10382b;border:3px solid white;z-index:3;scale:1.18}
#cnv-zone-map-v2 .cz-label{position:absolute;transform:translate(-50%,-150%);font-size:10px;color:#fff;text-shadow:0 1px 4px #061c15;white-space:nowrap;pointer-events:none}
#cnv-zone-map-v2 .cz-detail{background:#0d382d;border-radius:20px;padding:22px}
#cnv-zone-map-v2 .cz-eyebrow{font-size:11px;letter-spacing:.15em;color:#eac982}
#cnv-zone-map-v2 .cz-name{font:normal clamp(25px,2.6vw,36px) Georgia,serif;color:#eac982;margin:12px 0}
#cnv-zone-map-v2 .cz-desc{line-height:1.7;color:#e4eee8}
#cnv-zone-map-v2 .cz-controls{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:7px;margin-top:18px}
#cnv-zone-map-v2 .cz-controls button{background:var(--zone-color,#1b503e);border:1px solid #fff;color:#082e25;font-weight:700;border-radius:9px;padding:9px 3px;cursor:pointer}
#cnv-zone-map-v2 .cz-controls button[aria-pressed="true"]{background:#e7c77d;color:#15382c}
#cnv-zone-map-v2 .cz-legend{display:flex;flex-wrap:wrap;gap:10px 16px;margin:12px 0 22px}#cnv-zone-map-v2 .cz-legend-item{display:inline-flex;align-items:center;gap:6px;font-size:12px;color:#eef5ed}#cnv-zone-map-v2 .cz-legend-dot{width:12px;height:12px;border-radius:50%;border:1px solid #fff;display:inline-block}#cnv-zone-map-v2 .cz-note{color:#c6d9cb;font-size:12px;margin:15px 0 0}
@media(max-width:760px){#cnv-zone-map-v2 .cz-layout{grid-template-columns:1fr}#cnv-zone-map-v2 .cz-map{aspect-ratio:1.1}#cnv-zone-map-v2 .cz-label{display:none}#cnv-zone-map-v2 .cz-controls{grid-template-columns:repeat(4,1fr)}}
`;document.head.append(style);
const root=el("section");root.id="cnv-zone-map-v2";
const heading=el("h2","cz-title"),sub=el("p","cz-sub"),layout=el("div","cz-layout"),map=el("div","cz-map"),detail=el("div","cz-detail"),eyebrow=el("div","cz-eyebrow"),name=el("h3","cz-name"),desc=el("p","cz-desc"),controls=el("div","cz-controls"),note=el("p","cz-note");
const ns="http://www.w3.org/2000/svg",svg=document.createElementNS(ns,"svg");svg.setAttribute("viewBox","0 0 700 540");for(const radius of [60,115,170,225,280,335,390,445,500]){const c=document.createElementNS(ns,"circle");for(const [k,v] of Object.entries({cx:350,cy:270,r:radius,fill:"none",stroke:"#b6d1bb","stroke-opacity":".15"}))c.setAttribute(k,v);svg.append(c);}map.append(svg);
let current=0;const pins=[],buttons=[];
function select(i){current=i;const l=lang(),t=translations[l],zone=zones[l][i];eyebrow.textContent=t.zone+" · "+(i+1)+" / "+coords.length;name.textContent=zone[0];desc.textContent=zone[1];pins.forEach((p,j)=>p.setAttribute("aria-pressed",String(i===j)));buttons.forEach((p,j)=>p.setAttribute("aria-pressed",String(i===j)));}
for(let i=0;i<coords.length;i++){const pin=el("button","cz-pin",String(i+1));pin.style.setProperty("--zone-color",typeColors[zoneTypes[i]]);pin.type="button";pin.title=(i+1)+". "+zones[lang()][i][0];pin.style.left=coords[i][0]+"%";pin.style.top=coords[i][1]+"%";pin.addEventListener("click",()=>select(i));map.append(pin);pins.push(pin);const b=el("button","",String(i+1));b.type="button";b.style.setProperty("--zone-color",typeColors[zoneTypes[i]]);b.title=zones[lang()][i][0];b.setAttribute("aria-label",(i+1)+". "+zones[lang()][i][0]);b.addEventListener("click",()=>select(i));controls.append(b);buttons.push(b);}
function localize(){const l=lang(),t=translations[l];heading.textContent=t.title;sub.textContent=t.subtitle;note.textContent=t.note;pins.forEach((p,i)=>{p.title=(i+1)+". "+zones[l][i][0];});buttons.forEach((b,i)=>{const n=(i+1)+". "+zones[l][i][0];b.title=n;b.setAttribute("aria-label",n);});select(current);}
detail.append(eyebrow,name,desc,controls);layout.append(map,detail);root.append(heading,sub,layout,note);
const legend=el("div","cz-legend");const labels={fr:{nature:"Nature",agriculture:"Agriculture",wellness:"Bien-être",lifestyle:"Gastronomie",activities:"Activités",business:"Professionnel",entertainment:"Divertissement",housing:"Hébergements"},en:{nature:"Nature",agriculture:"Agriculture",wellness:"Wellness",lifestyle:"Dining",activities:"Activities",business:"Business",entertainment:"Entertainment",housing:"Housing"},es:{nature:"Naturaleza",agriculture:"Agricultura",wellness:"Bienestar",lifestyle:"Gastronomía",activities:"Actividades",business:"Negocios",entertainment:"Entretenimiento",housing:"Alojamientos"}};for(const [type,color] of Object.entries(typeColors)){const item=el("span","cz-legend-item");const dot=el("i","cz-legend-dot");dot.style.background=color;item.append(dot,el("span","cz-legend-text",labels.fr[type]));item.dataset.type=type;legend.append(item);}root.insertBefore(legend,layout);const oldLocalize=localize;localize=function(){oldLocalize();for(const item of legend.children)item.querySelector(".cz-legend-text").textContent=labels[lang()][item.dataset.type];};const village=document.getElementById("village");if(village){for(const oldMap of village.querySelectorAll(":scope > .master"))oldMap.remove();}target.prepend(root);localize();removeStaffVillage();
if(location.hash==="#village"){requestAnimationFrame(()=>root.scrollIntoView({block:"start",behavior:"instant"}));}
new MutationObserver(localize).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",mount);else mount();window.addEventListener("load",mount,{once:true});
})();