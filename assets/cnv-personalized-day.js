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
function lang(){
const selected=[...document.querySelectorAll("button,a,[data-lang],[lang]")].filter(e=>!e.closest("#cnv-day-experience")&&/^(FR|EN|ES)$/i.test((e.textContent||"").trim()));
const active=selected.find(e=>e.classList.contains("active")||e.classList.contains("selected")||e.getAttribute("aria-pressed")==="true"||e.getAttribute("aria-current")==="true");
if(active)return (active.getAttribute("data-lang")||active.textContent).trim().toLowerCase();
const stored=["lang","language","cnv_lang","cnv_language"].map(k=>{try{return localStorage.getItem(k)}catch(e){return null}}).find(v=>/^(fr|en|es)$/i.test(v||""));
return (stored||document.documentElement.lang||"fr").slice(0,2).toLowerCase();
}
function selectedProfile(){
const selects=[...document.querySelectorAll("select")].filter(e=>!e.closest("#cnv-day-experience"));
const p=selects.find(e=>/profil|profile|perfil/i.test((e.closest("label")?.textContent||"")+" "+(e.previousElementSibling?.textContent||"")+" "+(e.id||"")+" "+(e.name||"")))||selects[1]||selects[0];
return p?.selectedOptions?.[0]?.textContent?.trim()||"";
}
function profile(){
const value=clean(selectedProfile()+" "+[...document.querySelectorAll("select")].map(e=>e.selectedOptions?.[0]?.textContent||"").join(" "));
if(/leader|startup|start.up|business|entrepren|nomad|digital|profession|b.tisseur|constructor|builder|invest|founder|fondateur|innov/.test(value))return "entrepreneur";
if(/nature|natural|forest|contemplat|regenerat|ecolog|jardin|garden/.test(value))return "nature";
if(/social|community|connect|family|famille|familia|relation|human|rencontre/.test(value))return "social";
return "creative";
}

