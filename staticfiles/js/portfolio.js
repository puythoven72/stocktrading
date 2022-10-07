
 singlePortfolioTotal();
 function  singlePortfolioTotal(){
    
     let qty = document.querySelector('#stockQtyVlu');
     let current_price = document.querySelector('#current_price');
     let totStockVlu = current_price.value * qty.innerText;
     let totStockDiv = document.querySelector("#stockSymVlu");
     totStockDiv.innerHTML = ` Total Value:  $${totStockVlu.toFixed(2)} `;
 }