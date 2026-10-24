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

const cnvSlotPools={
en:[
[["Sunrise stretching","Gently wake up with mindful movement.","Wellness Garden"],["Morning meditation","Start the day with fresh air and quiet reflection.","Quiet Garden"]],
[["Shared organic breakfast","Meet fellow members over local produce.","Dining & Gastronomy"],["Garden breakfast","Enjoy a relaxed breakfast outdoors.","Garden Terrace"]],
[["Forest trail walk","Discover local wildlife on shaded trails.","Nature Trails"],["Guided permaculture tour","Explore edible gardens and regenerative growing.","Permaculture"]],
[["Outdoor adventure","Explore a guided activity suited to your interests.","Activities & Experiences"],["Creative workshop","Try photography or painting with other members.","Creative Studio"]],
[["Farm-to-table lunch","Enjoy fresh seasonal dishes.","Dining & Gastronomy"],["Community lunch","Share a relaxed meal and conversations.","Community Dining"]],
[["Spa and relaxation","Unwind in a quiet wellness space.","Spa & Wellness"],["Gentle yoga","Restore your energy through movement.","Yoga Terrace"]],
[["Afternoon workshop","Explore an activity that inspires you.","Activities & Experiences"],["Collaborative exchange","Join a small-group experience.","Community Hub"]],
[["Sunset nature walk","Watch the gardens glow in the evening light.","Garden Trails"],["Garden mocktails","Meet friends for a refreshing alcohol-free drink.","Garden Lounge"]],
[["Seasonal dinner","Taste locally inspired dishes.","Dining & Gastronomy"],["Shared table dinner","Enjoy good food and new connections.","Community Dining"]],
[["Live music","Enjoy an intimate evening performance.","Cultural Stage"],["Evening conversations","Exchange ideas with fellow members.","Community Lounge"]],
[["Stargazing","Watch the stars in a peaceful setting.","Quiet Nature Area"],["Restful evening","Wind down with a book and a calm atmosphere.","Your micro-village"]]
],
fr:[
[["Étirements au lever du soleil","Réveillez votre corps en douceur.","Jardin bien-être"],["Méditation matinale","Commencez la journée dans le calme.","Jardin paisible"]],
[["Petit-déjeuner partagé","Rencontrez les membres autour de produits locaux.","Restauration & Gastronomie"],["Petit-déjeuner au jardin","Savourez votre matinée en plein air.","Terrasse du jardin"]],
[["Balade en forêt","Découvrez les sentiers et la biodiversité.","Sentiers nature"],["Visite de la permaculture","Explorez les jardins nourriciers et les cultures écologiques.","Permaculture"]],
[["Aventure de plein air","Participez à une activité adaptée à vos envies.","Activités & Expériences"],["Atelier créatif","Essayez la photographie ou la peinture.","Atelier créatif"]],
[["Déjeuner des producteurs","Savourez des plats frais et de saison.","Restauration & Gastronomie"],["Déjeuner convivial","Partagez un repas et des conversations.","Restaurant communautaire"]],
[["Pause spa","Détendez-vous dans un espace bien-être.","Spa & Bien-être"],["Yoga doux","Retrouvez votre énergie avec des mouvements simples.","Terrasse yoga"]],
[["Atelier de l'après-midi","Découvrez une expérience qui vous inspire.","Activités & Expériences"],["Échange collaboratif","Participez à une expérience en petit groupe.","Espace communautaire"]],
[["Balade au coucher du soleil","Profitez de la lumière dorée des jardins.","Sentiers des jardins"],["Cocktail sans alcool","Retrouvez vos amis autour d'une boisson fraîche.","Lounge jardin"]],
[["Dîner de saison","Découvrez une cuisine locale et créative.","Restauration & Gastronomie"],["Grande tablée","Partagez un dîner et de nouvelles rencontres.","Restaurant communautaire"]],
[["Musique live","Découvrez un concert intimiste.","Scène culturelle"],["Conversations du soir","Échangez avec les autres membres.","Salon communautaire"]],
[["Observation des étoiles","Admirez le ciel nocturne dans le calme.","Espace nature"],["Soirée reposante","Terminez la journée avec un livre.","Votre micro-village"]]
],
es:[
[["Estiramientos al amanecer","Despierta suavemente con movimientos conscientes.","Jardín de bienestar"],["Meditación matinal","Empieza el día con calma.","Jardín tranquilo"]],
[["Desayuno compartido","Conoce a otros miembros mientras disfrutas productos locales.","Gastronomía"],["Desayuno en el jardín","Disfruta de una mañana al aire libre.","Terraza del jardín"]],
[["Paseo por el bosque","Descubre senderos y biodiversidad.","Senderos naturales"],["Visita a la permacultura","Explora huertos y cultivos ecológicos.","Permacultura"]],
[["Aventura al aire libre","Participa en una actividad adaptada a tus intereses.","Actividades y experiencias"],["Taller creativo","Prueba fotografía o pintura.","Taller creativo"]],
[["Almuerzo de temporada","Disfruta de platos frescos y locales.","Gastronomía"],["Almuerzo comunitario","Comparte una comida y nuevas conversaciones.","Comedor comunitario"]],
[["Pausa de spa","Relájate en un espacio de bienestar.","Spa y bienestar"],["Yoga suave","Recupera tu energía con movimientos tranquilos.","Terraza de yoga"]],
[["Taller de tarde","Descubre una experiencia inspiradora.","Actividades y experiencias"],["Intercambio colaborativo","Participa en una experiencia en grupo.","Espacio comunitario"]],
[["Paseo al atardecer","Disfruta de la luz dorada en los jardines.","Senderos del jardín"],["Cócteles sin alcohol","Comparte una bebida refrescante con amigos.","Salón del jardín"]],
[["Cena de temporada","Descubre una cocina local y creativa.","Gastronomía"],["Cena compartida","Conoce gente nueva alrededor de una mesa.","Comedor comunitario"]],
[["Música en vivo","Disfruta de un concierto íntimo.","Escenario cultural"],["Conversaciones nocturnas","Intercambia ideas con otros miembros.","Salón comunitario"]],
[["Observar las estrellas","Contempla el cielo nocturno en paz.","Zona natural"],["Noche de descanso","Termina el día leyendo tranquilamente.","Tu microaldea"]]
]};
function cnvChoicesForSlot(i,profileName,key,locale,current){
const L=locale==="fr"?"fr":locale==="es"?"es":"en";
const pools=cnvSlotPools[L]||cnvSlotPools.en;
const p=clean(profileName);
const theme=/advent|aventur|sport|explor|trek|voyag|travel|outdoor|vtt|active/.test(p)?"adventure":/art|creat|music|design|photo|artist|writer|auteur|escrit|peint/.test(p)?"creative":/nature|forest|ecolog|jardin|garden|natural|permacult|regenerat/.test(p)?"nature":/wellness|yoga|spa|senior|meditat|health|bien.tre|bienestar/.test(p)?"wellness":/social|family|famille|familia|community|connect|human|friend|amiti/.test(p)?"social":"business";
const themed={
en:{
business:[["Founder breakfast conversation","Exchange ideas over coffee before the day begins.","Dining & Gastronomy"],["Startup strategy lab","Work on an idea with other founders.","Pro Hub"],["Investor and founder roundtable","Share practical insights in a small professional group.","Business Club"],["Focused coworking session","Advance your project in a quiet workspace.","Pro Hub"],["Mentoring exchange","Discuss challenges and opportunities with peers.","Pro Hub"],["International networking evening","Connect with entrepreneurs over relaxed conversations.","Business Club"]],
adventure:[["Trail runner's warm-up","Prepare gently for the day's outdoor experiences.","Nature Trails"],["Guided mountain-bike ride","Discover the surroundings on a planned cycling route.","Activities Hub"],["Archery introduction","Practice technique and focus with an instructor.","Activities Hub"],["Tree-top adventure","Try a supervised climbing and rope course.","Adventure Area"],["Outdoor skills workshop","Learn useful skills through hands-on exploration.","Activities Hub"],["Adventure stories by the fire","Swap experiences after a day outdoors.","Community Lounge"]],
creative:[["Morning sketchbook","Capture the landscape in the soft morning light.","Creative Garden"],["Outdoor photography walk","Explore composition and natural light.","Nature Trails"],["Open-air painting studio","Create alongside other artists.","Creative Studio"],["Artist collaboration session","Develop a shared work or creative concept.","Creative Studio"],["Music and creative workshop","Explore rhythm or sound with other makers.","Cultural Hub"],["Intimate live performance","Discover musicians and artists on stage.","Cultural Stage"]],
nature:[["Birdwatching at sunrise","Observe local birds without disturbing their habitat.","Nature Trails"],["Guided biodiversity walk","Learn about plants and wildlife on protected paths.","Sanctuary"],["Food-forest discovery","Explore edible ecosystems and regenerative gardens.","Permaculture"],["Seed-saving workshop","Learn how seeds are collected and preserved.","Permaculture"],["Nature photography walk","Capture details of the landscape.","Nature Trails"],["Evening nature talk","Discuss conservation and local biodiversity.","Nature Hub"]],
wellness:[["Mindful morning breathing","Start slowly with guided breathing.","Wellness Garden"],["Gentle yoga practice","Stretch and restore your energy.","Yoga Terrace"],["Herbal garden discovery","Learn about aromatic and medicinal plants.","Wellness Garden"],["Guided relaxation session","Reconnect with your body and unwind.","Spa & Wellness"],["Sound meditation","Experience a quiet guided sound practice.","Wellness Pavilion"],["Calm evening meditation","End the day with a restorative practice.","Zen Garden"]],
social:[["Morning community coffee","Meet neighbours over a relaxed drink.","Garden Lounge"],["Small-group discovery walk","Explore the village with new friends.","Village Trails"],["Collaborative cooking workshop","Prepare seasonal food together.","Dining Workshop"],["Community games","Enjoy a friendly group challenge.","Activities Hub"],["Shared cultural experience","Join a creative or cultural group activity.","Cultural Hub"],["Music and dancing with friends","Enjoy a lively social evening.","Nightlife"]]
},
fr:{
business:[["Café des entrepreneurs","Échangez vos idées autour d'un café matinal.","Gastronomie"],["Atelier stratégie startup","Développez un projet avec d'autres fondateurs.","Pro Hub"],["Table ronde entrepreneurs","Partagez des retours d'expérience concrets.","Business Club"],["Session de coworking","Avancez sur vos projets dans un espace calme.","Pro Hub"],["Rencontre de mentorat","Échangez sur vos défis et vos opportunités.","Pro Hub"],["Networking international","Rencontrez des entrepreneurs dans une ambiance conviviale.","Business Club"]],
adventure:[["Échauffement avant la randonnée","Préparez votre corps en douceur.","Sentiers nature"],["Sortie VTT accompagnée","Découvrez les environs sur un itinéraire adapté.","Pôle activités"],["Initiation au tir à l'arc","Travaillez votre précision avec un encadrant.","Pôle activités"],["Parcours accrobranche","Explorez un parcours aérien encadré.","Parc aventure"],["Atelier de techniques nature","Apprenez des gestes utiles en plein air.","Pôle activités"],["Récits d'aventure au coin du feu","Partagez les découvertes de la journée.","Salon communautaire"]],
creative:[["Carnet de croquis matinal","Dessinez les paysages dans la lumière du matin.","Jardin créatif"],["Balade photo guidée","Explorez cadrages et lumière naturelle.","Sentiers nature"],["Atelier peinture en plein air","Créez aux côtés d'autres artistes.","Atelier créatif"],["Création collaborative","Imaginez une œuvre collective.","Atelier créatif"],["Atelier musique et création","Expérimentez rythmes et sons.","Espace culturel"],["Spectacle intimiste","Découvrez des musiciens et artistes sur scène.","Scène culturelle"]],
nature:[["Observation des oiseaux","Découvrez les oiseaux à l'aube sans les déranger.","Sentiers nature"],["Balade biodiversité","Explorez les plantes et la faune avec un guide.","Sanctuary"],["Découverte de la forêt nourricière","Visitez les jardins régénératifs.","Permaculture"],["Atelier conservation des semences","Découvrez la récolte et la conservation des graines.","Permaculture"],["Photographie de nature","Observez les détails des paysages.","Sentiers nature"],["Rencontre autour de la biodiversité","Échangez sur la protection du vivant.","Espace nature"]],
wellness:[["Respiration consciente","Commencez la journée dans le calme.","Jardin bien-être"],["Yoga doux","Retrouvez votre énergie avec des mouvements adaptés.","Terrasse yoga"],["Découverte du jardin aromatique","Explorez les plantes et leurs usages.","Jardin bien-être"],["Relaxation guidée","Détendez-vous profondément.","Spa & Bien-être"],["Méditation sonore","Découvrez une séance de sons apaisants.","Pavillon bien-être"],["Méditation du soir","Terminez la journée en douceur.","Jardin zen"]],
social:[["Café des voisins","Rencontrez les membres autour d'une boisson.","Lounge jardin"],["Balade découverte en groupe","Explorez le village avec de nouveaux amis.","Sentiers du village"],["Atelier cuisine collectif","Préparez ensemble des recettes de saison.","Atelier gastronomie"],["Jeux communautaires","Partagez un défi convivial.","Pôle activités"],["Expérience culturelle collective","Participez à une activité artistique en groupe.","Espace culturel"],["Musique et danse entre amis","Retrouvez les membres pour une soirée festive.","Nightlife"]]
},
es:{
business:[["Café de emprendedores","Intercambia ideas durante el desayuno.","Gastronomía"],["Taller de estrategia startup","Desarrolla un proyecto con otros fundadores.","Pro Hub"],["Mesa redonda de emprendedores","Comparte experiencias prácticas.","Business Club"],["Sesión de coworking","Avanza en tus proyectos en un lugar tranquilo.","Pro Hub"],["Encuentro de mentoría","Comparte desafíos y oportunidades.","Pro Hub"],["Networking internacional","Conoce emprendedores en un ambiente relajado.","Business Club"]],
adventure:[["Calentamiento antes de caminar","Prepara el cuerpo con suavidad.","Senderos naturales"],["Ruta guiada en bicicleta","Descubre el entorno sobre dos ruedas.","Zona de actividades"],["Iniciación al tiro con arco","Practica la precisión con un instructor.","Zona de actividades"],["Circuito de aventura en árboles","Explora un recorrido supervisado.","Parque de aventura"],["Taller de habilidades naturales","Aprende técnicas prácticas al aire libre.","Zona de actividades"],["Historias de aventura","Comparte experiencias al final del día.","Salón comunitario"]],
creative:[["Cuaderno de dibujo matinal","Dibuja paisajes con la luz de la mañana.","Jardín creativo"],["Paseo fotográfico","Explora encuadres y luz natural.","Senderos naturales"],["Taller de pintura al aire libre","Crea junto a otros artistas.","Taller creativo"],["Creación colaborativa","Desarrolla una obra en equipo.","Taller creativo"],["Taller de música y creación","Explora ritmos y sonidos.","Espacio cultural"],["Espectáculo íntimo","Descubre artistas y músicos en directo.","Escenario cultural"]],
nature:[["Observación de aves","Descubre las aves al amanecer sin molestarlas.","Senderos naturales"],["Paseo de biodiversidad","Conoce plantas y animales con un guía.","Sanctuary"],["Bosque comestible","Explora jardines regenerativos.","Permacultura"],["Taller de semillas","Aprende a recolectar y conservar semillas.","Permacultura"],["Fotografía de naturaleza","Captura detalles del paisaje.","Senderos naturales"],["Encuentro sobre biodiversidad","Conversa sobre la protección de la naturaleza.","Espacio natural"]],
wellness:[["Respiración consciente","Comienza el día en calma.","Jardín de bienestar"],["Yoga suave","Recupera energía con movimientos tranquilos.","Terraza de yoga"],["Jardín de plantas aromáticas","Descubre plantas y sus usos.","Jardín de bienestar"],["Relajación guiada","Disfruta de una pausa reparadora.","Spa y bienestar"],["Meditación sonora","Participa en una sesión de sonidos relajantes.","Pabellón de bienestar"],["Meditación nocturna","Termina el día con serenidad.","Jardín zen"]],
social:[["Café entre vecinos","Conoce a otros miembros durante la mañana.","Salón del jardín"],["Paseo en grupo","Explora la aldea con nuevos amigos.","Senderos"],["Taller de cocina colectiva","Prepara recetas de temporada en equipo.","Taller gastronómico"],["Juegos comunitarios","Disfruta de un reto amistoso.","Zona de actividades"],["Experiencia cultural compartida","Participa en una actividad creativa en grupo.","Espacio cultural"],["Música y baile con amigos","Disfruta de una noche festiva.","Vida nocturna"]]
}};
const schedule={business:[null,null,1,2,null,3,4,null,null,5,null],adventure:[0,null,1,2,null,null,3,null,null,5,null],creative:[0,null,1,2,null,null,3,null,null,5,null],nature:[0,null,1,2,null,null,3,null,null,5,null],wellness:[0,null,1,2,null,3,4,null,null,5,null],social:[null,null,1,2,null,null,3,null,null,5,null]};
const selected=schedule[theme][i];
const featured=selected===null?[]:[themed[L][theme][selected]];
const slot=(pools[i]||[]);
const extraTitles={
en:[["Sunrise breathing","Gentle wake-up walk","Morning reflection"],["Seasonal fruit breakfast","Breakfast with a view","Fresh juice and artisan bread"],["Guided birdwatching","Nature photography","Forest discovery"],["Permaculture practice","Natural sculpture","Team discovery"],["Chef's seasonal lunch","Garden picnic","Mediterranean lunch"],["Hammock reading","Breathwork reset","Thermal circuit"],["Seed-saving workshop","Outdoor photo studio","Cycling discovery"],["Golden-hour photography","Sunset herbal tea","Terrace conversations"],["Garden-to-table dinner","Chef's shared table","World cuisine evening"],["Open-air cinema","Storytelling circle","Acoustic concert"],["Constellation watching","Moonlit stroll","Bedtime herbal tea"]],
fr:[["Respiration au lever du soleil","Promenade douce au réveil","Réflexion matinale"],["Fruits de saison au petit-déjeuner","Petit-déjeuner panoramique","Jus frais et pain artisanal"],["Observation des oiseaux","Photographie de nature","Découverte de la forêt"],["Pratique de la permaculture","Sculpture naturelle","Découverte en équipe"],["Déjeuner de saison du chef","Pique-nique au jardin","Déjeuner méditerranéen"],["Lecture dans un hamac","Respiration guidée","Parcours thermal"],["Atelier des semences","Studio photo en plein air","Découverte à vélo"],["Photographie à l'heure dorée","Tisane au coucher du soleil","Conversations en terrasse"],["Dîner du potager","Grande table du chef","Soirée cuisines du monde"],["Cinéma en plein air","Cercle de récits","Concert acoustique"],["Observation des constellations","Balade au clair de lune","Tisane avant de dormir"]],
es:[["Respiración al amanecer","Paseo suave al despertar","Reflexión matinal"],["Fruta fresca de temporada","Desayuno panorámico","Zumo y pan artesano"],["Observación de aves","Fotografía natural","Descubrimiento del bosque"],["Práctica de permacultura","Escultura natural","Descubrimiento en equipo"],["Almuerzo de temporada del chef","Pícnic en el jardín","Almuerzo mediterráneo"],["Lectura en hamaca","Respiración guiada","Circuito termal"],["Taller de semillas","Estudio fotográfico al aire libre","Descubrimiento en bicicleta"],["Fotografía al atardecer","Infusión al atardecer","Conversaciones en la terraza"],["Cena del huerto","Mesa compartida del chef","Noche de cocina internacional"],["Cine al aire libre","Círculo de historias","Concierto acústico"],["Observar constelaciones","Paseo a la luz de la luna","Infusión antes de dormir"]]
};
const options=[...featured,...slot,...extraTitles[L][i].map((title,j)=>[title,(slot[j%slot.length]||current)[1],(slot[j%slot.length]||current)[2]])];
const unique=[],seen=new Set();
for(const e of options){if(!e||e.length!==3||seen.has(e[0]))continue;seen.add(e[0]);unique.push(e);if(unique.length===5)break;}
return unique;
}