// Each of the 50 existing selector options has a stable, independent itinerary.
// Themes stay grounded in the facilities already planned for CNV.
const itineraryThemes={
fr:[
[["Rencontre inspirante","Échangez avec des personnes qui partagent vos ambitions autour d'un café.","Pro Hub"],["Atelier d'idées","Transformez une intuition en projet lors d'un atelier collaboratif.","Pro Hub"],["Réseau international","Retrouvez des créateurs et entrepreneurs dans une atmosphère détendue.","Business Club"]],
[["Balade sensorielle","Découvrez les parfums, textures et sons d'un sentier préservé.","Sanctuary"],["Jardins vivants","Explorez la forêt nourricière et les cultures en permaculture.","Permaculture"],["Ciel étoilé","Observez les étoiles et appréciez le calme de la nature.","Espace nature"]],
[["Élan créatif","Expérimentez peinture, photographie ou sculpture en plein air.","Ateliers créatifs"],["Scène ouverte","Partagez vos créations et découvrez celles des autres.","Espace culturel"],["Concert intimiste","Profitez de musiques vivantes sous les arbres.","Scène culturelle"]],
[["Équilibre du corps","Essayez une séance de yoga ou de respiration consciente.","Spa & Bien-être"],["Pause profonde","Offrez-vous un massage ou un bain relaxant.","Spa & Bien-être"],["Méditation au crépuscule","Terminez la journée dans la sérénité.","Jardin zen"]],
[["Découverte active","Essayez un parcours nature, le vélo ou une activité de plein air.","Activités & Expériences"],["Défi ludique","Partagez une activité sportive adaptée à votre rythme.","Pôle activités"],["Soirée aventure","Échangez vos découvertes autour d'une ambiance conviviale.","Espace communautaire"]],
[["Rencontres spontanées","Rejoignez une tablée conviviale et faites connaissance.","Place du village"],["Expérience collective","Participez à un jeu, un atelier ou une activité en équipe.","Espace communautaire"],["Fête et convivialité","Retrouvez de nouveaux amis autour de musique et de danse.","Nightlife"]]
],
en:[
[["Inspiring connections","Exchange ideas with like-minded people over coffee.","Pro Hub"],["Ideas workshop","Turn a spark of inspiration into a collaborative project.","Pro Hub"],["International networking","Meet creators and founders in a relaxed setting.","Business Club"]],
[["Sensory nature walk","Discover the scents, textures and sounds of a protected trail.","Sanctuary"],["Living gardens","Explore the food forest and permaculture gardens.","Permaculture"],["Starry skies","Watch the stars and enjoy the silence of nature.","Nature area"]],
[["Creative energy","Experiment with painting, photography or outdoor sculpture.","Creative Studios"],["Open stage","Share your creations and discover the work of others.","Cultural Hub"],["Intimate concert","Enjoy live music beneath the trees.","Cultural Stage"]],
[["Body balance","Try yoga or mindful breathing.","Spa & Wellness"],["Deep relaxation","Enjoy a massage or a soothing bath.","Spa & Wellness"],["Sunset meditation","End the day in calm and stillness.","Zen Garden"]],
[["Active discovery","Try a nature trail, cycling or an outdoor activity.","Activities & Experiences"],["Playful challenge","Share an activity at your own pace.","Activities Hub"],["Adventure stories","Swap stories from the day in a friendly setting.","Community Hub"]],
[["Spontaneous connections","Join a welcoming shared table and meet new people.","Village Square"],["Together is better","Take part in a game, workshop or group experience.","Community Hub"],["Music and friendship","Meet new friends for music and dancing.","Nightlife"]]
],
es:[
[["Conexiones inspiradoras","Intercambia ideas con personas afines mientras tomas un café.","Pro Hub"],["Taller de ideas","Convierte una inspiración en un proyecto colaborativo.","Pro Hub"],["Red internacional","Conoce a creadores y emprendedores en un ambiente relajado.","Business Club"]],
[["Paseo sensorial","Descubre aromas, texturas y sonidos de un sendero protegido.","Sanctuary"],["Jardines vivos","Explora el bosque comestible y los huertos de permacultura.","Permacultura"],["Cielo estrellado","Observa las estrellas y disfruta del silencio de la naturaleza.","Zona natural"]],
[["Energía creativa","Experimenta con pintura, fotografía o escultura al aire libre.","Talleres creativos"],["Escenario abierto","Comparte tus creaciones y descubre las de otras personas.","Espacio cultural"],["Concierto íntimo","Disfruta de música en vivo bajo los árboles.","Escenario cultural"]],
[["Equilibrio corporal","Prueba yoga o respiración consciente.","Spa y bienestar"],["Relajación profunda","Disfruta de un masaje o un baño relajante.","Spa y bienestar"],["Meditación al atardecer","Termina el día en calma.","Jardín zen"]],
[["Descubrimiento activo","Prueba un sendero, ciclismo o una actividad al aire libre.","Actividades y experiencias"],["Reto divertido","Comparte una actividad a tu ritmo.","Zona de actividades"],["Historias de aventura","Comparte tus descubrimientos en un ambiente acogedor.","Espacio comunitario"]],
[["Encuentros espontáneos","Comparte mesa y conoce gente nueva.","Plaza del pueblo"],["Mejor juntos","Participa en un juego, taller o experiencia en grupo.","Espacio comunitario"],["Música y amistad","Reúnete con nuevos amigos para escuchar música y bailar.","Vida nocturna"]]
]};
function stableIndex(value){let h=2166136261;for(const c of value){h=Math.imul(h^c.charCodeAt(0),16777619);}return h>>>0;}
function themedExperiences(name,category,locale,dayVariant){
const v=clean(name+" "+category);
let theme=/yoga|wellness|bien.tre|bienestar|sant.|health|meditat|spa|senior|repos|relax/.test(v)?3:
/nature|natural|forest|contemplat|regenerat|ecolog|jardin|garden|agric|permacult|animal/.test(v)?1:
/art|creat|music|musique|musica|design|artist|photograph|culture|maker/.test(v)?2:
/sport|advent|aventur|explor|outdoor|athlet|randonn|travel|voyage/.test(v)?4:
/social|community|connect|family|famille|familia|relation|human|rencontre|f.te|fiesta/.test(v)?5:0;
const pool=itineraryThemes[locale]||itineraryThemes.en;
const hash=stableIndex(v);
const offset=(hash+dayVariant)%3;
return [pool[theme][offset],pool[theme][(offset+1)%3],pool[theme][(offset+2)%3]];
}

