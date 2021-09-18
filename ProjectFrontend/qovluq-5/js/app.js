

/*document.querySelector(".aboutme").onclick = function (e) {
    e.preventDefault()
    window.open('index-2.html');
location.href="index-2.html";
value='click here to visit home page';
}*/

let accStatus=true
let allItems=document.querySelector('.menu')
function myFunction(el){
   
   if(accStatus==true){
    el.nextElementSibling.style.display='none'
    accStatus=false
    
   }else{
    el.nextElementSibling.style.display='block'
    accStatus=true
   
   }
}
document.querySelector("#header-topbar")