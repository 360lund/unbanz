(()=>{const cards=[...document.querySelectorAll('.vt-card')];if(!cards.length)return;
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
const P='M7 4.5v15l12-7.5z',PA='M6 4.5h4.2v15H6zm7.8 0H18v15h-4.2z';
const svg=(d,c)=>`<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"${c?` class="${c}"`:''}><path fill="currentColor" d="${d}"/></svg>`;
const MUTE_OFF='M4 9v6h4l5 4V5L8 9zm12.5 3a4.5 4.5 0 0 0-2.5-4v8a4.5 4.5 0 0 0 2.5-4z',MUTE_ON='M4 9v6h4l5 4V5L8 9zm16.6.4-1.4-1.4L17 10.2 14.8 8l-1.4 1.4 2.2 2.2-2.2 2.2 1.4 1.4 2.2-2.2 2.2 2.2 1.4-1.4-2.2-2.2z';
const FS='M4 9V4h5v2H6v3zm11-5h5v5h-2V6h-3zM6 15v3h3v2H4v-5zm12 3v-3h2v5h-5v-2z';
let active=null;
function setup(c){if(c._v)return c._v;const m=c.querySelector('.vt-media'),b=c.querySelector('.vt-play');
 const v=document.createElement('video');v.preload='metadata';v.playsInline=true;v.setAttribute('playsinline','');v.setAttribute('webkit-playsinline','');v.disablePictureInPicture=true;v.poster=m.querySelector('img').currentSrc||m.querySelector('img').src;v.src=c.dataset.src;m.insertBefore(v,b);
 m.insertAdjacentHTML('beforeend',`<button class="vt-tap" type="button" aria-label="Play or pause"></button><span class="vt-center" aria-hidden="true">${svg(P)}</span><span class="vt-spin" aria-hidden="true"></span><div class="vt-ctl"><button class="vt-pp" type="button" aria-label="Pause"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="${PA}"/></svg></button><div class="vt-bar" role="slider" aria-label="Seek" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" tabindex="0"><i></i></div><button class="vt-mute" type="button" aria-label="Mute">${svg(MUTE_OFF,'off')}${svg(MUTE_ON,'on')}</button><button class="vt-fs" type="button" aria-label="Full screen">${svg(FS)}</button></div>`);
 const pp=m.querySelector('.vt-pp'),ppath=pp.querySelector('path'),bar=m.querySelector('.vt-bar'),fill=bar.firstChild;
 let raf=0,hide=0,buf=0;
 const tick=()=>{if(v.duration){const r=v.currentTime/v.duration;fill.style.transform=`scaleX(${r})`;bar.setAttribute('aria-valuenow',Math.round(r*100));}raf=v.paused?0:requestAnimationFrame(tick)};
 const showCtl=()=>{c.classList.add('show-ctl');clearTimeout(hide);hide=setTimeout(()=>{if(!v.paused)c.classList.remove('show-ctl')},2200)};
 const icon=(playing)=>{ppath.setAttribute('d',playing?PA:P);pp.setAttribute('aria-label',playing?'Pause':'Play')};
 v.addEventListener('playing',()=>{clearTimeout(buf);c.classList.remove('is-buffering','is-ended','is-paused');c.classList.add('is-live');icon(true);if(!raf)raf=requestAnimationFrame(tick)});
 v.addEventListener('waiting',()=>{clearTimeout(buf);buf=setTimeout(()=>c.classList.add('is-buffering'),300)});
 v.addEventListener('pause',()=>{clearTimeout(buf);c.classList.remove('is-buffering');if(!v.ended){c.classList.add('is-paused');icon(false)}tick()});
 v.addEventListener('ended',()=>{c.classList.remove('is-live','is-started','is-paused','show-ctl');c.classList.add('is-ended');icon(false);setTimeout(()=>{v.currentTime=0;fill.style.transform='scaleX(0)'},500)});
 v.addEventListener('volumechange',()=>c.classList.toggle('is-muted',v.muted));
 const toggle=()=>{if(v.paused)play(c);else v.pause();showCtl()};
 m.querySelector('.vt-tap').addEventListener('click',toggle);pp.addEventListener('click',toggle);
 m.addEventListener('pointermove',()=>{if(c.classList.contains('is-started'))showCtl()});
 m.querySelector('.vt-mute').addEventListener('click',()=>{v.muted=!v.muted;showCtl()});
 m.querySelector('.vt-fs').addEventListener('click',()=>{if(document.fullscreenElement)return document.exitFullscreen();if(m.requestFullscreen)m.requestFullscreen().catch(()=>{});else if(v.webkitEnterFullscreen)v.webkitEnterFullscreen()});
 const seek=(x)=>{const r=bar.getBoundingClientRect();if(v.duration){v.currentTime=Math.max(0,Math.min(1,(x-r.left)/r.width))*v.duration;tick()}showCtl()};
 bar.addEventListener('click',e=>seek(e.clientX));
 bar.addEventListener('keydown',e=>{if(!v.duration)return;if(e.key==='ArrowRight')v.currentTime=Math.min(v.duration,v.currentTime+2);else if(e.key==='ArrowLeft')v.currentTime=Math.max(0,v.currentTime-2);else return;e.preventDefault();tick()});
 return c._v=v;}
function warm(c){const v=setup(c);if(v.preload!=='auto'){v.preload='auto';}}
function play(c){const v=setup(c);if(active&&active!==c&&active._v&&!active._v.paused)active._v.pause();active=c;
 c.classList.add('is-started','show-ctl');c.classList.remove('is-ended');v.muted=false;
 const p=v.play();if(p)p.catch(()=>{v.muted=true;v.play().catch(()=>c.classList.add('is-paused'))});}
cards.forEach(c=>{const b=c.querySelector('.vt-play'),m=c.querySelector('.vt-media');
 b.addEventListener('click',()=>play(c));
 ['pointerenter','touchstart','focusin'].forEach(ev=>m.addEventListener(ev,()=>warm(c),{passive:true,once:true}));
 const d=c.querySelector('.vt-tr');if(d&&!rm){const s=d.querySelector('summary'),body=d.querySelector('.vt-body');
  s.addEventListener('click',e=>{e.preventDefault();if(d.dataset.busy)return;d.dataset.busy=1;const open=!d.open;if(open)d.open=true;
   const h=body.scrollHeight;const a=body.animate(open?[{height:'0px',opacity:0},{height:h+'px',opacity:1}]:[{height:h+'px',opacity:1},{height:'0px',opacity:0}],{duration:280,easing:'cubic-bezier(.2,.8,.2,1)'});
   a.onfinish=()=>{if(!open)d.open=false;delete d.dataset.busy;};});}});
if('IntersectionObserver'in window){
 const near=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){setup(e.target);near.unobserve(e.target)}}),{rootMargin:'300px 0px'});
 const vis=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target._v;if(!e.isIntersecting&&v&&!v.paused)v.pause();}),{threshold:.2});
 cards.forEach(c=>{near.observe(c);vis.observe(c)});
 if(!rm){document.documentElement.classList.add('vt-anim');const ro=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target)}}),{threshold:.15,rootMargin:'0px 0px -8% 0px'});cards.forEach((c,i)=>{c.style.setProperty('--i',i%3);ro.observe(c)});}}
else cards.forEach(setup);
})();
