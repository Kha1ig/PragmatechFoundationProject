
/*left.addEventListener('click', function (){
    document.querySelector('.box').scrollTo(0,30)
})*/
/*function prev() {
    var val = (parseInt(document.querySelector('.box').style.left, 10) || 0) - 50;
    document.querySelector('.box').style.left = val + 'px';
}*/

/*function Left() {
    moveleft.style.left = parseInt(moveleft.style.left) - 5 + "px";
}*/
var box = document.querySelector(".box");
var container = document.querySelector(".container");

let up2 = 1;
let right2 = 1;
let left2 = 1;
let down2 = 1;

function up() {
  box.style.height = 30 + "px";
  box.style.bottom = 30 * up2 + "px";
  up2++;
}

function right() {
  box.style.right = 30 + "px";
  box.style.right = 30 * right2 + "px";
  right2++;
}

function left() {
  box.style.left = 30 + "px";
  box.style.left = 30 * left2 + "px";
  left2++;
}

function down() {
  box.style.bottom = 30 + "px";
  box.style.top = 30 * down2 + "px";
  down2++;
}
