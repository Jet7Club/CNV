(function(){
"use strict";
const zones=[
["Sanctuaire naturel","300 ha","Biodiversité, forêt protégée, silence, sentiers naturels et observation de la faune."],
["Permaculture","50 ha","Forêt nourricière, potagers bio, compostage, récupération d’eau, transformation et conservation des récoltes, école de permaculture."],
["Spa & Wellness","3 ha","Parcours thermal, bassins, jacuzzis, massages, yoga, Tai Chi, Qi Gong et jardins zen."],
["Dining & Gastronomy","2 ha","Restaurants, grandes tablées, chefs invités, ateliers culinaires et marchés de producteurs."],
["Activities & Experiences","5 ha","Accrobranche, VTT, sports, ateliers artistiques, théâtre, musique et cinéma en plein air."],
["Pro Hub & Coworking","1 ha","Coworking, Business Club, incubateur, networking, conférences et formations IA."],
["Nightlife & Entertainment","2 ha","DJ, concerts, festivals, deux pistes de danse, bars et lounges, avec maîtrise acoustique."],
["Housing & Micro-Villages","100 ha","Camp libre, hébergements nature, Young, Family, Senior, Glamping et Suites prestiges."],
["Logistique & réserve","À définir","Stocks alimentaires, réserve stratégique, entrepôts et banque de semences."],
["Eau & assainissement","À définir","Captage, potabilisation, stockage, traitement et réutilisation des eaux."],
["Énergie","À définir","Solaire, batteries, autonomie et gestion intelligente."],
["Mobilité","À définir","Navettes électriques, vélos, parking photovoltaïque et héliport."],
["Sécurité & santé","À définir","Centre médical 24/7, ambulance, pharmacie et secours."],
["Gestion des déchets","À définir","Tri, compostage, recyclage et valorisation des déchets."],
["Numérique","À définir","Wi-Fi, cybersécurité et communications d’urgence."],
["Administration","À définir","Accueil, conciergerie, réservations et gestion des membres."],
["Maintenance","À définir","Ateliers, réparation, entretien et réemploi."],
["Paysages & biodiversité","À définir","Grands arbres, corridors écologiques et jardins naturels."],
["Éducation & culture","À définir","Formations, ateliers, conférences et transmission des savoir-faire."],
["RH & bénévolat","À définir","Équipes, bénévoles, formation et coordination."],
["Agriculture complémentaire","À définir","Production locale et diversification agricole."],
["Événements","À définir","Amphithéâtre, esplanades et rassemblements culturels."],
["Tourisme","À définir","Excursions, découvertes locales et tourisme responsable."],
["Commerces & services","À définir","Boutiques, marchés, coiffure, blanchisserie et services."],
["Architecture écologique","À définir","Matériaux naturels, bioclimatisme et intégration paysagère."],
["Autonomie & résilience","À définir","Réserves d’eau, sécurité hydrique et sobriété."]
];
const coords=[[18,15],[42,19],[64,23],[53,43],[76,36],[39,49],[85,65],[18,51],[55,76],[29,82],[14,77],[74,86],[67,54],[43,87],[28,61],[54,61],[66,79],[12,35],[42,33],[40,70],[28,28],[78,49],[12,62],[53,29],[29,44],[84,18]];
const translations={fr:{title:"Carte interactive des 26 zones",subtitle:"Explorez les zones et leurs principaux équipements",zone:"ZONE SÉLECTIONNÉE",note:"Implantation conceptuelle : les emplacements ne représentent pas un plan géographique définitif.",area:"Superficie"},en:{title:"Interactive map of 26 zones",subtitle:"Explore each zone and its main facilities",zone:"SELECTED ZONE",note:"Conceptual layout: positions are not a final geographic plan.",area:"Area"},es:{title:"Mapa interactivo de 26 zonas",subtitle:"Explora las zonas y sus principales instalaciones",zone:"ZONA SELECCIONADA",note:"Distribución conceptual: las posiciones no son un plano geográfico definitivo.",area:"Superficie"}};
const zoneTypes=["nature","agriculture","wellness","lifestyle","activities","business","entertainment","housing","infrastructure","infrastructure","infrastructure","infrastructure","services","infrastructure","infrastructure","services","infrastructure","nature","services","services","agriculture","activities","activities","services","infrastructure","infrastructure"];
const typeColors={nature:"#62cf81",agriculture:"#b2d76e",wellness:"#bd91ed",lifestyle:"#f2b46c",activities:"#f4d35e",business:"#73c9f2",entertainment:"#ee79a6",housing:"#f49a74",infrastructure:"#9ab1c6",services:"#63d7c7"};
function lang(){let v=(document.documentElement.lang||"fr").slice(0,2);return translations[v]?v:"fr";}
function el(tag,cls,txt){const n=document.createElement(tag);if(cls)n.className=cls;if(txt!==undefined)n.textContent=txt;return n;}
function removeStaffVillage(){const scopes=[document.getElementById("village"),document.getElementById("housing"),document.querySelector('[id*="micro-village"]')].filter(Boolean);for(const scope of scopes){for(const node of scope.querySelectorAll("h2,h3,h4,h5,.card-title,.village-title")){if(!/^staff(?:\s+village)?$|^village\s+(?:du\s+)?personnel$|^staff\s+micro.village$/i.test((node.textContent||"").trim()))continue;const card=node.closest("article,.card,.village-card,.housing-card,li");if(card&&!card.contains(document.getElementById("cnv-zone-map-v2")))card.remove();else node.remove();}}}
function mount(){
if(document.getElementById("cnv-zone-map-v2"))return;
const target=document.getElementById("village")||document.querySelector('[id*="village"]')||document.querySelector('a[href="#village"]')?.closest("section")||document.querySelector("main");if(!target)return;
const style=el("style");style.textContent=`
#cnv-zone-map-v2{background:#082e25;color:#f7f5ed;padding:clamp(18px,3vw,36px);border-radius:28px;margin:30px auto;max-width:1250px;font-family:inherit}
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
#cnv-zone-map-v2 .cz-controls{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:7px;margin-top:18px}
#cnv-zone-map-v2 .cz-controls button{background:var(--zone-color,#1b503e);border:1px solid #fff;color:#082e25;font-weight:700;border-radius:9px;padding:9px 3px;cursor:pointer}
#cnv-zone-map-v2 .cz-controls button[aria-pressed="true"]{background:#e7c77d;color:#15382c}
#cnv-zone-map-v2 .cz-legend{display:flex;flex-wrap:wrap;gap:10px 16px;margin:12px 0 22px}#cnv-zone-map-v2 .cz-legend-item{display:inline-flex;align-items:center;gap:6px;font-size:12px;color:#eef5ed}#cnv-zone-map-v2 .cz-legend-dot{width:12px;height:12px;border-radius:50%;border:1px solid #fff;display:inline-block}#cnv-zone-map-v2 .cz-note{color:#c6d9cb;font-size:12px;margin:15px 0 0}
@media(max-width:760px){#cnv-zone-map-v2 .cz-layout{grid-template-columns:1fr}#cnv-zone-map-v2 .cz-map{aspect-ratio:1.1}#cnv-zone-map-v2 .cz-label{display:none}#cnv-zone-map-v2 .cz-controls{grid-template-columns:repeat(9,1fr)}}
`;document.head.append(style);
const root=el("section");root.id="cnv-zone-map-v2";
const heading=el("h2","cz-title"),sub=el("p","cz-sub"),layout=el("div","cz-layout"),map=el("div","cz-map"),detail=el("div","cz-detail"),eyebrow=el("div","cz-eyebrow"),name=el("h3","cz-name"),desc=el("p","cz-desc"),controls=el("div","cz-controls"),note=el("p","cz-note");
const ns="http://www.w3.org/2000/svg",svg=document.createElementNS(ns,"svg");svg.setAttribute("viewBox","0 0 700 540");for(const radius of [60,115,170,225,280,335,390,445,500]){const c=document.createElementNS(ns,"circle");for(const [k,v] of Object.entries({cx:350,cy:270,r:radius,fill:"none",stroke:"#b6d1bb","stroke-opacity":".15"}))c.setAttribute(k,v);svg.append(c);}map.append(svg);
let current=0;const pins=[],buttons=[];
function select(i){current=i;const z=zones[i],l=lang(),t=translations[l];eyebrow.textContent=t.zone+" · "+(i+1)+" / 26 · "+z[1];name.textContent=z[0];desc.textContent=z[2];pins.forEach((p,j)=>p.setAttribute("aria-pressed",String(i===j)));buttons.forEach((p,j)=>p.setAttribute("aria-pressed",String(i===j)));}
for(let i=0;i<26;i++){const pin=el("button","cz-pin",String(i+1));pin.style.setProperty("--zone-color",typeColors[zoneTypes[i]]);pin.type="button";pin.title=(i+1)+". "+zones[i][0];pin.style.left=coords[i][0]+"%";pin.style.top=coords[i][1]+"%";pin.addEventListener("click",()=>select(i));map.append(pin);pins.push(pin);const b=el("button","",String(i+1));b.type="button";b.style.setProperty("--zone-color",typeColors[zoneTypes[i]]);b.title=zones[i][0];b.setAttribute("aria-label",(i+1)+". "+zones[i][0]);b.addEventListener("click",()=>select(i));controls.append(b);buttons.push(b);}
function localize(){const t=translations[lang()];heading.textContent=t.title;sub.textContent=t.subtitle;note.textContent=t.note;select(current);}
detail.append(eyebrow,name,desc,controls);layout.append(map,detail);root.append(heading,sub,layout,note);
const legend=el("div","cz-legend");const labels={fr:{nature:"Nature",agriculture:"Agriculture",wellness:"Bien-être",lifestyle:"Gastronomie",activities:"Activités",business:"Professionnel",entertainment:"Divertissement",housing:"Hébergements",infrastructure:"Infrastructures",services:"Services"},en:{nature:"Nature",agriculture:"Agriculture",wellness:"Wellness",lifestyle:"Dining",activities:"Activities",business:"Business",entertainment:"Entertainment",housing:"Housing",infrastructure:"Infrastructure",services:"Services"},es:{nature:"Naturaleza",agriculture:"Agricultura",wellness:"Bienestar",lifestyle:"Gastronomía",activities:"Actividades",business:"Negocios",entertainment:"Entretenimiento",housing:"Alojamientos",infrastructure:"Infraestructuras",services:"Servicios"}};for(const [type,color] of Object.entries(typeColors)){const item=el("span","cz-legend-item");const dot=el("i","cz-legend-dot");dot.style.background=color;item.append(dot,el("span","cz-legend-text",labels.fr[type]));item.dataset.type=type;legend.append(item);}root.insertBefore(legend,layout);const oldLocalize=localize;localize=function(){oldLocalize();for(const item of legend.children)item.querySelector(".cz-legend-text").textContent=labels[lang()][item.dataset.type];};target.prepend(root);localize();removeStaffVillage();
if(location.hash==="#village"){requestAnimationFrame(()=>root.scrollIntoView({block:"start",behavior:"instant"}));}
new MutationObserver(localize).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",mount);else mount();window.addEventListener("load",mount,{once:true});
})();