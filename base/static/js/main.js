var radios = document.forms["portfolio"].elements["stock_choice"];

if(radios){
    for (var i = 0, max = radios.length; i < max; i++) {
        radios[i].onclick = getStockTotal;
    }
};

function getStockTotal() {

    let qty = document.querySelector('#qty_' + this.id);
    let vlu = document.querySelector('#vlu_' + this.id);
    let sym = document.querySelector('#sym' + this.id);
    let dte = document.querySelector('#dte_' + this.id);

    let totStockVlu = qty.innerHTML * vlu.innerHTML;

    let totStockDiv = document.querySelector("#stockSymVlu");
    totStockDiv.innerHTML = `${sym.innerHTML} Total Value:  $${totStockVlu} On ${dte.innerHTML}`;


}