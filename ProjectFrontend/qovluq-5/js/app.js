

/*document.querySelector(".aboutme").onclick = function (e) {
    e.preventDefault()
    window.open('index-2.html');
location.href="index-2.html";
value='click here to visit home page';
}

let accStatus=true
let allItems=document.querySelector('.menu')
function openmenu(){
   
   if(accStatus==true){
    document.querySelector('.menu').style.display='block'
    accStatus=false
    
   }else{
    document.querySelector('.menu').style.display='none'
    accStatus=true
   
   }
}*/
let accStatus=true
document.addEventListener("click", function openMenu(){
    if(accStatus==true){
        document.querySelector('.menu').style.display='block',document.querySelector("#header-topbar").style.display='block'
        accStatus=false
        
       }else{
        document.querySelector('.menu').style.display='block', document.querySelector("#header-topbar").style.display='none'
        accStatus=true
       }

  }
  );
