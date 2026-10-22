(()=>{const cards=[...document.querySelectorAll('.vt-card')];if(!cards.length)return;
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
cards.forEach((c,i)=>{const b=c.querySelector('.vt-play'),m=c.querySelector('.vt-media');
b.addEventListener('click',()=>{let v=m.querySelector('video');
 if(!v){v=document.createElement('video');v.src=c.dataset.src;v.controls=true;v.playsInline=true;v.setAttribute('playsinline','');v.preload='auto';m.insertBefore(v,b);
  v.addEventListener('playing',()=>{c.classList.remove('is-loading');c.classList.add('is-live','is-playing')});
  v.addEventListener('play',()=>cards.forEach(o=>{const ov=o.querySelector('video');if(ov&&ov!==v&&!ov.paused)ov.pause()}));}
 c.classList.add('is-loading');v.muted=false;const p=v.play();if(p)p.catch(()=>{c.classList.remove('is-loading');c.classList.add('is-live','is-playing')});});
const d=c.querySelector('.vt-tr');if(d&&!rm){const s=d.querySelector('summary'),body=d.querySelector('.vt-body');
 s.addEventListener('click',e=>{e.preventDefault();if(d.dataset.busy)return;d.dataset.busy=1;const open=!d.open;if(open)d.open=true;
  const h=body.scrollHeight;const a=body.animate(open?[{height:'0px',opacity:0},{height:h+'px',opacity:1}]:[{height:h+'px',opacity:1},{height:'0px',opacity:0}],{duration:280,easing:'cubic-bezier(.2,.8,.2,1)'});
  a.onfinish=()=>{if(!open)d.open=false;delete d.dataset.busy;};});}});
if('IntersectionObserver'in window){
 const io=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target.querySelector('video');if(!e.isIntersecting&&v&&!v.paused)v.pause();}),{threshold:.2});cards.forEach(c=>io.observe(c));
 if(!rm){document.documentElement.classList.add('vt-anim');const ro=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target)}}),{threshold:.15,rootMargin:'0px 0px -8% 0px'});cards.forEach((c,i)=>{c.style.setProperty('--i',i%3);ro.observe(c)});}}
})();
