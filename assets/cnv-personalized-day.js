(function(){
"use strict";
const profiles={
creative:["Creative Explorer","palette",["Open-air art workshop","Paint, photograph or sculpt alongside other creative minds.","Creative Studio"],["Creative discoveries","Join a music, photography or artist-led experience.","Arts & Culture"],["Live music & inspiration","Discover local talent and share ideas beneath the stars.","Cultural Stage"]],
nature:["Nature Lover","leaf",["Forest bathing","A guided sensory walk beneath the trees, surrounded by birdsong.","Sanctuary"],["Permaculture discoveries","Explore edible gardens, biodiversity and regenerative practices.","Permaculture"],["Stargazing & silence","Enjoy the night sky in a peaceful nature setting.","Quiet Nature Area"]],
social:["Social Connector","users",["Meet your village","Share stories and meet inspiring people from different places.","Community Hub"],["Games & shared adventures","Join a relaxed team activity or playful group discovery.","Activities Hub"],["Music & dancing","Celebrate with new friends and an uplifting atmosphere.","Nightlife"]],
entrepreneur:["Entrepreneurial Nomad","briefcase",["Ideas that grow","Exchange ideas with founders, creators and international professionals.","Pro Hub"],["Work & connect","Choose a coworking session or join an inspiring networking conversation.","Pro Hub"],["Conversations that matter","Meet curious minds in a relaxed evening atmosphere.","Business Club"]]
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
function render(){const root=document.getElementById("cnv-day-experience");if(!root)return;const l=tr[lang()]||tr.en;const key=profile();const fingerprint=key+"|"+lang()+"|"+variation;if(last===fingerprint)return;last=fingerprint;const p=profiles[key];root.innerHTML="";const heading=document.createElement("h3");heading.textContent=l.title;root.appendChild(heading);const intro=document.createElement("p");intro.className="cnv-day-sub";intro.textContent=l.sub;root.appendChild(intro);const bar=document.createElement("div");bar.className="cnv-day-bar";const pill=document.createElement("span");pill.className="cnv-day-pill";pill.textContent="✧ "+p[0];bar.appendChild(pill);const btn=document.createElement("button");btn.type="button";btn.textContent="↻ "+l.again;btn.addEventListener("click",()=>{variation++;last="";render()});bar.appendChild(btn);root.appendChild(bar);
const timeline=document.createElement("div");timeline.className="cnv-day-timeline";
base.forEach((entry,i)=>{let data=entry.slice();if([3,6,9].includes(i)){const v=p[[3,6,9].indexOf(i)+2];data=[p[1],...v];}if(variation%2){if(i===2)data=["trees","A mindful nature walk","Discover hidden paths and beautiful green spaces.","Nature trails"];if(i===5)data=["heart","A peaceful reset","Try gentle movement, a spa ritual or simply unwind.","Spa & Wellness"];}
const item=document.createElement("article");item.className="cnv-day-item";const clock=document.createElement("span");clock.className="cnv-day-time";clock.textContent=times[i];const symbol=document.createElement("span");symbol.className="cnv-day-icon";symbol.textContent=icons[data[0]]||"✧";const content=document.createElement("div");const h=document.createElement("h4");h.textContent=data[1];const desc=document.createElement("p");desc.textContent=data[2];const place=document.createElement("small");place.textContent="⌖ "+data[3];content.append(h,desc,place);item.append(clock,symbol,content);timeline.appendChild(item);});root.appendChild(timeline);const foot=document.createElement("p");foot.className="cnv-day-foot";foot.textContent="✧ "+l.note;root.appendChild(foot);}
function init(){
if(document.getElementById("cnv-day-experience"))return;
const art=document.getElementById("artoflife"),life=document.getElementById("life");
if(!art)return;
const root=document.createElement("div");root.id="cnv-day-experience";root.className="cnv-day-experience";
const charter=art.querySelector(".cnv-charter-cta");if(charter)art.insertBefore(root,charter);else art.appendChild(root);
if(life)life.style.display="none";
render();
document.addEventListener("change",()=>{last="";render()},true);
document.addEventListener("click",e=>{if(e.target.closest("#cnv-day-experience"))return;setTimeout(()=>{last="";render()},120)},true);
new MutationObserver(()=>{if((tr[lang()]||tr.en).title!==root.querySelector("h3")?.textContent){last="";render()}}).observe(document.documentElement,{attributes:true,attributeFilter:["lang"]});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();