const cnvSlotPools={"fr":[[["Réveil au chant des oiseaux","Accueillez le jour en douceur depuis votre hébergement.","Micro-village"],["Étirements au lever du soleil","Réveillez votre corps avec une séance de mouvements doux.","Jardin bien-être"],["Méditation matinale","Commencez la journée par quelques minutes de respiration consciente.","Espace calme"]],[["Petit-déjeuner bio","Dégustez des produits frais et locaux.","Gastronomie"],["Petit-déjeuner convivial","Rejoignez une grande table pour faire connaissance.","Salle à manger"],["Petit-déjeuner au jardin","Savourez votre matinée au grand air.","Jardin"]],[["Balade en forêt","Explorez les sentiers ombragés et la biodiversité.","Sentiers nature"],["Découverte de la permaculture","Visitez les jardins nourriciers et les cultures écologiques.","Permaculture"],["Parcours sensoriel","Découvrez la nature à travers les sons et les parfums.","Sanctuary"]],[["Atelier de découverte","Participez à une expérience guidée autour de votre passion.","Pôle activités"]],[["Déjeuner des producteurs","Savourez une cuisine de saison issue des jardins.","Gastronomie"],["Grande tablée conviviale","Partagez un déjeuner avec les membres du village.","Restaurant communautaire"],["Déjeuner végétal","Découvrez des recettes fraîches et créatives.","Gastronomie"]],[["Bain relaxant","Profitez d'une pause ressourçante dans l'espace bien-être.","Spa"],["Yoga doux","Détendez le corps et l'esprit à votre rythme.","Espace yoga"],["Sieste dans un hamac","Offrez-vous une pause paisible à l'ombre des arbres.","Jardin calme"]],[["Expérience de l'après-midi","Découvrez une nouvelle activité adaptée à vos envies.","Pôle activités"]],[["Coucher de soleil panoramique","Admirez les couleurs du soir depuis un belvédère.","Terrasse panoramique"],["Promenade dorée","Profitez d'une balade paisible dans la lumière du soir.","Jardins"],["Apéritif sans alcool au jardin","Partagez un moment chaleureux autour d'une boisson fraîche.","Lounge nature"]],[["Dîner gastronomique","Découvrez une cuisine locale et créative.","Gastronomie"],["Dîner partagé","Retrouvez d'autres membres autour d'une grande table.","Restaurant communautaire"],["Soirée saveurs du monde","Explorez une cuisine thématique et de nouvelles rencontreconst langCode=lang();
const choices=cnvChoicesForSlot(i,selectedProfile(),key,langCode,data.slice(1));
let choiceIndex=0;
const next=document.createElement("button");next.type="button";next.className="cnv-day-next-choice";
next.textContent=langCode==="fr"?"↻ Autre proposition":langCode==="es"?"↻ Otra propuesta":"↻ Another suggestion";
next.setAttribute("aria-label",next.textContent+" "+times[i]);
next.addEventListener("click",()=>{
choiceIndex=(choiceIndex+1)%choices.length;
const chosen=choices[choiceIndex];
h.textContent=chosen[0];desc.textContent=chosen[1];place.textContent="⌖ "+chosen[2];
});
content.appendChild(next);
softly lit village paths.","Village Paths"],["Reading and rest","Wind down in the comfort of your accommodation.","Micro-village"]]],"es":[[["Despertar con los pájaros","Empieza el día suavemente con los sonidos de la naturaleza.","Microaldea"],["Estiramientos al amanecer","Activa tu cuerpo con movimientos suaves.","Jardín de bienestar"],["Meditación matinal","Comienza con respiración consciente.","Zona tranquila"]],[["Desayuno ecológico","Disfruta de alimentos frescos y locales.","Gastronomía"],["Desayuno compartido","Conoce a otras personas alrededor de una mesa.","Comedor"],["Desayuno en el jardín","Disfruta de una mañana tranquila al aire libre.","Jardín"]],[["Paseo por el bosque","Explora senderos sombreados y biodiversidad.","Senderos naturales"],["Descubre la permacultura","Visita huertos comestibles y cultivos ecológicos.","Permacultura"],["Sendero sensorial","Descubre aromas y sonidos de la naturaleza.","Sanctuary"]],[["Taller de descubrimiento","Disfruta de una experiencia guiada según tus intereses.","Zona de actividades"]],[["Almuerzo de temporada","Prueba cocina fresca y local.","Gastronomía"],["Almuerzo comunitario","Comparte mesa con otros miembros.","Comedor comunitario"],["Almuerzo vegetal","Descubre recetas frescas y creativas.","Gastronomía"]],[["Baño relajante","Disfruta de una pausa de bienestar.","Spa"],["Yoga suave","Relaja cuerpo y mente a tu ritmo.","Zona de yoga"],["Siesta en hamaca","Descansa tranquilamente bajo los árboles.","Jardín tranquilo"]],[["Experiencia de tarde","Explora una actividad según tus intereses.","Zona de actividades"]],[["Atardecer panorámico","Contempla los colores de la tarde desde un mirador.","Terraza panorámica"],["Paseo al atardecer","Camina por los jardines bajo una luz cálida.","Jardines"],["Cócteles sin alcohol","Comparte una bebida refrescante al aire libre.","Salón natural"]],[["Cena creativa","Descubre cocina local de temporada.","Gastronomía"],["Cena compartida","Reúnete con otros miembros alrededor de la mesa.","Comedor comunitario"],["Sabores del mundo","Explora una cena temática y nuevas conversaciones.","Gastronomía"]],[["Noche cultural","Disfruta de un espectáculo o encuentro inspirador.","Espacio cultural"]],[["Observar las estrellas","Contempla el cielo nocturno en paz.","Zona natural"],["Paseo nocturno","Camina por senderos suavemente iluminados.","Caminos de la aldea"],["Lectura y descanso","Termina el día tranquilamente en tu alojamiento.","Microaldea"]]]};
function cnvChoicesForSlot(i,profileName,key,locale,current){
const slots=cnvSlotPools[locale]||cnvSlotPools.en;
const special=themedExperiences(profileName,key,locale,0);
const options=[...(slots[i]||[])];
if(i===3||i===6||i===9)options.unshift(...special);
const seen=new Set();const unique=[];
for(const entry of [current,...options]){if(!entry||!entry[0]||seen.has(entry[0]))continue;seen.add(entry[0]);unique.push(entry);}
const rotation=stableIndex(clean(profileName)+"|"+i)%Math.max(1,unique.length);
return [unique[0],...unique.slice(1+rotation),...unique.slice(1,1+rotation)];
}

let variation=0,last="";
function render(){const root=document.getElementById("cnv-day-experience");if(!root)return;const l=tr[lang()]||tr.en;const key=profile();const fingerprint=key+"|"+selectedProfile()+"|"+lang()+"|"+variation;if(last===fingerprint)return;last=fingerprint;const p=profiles[key];root.innerHTML="";const heading=document.createElement("h3");heading.textContent=l.title;root.appendChild(heading);const intro=document.createElement("p");intro.className="cnv-day-sub";intro.textContent=l.sub;root.appendChild(intro);const bar=document.createElement("div");bar.className="cnv-day-bar";const pill=document.createElement("span");pill.className="cnv-day-pill";pill.textContent="✧ "+(selectedProfile()||translations[lang()]?.profiles[key]||p[0]);bar.appendChild(pill);root.appendChild(bar);
const timeline=document.createElement("div");timeline.className="cnv-day-timeline";const unique=themedExperiences(selectedProfile(),key,lang(),variation);
base.forEach((entry,i)=>{let data=entry.slice();if([3,6,9].includes(i)){const v=p[[3,6,9].indexOf(i)+2];data=[p[1],...v];}if(variation%2){if(i===2)data=["trees","A mindful nature walk","Discover hidden paths and beautiful green spaces.","Nature trails"];if(i===5)data=["heart","A peaceful reset","Try gentle movement, a spa ritual or simply unwind.","Spa & Wellness"];}
const locale=translations[lang()];if(locale){const v=locale.entries[i];data=[data[0],...v];if([3,6,9].includes(i))data=[data[0],...locale.special[key][[3,6,9].indexOf(i)]];if(variation%2&&i===2)data=["trees",...locale.alternate[0]];if(variation%2&&i===5)data=["heart",...locale.alternate[1]];}if([3,6,9].includes(i))data=[data[0],...unique[[3,6,9].indexOf(i)]];const item=document.createElement("article");item.className="cnv-day-item";const clock=document.createElement("span");clock.className="cnv-day-time";clock.textContent=times[i];const symbol=document.createElement("span");symbol.className="cnv-day-icon";symbol.textContent=icons[data[0]]||"✧";const content=document.createElement("div");const h=document.createElement("h4");h.textContent=data[1];const desc=document.createElement("p");desc.textContent=data[2];const place=document.createElement("small");place.textContent="⌖ "+data[3];content.append(h,desc,place);
const picker=document.createElement("select");picker.className="cnv-day-choice";
const langCode=lang();const profileName=selectedProfile();const category=key;
const themed=themedExperiences(profileName,category,langCode,0);
const local=translations[langCode];
const choices=[data.slice(1)];
if([3,6,9].includes(i)){
for(const candidate of themed){if(!choices.some(v=>v[0]===candidate[0]))choices.push(candidate);}
}else{
const extra=(itineraryThemes[langCode]||itineraryThemes.en);
const themeIndex=/nature|natural|forest|ecolog|jardin/i.test(clean(profileName))?1:/art|creat|music/i.test(clean(profileName))?2:/sport|advent|explor/i.test(clean(profileName))?4:/wellness|yoga|spa|senior/i.test(clean(profileName))?3:/social|family|famille|community/i.test(clean(profileName))?5:0;
const theme=extra[themeIndex];
const alt=local?.alternate||[];
const additions=(i===0||i===1||i===4||i===8||i===10)?[
(i===0?local?.entries[2]:i===1?local?.entries[4]:i===4?local?.entries[8]:i===8?local?.entries[4]:local?.entries[7]),
theme[(i+1)%3]
]:[theme[i%3],theme[(i+1)%3],...(i===2||i===5?alt.slice(0,1):[])];
for(const candidate of additions){if(candidate&&!choices.some(v=>v[0]===candidate[0]))choices.push(candidate);}
}
const choiceLabel=langCode==="fr"?"Autre activité à ce créneau":langCode==="es"?"Otra actividad en este horario":"Alternative activity for this time";
picker.setAttribute("aria-label",choiceLabel+" "+times[i]);picker.title=choiceLabel;
choices.forEach((choice,n)=>{const option=document.createElement("option");option.value=String(n);option.textContent=choice[0];picker.appendChild(option);});
picker.addEventListener("change",()=>{const chosen=choices[Number(picker.value)]||choices[0];h.textContent=chosen[0];desc.textContent=chosen[1];place.textContent="⌖ "+chosen[2];});
const choiceWrap=document.createElement("div");choiceWrap.className="cnv-day-choice-wrap";
const choiceText=document.createElement("span");choiceText.textContent=choiceLabel+": ";
const next=document.createElement("button");next.type="button";next.className="cnv-day-next-choice";
next.textContent=langCode==="fr"?"↻ Autre proposition":langCode==="es"?"↻ Otra propuesta":"↻ Another suggestion";
next.addEventListener("click",()=>{const current=Number(picker.value);const nextIndex=(current+1)%choices.length;picker.value=String(nextIndex);picker.dispatchEvent(new Event("change",{bubbles:false}));});
choiceWrap.append(choiceText,picker,next);content.appendChild(choiceWrap);
item.append(clock,symbol,content);timeline.appendChild(item);});root.appendChild(timeline);const foot=document.createElement("p");foot.className="cnv-day-foot";foot.textContent="✧ "+l.note;root.appendChild(foot);}
function init(){
if(document.getElementById("cnv-day-experience"))return;
const art=document.getElementById("artoflife"),life=document.getElementById("life");
if(!art)return;
const root=document.createElement("div");root.id="cnv-day-experience";root.className="cnv-day-experience";
const charter=art.querySelector(".cnv-charter-cta");if(charter)art.insertBefore(root,charter);else art.appendChild(root);
if(life)life.style.display="none";
render();
document.addEventListener("change",e=>{last="";render();if(e.target.matches("select")){const panel=document.getElementById("cnv-day-experience");if(panel)requestAnimationFrame(()=>panel.scrollIntoView({behavior:"smooth",block:"start"}));}},true);
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