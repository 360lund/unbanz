(()=>{const cards=document.querySelectorAll('.vt-card');if(!cards.length)return;
const stopOthers=(me)=>document.querySelectorAll('.vt-card video').forEach(v=>{if(v!==me&&!v.paused)v.pause()});
cards.forEach(c=>{const b=c.querySelector('.vt-play'),m=c.querySelector('.vt-media');b.addEventListener('click',()=>{let v=m.querySelector('video');
if(!v){v=document.createElement('video');v.src=c.dataset.src;v.poster=c.dataset.poster;v.controls=true;v.playsInline=true;v.setAttribute('playsinline','');v.preload='auto';m.appendChild(v);v.addEventListener('play',()=>stopOthers(v));}
c.classList.add('is-playing');v.muted=false;v.play().catch(()=>{});v.focus();});});
if('IntersectionObserver'in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting){const v=e.target.querySelector('video');if(v&&!v.paused)v.pause();}}),{threshold:.2});cards.forEach(c=>io.observe(c));}})();
