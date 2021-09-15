
let btn = document.createElement("button");
btn.innerHTML = "Submit";

document.body.appendChild(btn);

document.querySelector(".box").appendChild(btn);
/*btn.onclick.document.querySelector('.box').style.bacground='red'*/

let yuxari=0
btn.addEventListener("click", function() {
    document.querySelector('.box').style.background='blue';
    yuxari+=5
    btn.style.marginBottom=`${yuxari}px`

  });