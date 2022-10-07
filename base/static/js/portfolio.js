
// document.getElementById("sell_btn").addEventListener("click", disable_on_click);
// document.getElementById("sell-form").addEventListener("submit", function(e){
//     var element = document.getElementById('sell_btn');
//     element.setAttribute("disabled", "disabled");
//   	//do whatever an submit the form
// });



 singlePortfolioTotal();
 function  singlePortfolioTotal(){
    
     let qty = document.querySelector('#stockQtyVlu');
     let current_price = document.querySelector('#current_price');
     let totStockVlu = current_price.value * qty.innerText;
     let totStockDiv = document.querySelector("#stockSymVlu");
     totStockDiv.innerHTML = ` Total Value:  $${totStockVlu.toFixed(2)} `;
 }

 function disable_on_click() {
    var element = document.getElementById('sell_btn');
    element.setAttribute("disabled", "disabled");
  }