(function(){
"use strict";
const profiles={
creative:["Creative Explorer","palette",["Open-air art workshop","Paint, photograph or sculpt alongside other creative minds.","Creative Studio"],["Creative discoveries","Join a music, photography or artist-led experience.","Arts & Culture"],["Live music & inspiration","Discover local talent and share ideas beneath the stars.","Cultural Stage"]],
nature:["Nature Lover","leaf",["Forest bathing","A guided sensory walk beneath the trees, surrounded by birdsong.","Sanctuary"],["Permaculture discoveries","Explore edible gardens, biodiversity and regenerative practices.","Permaculture"],["Stargazing & silence","Enjoy the night sky in a peaceful nature setting.","Quiet Nature Area"]],
social:["Social Connector","users",["Meet your village","Share stories and meet inspiring people from different places.","Community Hub"],["Games & shared adventures","Join a relaxed team activity or playful group discovery.","Activities Hub"],["Music & dancing","Celebrate with new friends and an uplifting atmosphere.","Nightlife"]],
entrepreneur:["Entrepreneurial Nomad","briefcase",["Ideas that grow","Exchange ideas with founders, creators and international professionals.","Pro Hub"],["Work & connect","Choose a coworking session or join an inspiring networking conversation.","Pro Hub"],["Conversations that matter","Meet curious minds in a relaxed evening atmosphere.","Business Club"]]
};
const translations={
fr:{
profiles:{creative:"Explorateur créatif",nature:"Amoureux de la nature",social:"Esprit sociable",entrepreneur:"Nomade entrepreneur"},
entries:[
["Réveil en douceur","Ouvrez les fenêtres sur le chant des oiseaux, l'air frais et la lumière du matin.","Votre micro-village"],
["Petit-déjeuner au jardin","Savourez fruits frais, produits locaux et pain croustillant lors d'un petit-déjeuner bio sans précipitation.","Restauration & Gastronomie"],
["Une petite aventure","Suivez un sentier ombragé et découvrez les paysages à votre rythme.","Nature & Activités"],
["Votre expérience signature","Une expérience mémorable choisie selon vos centres d'intérêt.","Expérience personnalisée"],
["Déjeuner avec vue","Partagez un repas de saison et de belles conversations dans une ambiance détendue.","Restauration & Gastronomie"],
["Rechargez vos batteries","Profitez du spa, d'un yoga doux, d'un hamac ou d'un moment de liberté absolue.","Spa & Bien-être"],
["Une nouvelle découverte","Explorez une passion et laissez-vous surprendre par une rencontre inattendue.","Activités & Expériences"],
["L'heure dorée","Savourez une boisson fraîche dans la douce lumière du soir.","Salon du jardin"],
["Dîner & conversations","Dégustez des plats de saison et prolongez les conversations autour de la table.","Restauration & Gastronomie"],
["Une soirée inoubliable","Choisissez musique, culture, danse ou conversations sous les arbres.","Culture & Divertissements"],
["Douceur sous les étoiles","Terminez la journée par une promenade paisible avant une nuit réparatrice.","Votre micro-village"]],
special:{creative:[["Atelier artistique en plein air","Peignez, photographiez ou sculptez avec d'autres passionnés.","Studio créatif"],["Découvertes créatives","Participez à une expérience musicale, photographique ou artistique.","Arts & Culture"],["Musique live & inspiration","Découvrez de nouveaux talents et échangez des idées sous les étoiles.","Scène culturelle"]],nature:[["Bain de forêt","Une promenade sensorielle guidée sous les arbres, au chant des oiseaux.","Sanctuary"],["Découverte de la permaculture","Explorez jardins comestibles, biodiversité et pratiques régénératrices.","Permaculture"],["Observation des étoiles","Admirez le ciel nocturne dans un cadre naturel paisible.","Espace nature calme"]],social:[["Rencontrez votre village","Partagez des histoires et rencontrez des personnes inspirantes.","Espace communautaire"],["Jeux & aventures partagées","Participez à une activité collective conviviale.","Pôle activités"],["Musique & danse","Célébrez la soirée avec de nouveaux amis.","Vie nocturne"]],entrepreneur:[["Des idées qui grandissent","Échangez avec des fondateurs, créateurs et professionnels internationaux.","Pro Hub"],["Travail & rencontres","Profitez d'un espace de coworking ou d'une rencontre inspirante.","Pro Hub"],["Conversations inspirantes","Rencontrez des esprits curieux dans une ambiance détendue.","Business Club"]]},
alternate:[["Promenade en pleine conscience","Découvrez des sentiers secrets et de beaux espaces verts.","Sentiers nature"],["Pause ressourçante","Essayez une activité douce, un rituel spa ou un moment de détente.","Spa & Bien-être"]]},
es:{
profiles:{creative:"Explorador creativo",nature:"Amante de la naturaleza",social:"Conector social",entrepreneur:"Nómada emprendedor"},
entries:[
["Despertar naturalmente","Abre las ventanas al canto de los pájaros, el aire fresco y la suave luz de la mañana.","Tu microaldea"],
["Desayuno en el jardín","Disfruta de fruta fresca, productos locales, pan recién hecho y un desayuno ecológico sin prisas.","Gastronomía"],
["Una pequeña aventura","Sigue un sendero sombreado y descubre los paisajes a tu ritmo.","Naturaleza y actividades"],
["Tu experiencia especial","Una experiencia memorable elegida según tus intereses.","Experiencia personalizada"],
["Almuerzo con vistas","Comparte una comida de temporada y conversaciones agradables.","Gastronomía"],
["Recarga energías","Disfruta del spa, yoga suave, una hamaca o un momento de libertad.","Spa y bienestar"],
["Descubre algo nuevo","Explora una nueva pasión y déjate sorprender.","Actividades y experiencias"],
["La hora dorada","Disfruta de una bebida refrescante bajo la cálida luz del atardecer.","Salón del jardín"],
["Cena y conversaciones","Saborea platos de temporada y disfruta de conversaciones inolvidables.","Gastronomía"],
["Una noche para recordar","Elige música, cultura, baile o conversaciones bajo los árboles.","Cultura y entretenimiento"],
["Relájate bajo las estrellas","Da un último paseo tranquilo antes de regresar a descansar.","Tu microaldea"]],
special:{creative:[["Taller de arte al aire libre","Pinta, fotografía o esculpe junto a otras mentes creativas.","Estudio creativo"],["Descubrimientos creativos","Participa en una experiencia musical, fotográfica o artística.","Arte y cultura"],["Música en vivo e inspiración","Descubre talentos locales y comparte ideas bajo las estrellas.","Escenario cultural"]],nature:[["Baño de bosque","Un paseo sensorial guiado entre árboles y cantos de pájaros.","Sanctuary"],["Descubre la permacultura","Explora huertos comestibles, biodiversidad y prácticas regenerativas.","Permacultura"],["Observación de estrellas","Contempla el cielo nocturno en un entorno natural tranquilo.","Zona natural tranquila"]],social:[["Conoce tu aldea","Comparte historias y conoce a personas inspiradoras.","Espacio comunitario"],["Juegos y aventuras compartidas","Únete a una actividad en grupo divertida y relajada.","Zona de actividades"],["Música y baile","Celebra con nuevos amigos en un ambiente alegre.","Vida nocturna"]],entrepreneur:[["Ideas que crecen","Intercambia ideas con emprendedores, creadores y profesionales internacionales.","Pro Hub"],["Trabaja y conecta","Elige una sesión de coworking o una conversación inspiradora.","Pro Hub"],["Conversaciones que importan","Conoce a personas interesantes en un ambiente relajado.","Business Club"]]},
alternate:[["Paseo consciente por la naturaleza","Descubre senderos escondidos y espacios verdes preciosos.","Senderos naturales"],["Una pausa para renovarte","Prueba movimiento suave, un ritual de spa o simplemente descansa.","Spa y bienestar"]]}
};
const times=["08:00","08:45","10:00","11:30","13:00","14:30","16:00","18:00","19:30","21:00","23:00"];
const base=[
["sunrise","Wake up naturally","Open your windows to birdsong, fresh air and gentle morning light.","Your micro-village"],
["coffee","Breakfast in the garden","Enjoy fresh fruit, local produce, warm bread and an unhurried organic breakfast.","Dining & Gastronomy"],
["trees","A little adventure","Follow a shaded trail and discover the landscapes at your own pace.","Nature & Activities"],
["sparkles","Your signature experience","A memorable experience chosen to match your interests.","Personalised experience"],
["utensils","Lunch with a view","Share a seasonal meal and enjoy relaxed conversations with fellow guests.","Dining & Gastronomy"],
["heart","Recharge your energy","Enjoy the spa, gentle yoga, a hammock or a moment of complete freedom.","Spa & Wellness"],
["compass","Discover something new","Explore a new passion and encounter something unexpected.","Activities & Experiences"],
["sunset","The golden hour","Enjoy a refreshing drink and the warm evening light over the gardens.","Garden lounge"],
["utensils","Dinner & conversations","Taste seasonal dishes and linger over meaningful conversations.","Dining & Gastronomy"],
["music","An evening to remember","Choose music, culture, dancing or quiet conversation beneath the trees.","Culture & Entertainment"],
["moon","Slow down under the stars","Take a final peaceful stroll before returning for a restful night.","Your micro-village"]
];
const icons={sunrise:"☀",coffee:"☕",trees:"♧",sparkles:"✧",utensils:"♨",heart:"♡",compass:"⌁",sunset:"◒",music:"♫",moon:"☾",palette:"✎",leaf:"♧",users:"♧",briefcase:"▣"};
const tr={
en:{title:"Your perfect day at CNV",sub:"From sunrise to starlight. A day that feels like you.",again:"Try another day",note:"Your programme is an invitation, not a fixed schedule. Follow your curiosity.",where:"Experience"},
fr:{title:"Votre journée idéale à CNV",sub:"Du lever du soleil aux étoiles, une journée qui vous ressemble.",again:"Une autre journée",note:"Ce programme est une invitation, jamais une obligation. Suivez vos envies.",where:"Expérience"},
es:{title:"Tu día ideal en CNV",sub:"Del amanecer a las estrellas. Un día hecho para ti.",again:"Probar otro día",note:"Este programa es una invitación, no un horario obligatorio. Sigue tu curiosidad.",where:"Experiencia"}
};
function clean(s){return (s||"").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"");}
function lang(){return (document.documentElement.lang||"en").slice(0,2).toLowerCase();}
function profile(){const host=document.querySelector("#cnv-day-experience");const candidates=[...document.querySelectorAll("select,button,[role=option],[aria-selected=true],input:checked")].filter(x=>!host||!host.contains(x));let s=clean(candidates.filter(x=>x.matches("select,[aria-selected=true],input:checked")).map(x=>x.selectedOptions?x.selectedOptions[0]?.textContent:x.closest("label")?.textContent||x.textContent).join(" "));if(/nature|natural|forest|contemplat|regenerat/.test(s))return "nature";if(/social|community|connect|family|famille|familia/.test(s))return "social";if(/business|entrepren|nomad|digital|profession/.test(s))return "entrepreneur";return "creative";}
let variation=0,last="";
function render(){const root=document.getElementById("cnv-day-experience");if(!root)return;const l=tr[lang()]||tr.en;const key=profile();const fingerprint=key+"|"+lang()+"|"+variation;if(last===fingerprint)return;last=fingerprint;const p=profiles[key];root.innerHTML="";const heading=document.createElement("h3");heading.textContent=l.title;root.appendChild(heading);const intro=document.createElement("p");intro.className="cnv-day-sub";intro.textContent=l.sub;root.appendChild(intro);const bar=document.createElement("div");bar.className="cnv-day-bar";const pill=document.createElement("span");pill.className="cnv-day-pill";pill.textContent="✧ "+(translations[lang()]?.profiles[key]||p[0]);bar.appendChild(pill);const btn=document.createElement("button");btn.type="button";btn.textContent="↻ "+l.again;btn.addEventListener("click",()=>{variation++;last="";render()});bar.appendChild(btn);root.appendChild(bar);
const timeline=document.createElement("div");timeline.className="cnv-day-timeline";
base.forEach((entry,i)=>{let data=entry.slice();if([3,6,9].includes(i)){const v=p[[3,6,9].indexOf(i)+2];data=[p[1],...v];}if(variation%2){if(i===2)data=["trees","A mindful nature walk","Discover hidden paths and beautiful green spaces.","Nature trails"];if(i===5)data=["heart","A peaceful reset","Try gentle movement, a spa ritual or simply unwind.","Spa & Wellness"];}
const locale=translations[lang()];if(locale){const v=locale.entries[i];data=[data[0],...v];if([3,6,9].includes(i))data=[data[0],...locale.special[key][[3,6,9].indexOf(i)]];if(variation%2&&i===2)data=["trees",...locale.alternate[0]];if(variation%2&&i===5)data=["heart",...locale.alternate[1]];}const item=document.createElement("article");item.className="cnv-day-item";const clock=document.createElement("span");clock.className="cnv-day-time";clock.textContent=times[i];const symbol=document.createElement("span");symbol.className="cnv-day-icon";symbol.textContent=icons[data[0]]||"✧";const content=document.createElement("div");const h=document.createElement("h4");h.textContent=data[1];const desc=document.createElement("p");desc.textContent=data[2];const place=document.createElement("small");place.textContent="⌖ "+data[3];content.append(h,desc,place);item.append(clock,symbol,content);timeline.appendChild(item);});root.appendChild(timeline);const foot=document.createElement("p");foot.className="cnv-day-foot";foot.textContent="✧ "+l.note;root.appendChild(foot);}
function init(){
if(document.getElementById("cnv-day-experience"))return;
const art=document.getElementById("artoflife"),life=document.getElementById("life");
if(!art)return;
const root=document.createElement("div");root.id="cnv-day-experience";root.className="cnv-day-experience";
const charter=art.querySelector(".cnv-charter-cta");if(charter)art.insertBefore(root,charter);else art.appendChild(root);
if(life)life.style.display="none";
render();
document.addEventListener("change",()=>{last="";render()},true);
document.addEventListener("click",e=>{
if(e.target.closest("#cnv-day-experience"))return;
const action=e.target.closest("button,a,[role=button],option,[role=option]");
const label=(action?.textContent||action?.getAttribute("aria-label")||"").trim().toLowerCase();
const choose=/choisir votre profil|choose your profile|select your profile|elige tu perfil|elegir perfil|seleccionar perfil|voir mon programme|see my programme|ver mi programa/.test(label);
setTimeout(()=>{
last="";render();
if(choose){
const panel=document.getElementById("cnv-day-experience");
if(panel){panel.hidden=false;panel.style.display="";panel.scrollIntoView({behavior:"smooth",block:"start"});}
}
},180);
},true);
new MutationObserver(()=>{if((tr[lang()]||tr.en).title!==root.querySelector("h3")?.textContent){last="";render()}}).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();