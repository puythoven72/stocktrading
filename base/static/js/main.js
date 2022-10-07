
var radios=document.getElementsByName("stock_choice");

if (radios) {
    for (var i = 0, max = radios.length; i < max; i++) {
        let crnt = document.querySelector('#crnt_' + radios[i].id);
        if (crnt.innerHTML == '!') {
            radios[i].disabled = true;
        }
        else {
            radios[i].onclick = getStockTotal;
        }
    }
};

function getStockTotal() {

    let qty = document.querySelector('#qty_' + this.id);
    let vlu = document.querySelector('#crnt_' + this.id);
    let sym = document.querySelector('#sym' + this.id);
    let totStockVlu = qty.innerHTML * vlu.innerHTML;
    let totStockDiv = document.querySelector("#stockSymVlu");
    totStockDiv.innerHTML = `${sym.innerHTML} Total Value:  $${totStockVlu.toFixed(2)} `;

}