let variation=0,last="";
function render(){const root=document.getElementById("cnv-day-experience");if(!root)return;const l=tr[lang()]||tr.en;const key=profile();const fingerprint=key+"|"+selectedProfile()+"|"+lang()+"|"+variation;if(last===fingerprint)return;last=fingerprint;const p=profiles[key];root.innerHTML="";const heading=document.createElement("h3");heading.textContent=l.title;root.appendChild(heading);const intro=document.createElement("p");intro.className="cnv-day-sub";intro.textContent=l.sub;root.appendChild(intro);const bar=document.createElement("div");bar.className="cnv-day-bar";const pill=document.createElement("span");pill.className="cnv-day-pill";pill.textContent="✧ "+(selectedProfile()||translations[lang()]?.profiles[key]||p[0]);bar.appendChild(pill);root.appendChild(bar);
const timeline=document.createElement("div");timeline.className="cnv-day-timeline";const unique=themedExperiences(selectedProfile(),key,lang(),variation);
base.forEach((entry,i)=>{let data=entry.slice();if([3,6,9].includes(i)){const v=p[[3,6,9].indexOf(i)+2];data=[p[1],...v];}if(variation%2){if(i===2)data=["trees","A mindful nature walk","Discover hidden paths and beautiful green spaces.","Nature trails"];if(i===5)data=["heart","A peaceful reset","Try gentle movement, a spa ritual or simply unwind.","Spa & Wellness"];}
const locale=translations[lang()];if(locale){const v=locale.entries[i];data=[data[0],...v];if([3,6,9].includes(i))data=[data[0],...locale.special[key][[3,6,9].indexOf(i)]];if(variation%2&&i===2)data=["trees",...locale.alternate[0]];if(variation%2&&i===5)data=["heart",...locale.alternate[1]];}if([3,6,9].includes(i))data=[data[0],...unique[[3,6,9].indexOf(i)]];const item=document.createElement("article");item.className="cnv-day-item";const clock=document.createElement("span");clock.className="cnv-day-time";clock.textContent=times[i];const symbol=document.createElement("span");symbol.className="cnv-day-icon";symbol.textContent=icons[data[0]]||"✧";const content=document.createElement("div");const h=document.createElement("h4");h.textContent=data[1];const desc=document.createElement("p");desc.textContent=data[2];const place=document.createElement("small");place.textContent="⌖ "+data[3];content.append(h,desc,place);
const langCode=lang();
const choices=cnvChoicesForSlot(i,selectedProfile(),key,langCode,data.slice(1));
if(choices.length){h.textContent=choices[0][0];desc.textContent=choices[0][1];place.textContent="⌖ "+choices[0][2];}
let choiceIndex=0;
const next=document.createElement("button");next.type="button";next.className="cnv-day-next-choice";
next.textContent=langCode==="fr"?"↻ Autre proposition":langCode==="es"?"↻ Otra propuesta":"↻ Another suggestion";
next.setAttribute("aria-label",next.textContent+" "+times[i]);
next.addEventListener("click",()=>{choiceIndex=(choiceIndex+1)%choices.length;const chosen=choices[choiceIndex];h.textContent=chosen[0];desc.textContent=chosen[1];place.textContent="⌖ "+chosen[2];});
content.appendChild(next);
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