'use strict';
const $ = s => document.querySelector(s);
const seed = [
 {id:1,name:'Alex Morgan',handle:'@alex.example',email:'alex@example.com',phone:'Not provided',service:'Instagram unban',status:'New',date:'Today',message:'Demo request: my account was disabled yesterday. I would like a case review.'},
 {id:2,name:'Maya Chen',handle:'@studio.example',email:'maya@example.com',phone:'Not provided',service:'Instagram username claim',status:'New',date:'Today',message:'Demo request: looking into a username for a studio brand.'},
 {id:3,name:'Omar Ali',handle:'Example ad account',email:'omar@example.com',phone:'Not provided',service:'Ad account unban',status:'In progress',date:'Yesterday',message:'Demo request: business advertising access is restricted.'},
 {id:4,name:'Sofia Reed',handle:'@sofia.example',email:'sofia@example.com',phone:'Not provided',service:'Facebook unban',status:'In progress',date:'Yesterday',message:'Demo request: help with a disabled Facebook profile.'},
 {id:5,name:'Noah Park',handle:'@noah.example',email:'noah@example.com',phone:'Not provided',service:'Impersonation report',status:'New',date:'Yesterday',message:'Demo request: another account is impersonating my business.'},
 {id:6,name:'Amira Khan',handle:'@amira.example',email:'amira@example.com',phone:'Not provided',service:'Instagram username claim',status:'Closed',date:'2 days ago',message:'Demo request: checking a name for a new profile.'},
 {id:7,name:'Ethan Cole',handle:'Example business',email:'ethan@example.com',phone:'Not provided',service:'Page access',status:'In progress',date:'2 days ago',message:'Demo request: lost access to a business Page.'},
 {id:8,name:'Leila Hassan',handle:'@leila.example',email:'leila@example.com',phone:'Not provided',service:'Instagram unban',status:'Closed',date:'3 days ago',message:'Demo request: recovery of a disabled account.'}
];
let leads=structuredClone(seed),filter='All',selected=null,lastFocus=null;
function initials(name){return name.split(' ').map(x=>x[0]).slice(0,2).join('');}
$('#show-password').addEventListener('click',()=>{const input=$('#password');input.type=input.type==='password'?'text':'password';$('#show-password').textContent=input.type==='password'?'Show':'Hide';});
$('#login-form').addEventListener('submit',e=>{e.preventDefault();if($('#password').value!=='preview'){$('#login-error').textContent='Use preview to explore the design.';return;}$('#login').hidden=true;$('#workspace').hidden=false;$('#password').value='';render();});
$('#logout').addEventListener('click',()=>{$('#workspace').hidden=true;$('#login').hidden=false;$('#login-error').textContent='';$('#password').focus();});
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{filter=button.dataset.filter;render();}));
$('#search').addEventListener('input',render);
$('#reset-demo').addEventListener('click',()=>{leads=structuredClone(seed);filter='All';$('#search').value='';render();});
function render(){
 $('#total-count').textContent=leads.length;$('#side-count').textContent=leads.length;
 $('#new-count').textContent=leads.filter(x=>x.status==='New').length;$('#progress-count').textContent=leads.filter(x=>x.status==='In progress').length;$('#closed-count').textContent=leads.filter(x=>x.status==='Closed').length;
 document.querySelectorAll('[data-filter]').forEach(b=>{const active=b.dataset.filter===filter;b.classList.toggle(b.classList.contains('nav-item')?'active':'selected',active);b.setAttribute('aria-pressed',String(active));});
 const q=$('#search').value.toLowerCase().trim();const visible=leads.filter(x=>(filter==='All'||x.status===filter)&&[x.name,x.handle,x.service].join(' ').toLowerCase().includes(q));
 $('#visible-count').textContent=visible.length;$('#empty').hidden=visible.length>0;
 $('#lead-list').replaceChildren(...visible.map(lead=>{const b=document.createElement('button');b.className='lead-row';b.setAttribute('aria-label',`View ${lead.name}, ${lead.service}, ${lead.status}`);b.innerHTML='<span class="person"><span class="avatar"></span><span><strong></strong><small></small></span></span><span class="lead-service"></span><span class="status"></span><span class="lead-date"></span>';b.querySelector('.avatar').textContent=initials(lead.name);b.querySelector('strong').textContent=lead.name;b.querySelector('small').textContent=lead.handle;b.querySelector('.lead-service').textContent=lead.service;const status=b.querySelector('.status');status.textContent=lead.status;status.classList.toggle('progress',lead.status==='In progress');status.classList.toggle('closed',lead.status==='Closed');b.querySelector('.lead-date').textContent=lead.date;b.addEventListener('click',()=>openLead(lead));return b;}));
}
function openLead(lead){selected=lead;lastFocus=document.activeElement;$('#lead-title').textContent=lead.name;$('#detail-avatar').textContent=initials(lead.name);$('#detail-handle').textContent=lead.handle;for(const key of ['service','date','email','phone','message'])$('#detail-'+key).textContent=lead[key];$('#lead-status').value=lead.status;$('#lead-note').value=lead.note||'';$('#save-status').textContent='';$('#lead-dialog').showModal();document.body.style.overflow='hidden';}
$('#close-detail').addEventListener('click',()=>$('#lead-dialog').close());
$('#lead-dialog').addEventListener('close',()=>{document.body.style.overflow='';if (lastFocus?.isConnected) lastFocus.focus(); else $('#search').focus();});
$('#lead-edit').addEventListener('submit',e=>{e.preventDefault();selected.status=$('#lead-status').value;selected.note=$('#lead-note').value;render();$('#save-status').textContent='Demo changes saved for this session.';});
