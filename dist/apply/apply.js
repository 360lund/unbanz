'use strict';
const $=s=>document.querySelector(s);
const form=$('#application-form'),application=$('.application');
const narrow=matchMedia('(max-width:900px)');
let step=1;
const selectedService=new URLSearchParams(location.search).get('service');
if([...$('#service-select').options].some(option=>option.value===selectedService))$('#service-select').value=selectedService;
function showStep(next){
 step=next;application.dataset.step=String(step);
 $('#step-count').textContent=step+' of 2';$('#step-name').textContent=step===1?'The account':'Your details';
 $('#account-section').inert=narrow.matches&&step!==1;
 $('#contact-section').inert=narrow.matches&&step!==2;
 $('#form-title').innerHTML=narrow.matches&&step===2?'Where can we<br>reach you?':'A few details.<br>We’ll take a look.';
 if(narrow.matches&&!matchMedia('(prefers-reduced-motion:reduce)').matches){const section=$(step===1?'#account-section':'#contact-section');section.animate([{opacity:0,transform:'translateY(8px)'},{opacity:1,transform:'translateY(0)'}],{duration:280,easing:'cubic-bezier(.2,.7,.2,1)'});}
}
function validate(fields){
 for(const id of fields){const input=$(id);input.setCustomValidity('');if(input.required&&!input.value.trim())input.setCustomValidity('Please fill in this field.');if(id==='#account-input'&&input.value.trim().length<2)input.setCustomValidity('Enter your username or account link.');const valid=input.checkValidity();input.setAttribute('aria-invalid',String(!valid));if(!valid){input.reportValidity();return false;}}
 return true;
}
$('#next-step').addEventListener('click',()=>{if(validate(['#account-input'])){showStep(2);window.scrollTo({top:0,behavior:'auto'});}});
$('#back-step').addEventListener('click',()=>{showStep(1);window.scrollTo({top:0,behavior:'auto'});});
narrow.addEventListener('change',()=>showStep(step));
form.querySelectorAll('input,textarea').forEach(input=>input.addEventListener('input',()=>{input.setCustomValidity('');input.removeAttribute('aria-invalid');}));
function data(){return{service:$('#service-select').value,account:$('#account-input').value.trim(),details:$('#details-input').value.trim(),name:$('#name-input').value.trim(),email:$('#email-input').value.trim(),phone:$('#phone-input').value.trim(),company:$('#company-input').value};}
form.addEventListener('submit',async event=>{
 event.preventDefault();
 if(narrow.matches&&step===1){$('#next-step').click();return;}
 if(!$('#account-input').value.trim()){showStep(1);validate(['#account-input']);return;}
 if(!validate(['#account-input','#name-input','#email-input']))return;
 const button=$('#submit-application'),status=$('#application-status');button.disabled=true;$('#submit-label').textContent='Sending…';status.hidden=true;$('#submission-help').hidden=true;
 try{
  // Firebase can replace this endpoint without changing the application design.
  const response=await fetch('/api/application',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data()),signal:AbortSignal.timeout(15000)});
  const result=await response.json();if(!response.ok||!result.accepted)throw new Error('Submission unavailable');
  status.textContent='Your request has been received. We’ll reply to your email.';form.reset();showStep(1);
 }catch{
  status.textContent='Your request couldn’t be submitted. Your details are still here—try again or contact us below.';$('#submission-help').hidden=false;
 }finally{status.hidden=false;button.disabled=false;$('#submit-label').textContent='Send my request';}
});
$('#whatsapp-alternative').addEventListener('click',()=>{const d=data();const message=`Hi Unbanz,\n\nService: ${d.service}\nAccount: ${d.account}\nName: ${d.name}\nEmail: ${d.email}\nPhone: ${d.phone}\nDetails: ${d.details}`;location.assign('https://wa.me/19342012490?text='+encodeURIComponent(message));});
showStep(1);
