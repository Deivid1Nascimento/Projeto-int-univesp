(function(win,doc) {
'use strict';

if(doc.querySelector('.btnDel')){
let btnDel = doc.querySelectorAll('.btnDel');
for(let i=0; i < btnDel.length; i++){
btnDel[i].addEventListener('click', function(event){
if(confirm('Tem certeza que deseja apagar esse dado?')){
return true;
}else{
event.preventDefault();}
});
}
}
if(doc.querySelector('#form')){
let form=doc.querySelector('#form');
function sendForm(event)
{
event.preventDefault();
let data = new FormData(form);
let ajax = new XMLHttpRequest();
let token = doc.querySelectorAll('input')[0].value;
ajax.open('POST', form.action );
ajax.setRequestHeader('X_CSRF_TOKEN', token);
ajax.onreadystatechange = function(){
if(ajax.status === 200 && ajax.readyState === 4){
let result = doc.querySelector('#result');
result.innerHTML = 'Cadastrado com sucesso!'
result.classList.add('alert');
result.classList.add('alert-sucess');
}
}
ajax.send(data);
form.reset();
}
form.addEventListener('submit', sendForm, false);
}
})(window,document);

$(document).ready(function(){
$(".menu-button").click(function(){
$(".menu-bar").toggleClass( "open" );
})
})