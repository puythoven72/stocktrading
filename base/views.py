from django.shortcuts import render,redirect
from .models import Stocks,User
from .lib.api import getstock,get_all_tot_qty,save_action,get_stk_qty,get_user_amt,save_user_amt
from django.contrib import messages

def reset_account(request):
    reset_vlu = float(1000) 
    if not save_user_amt('reset',reset_vlu):
        messages.error(request,'Error Saving reset amt. Call Administrator!')
    return redirect('home')

def home(request):
    stock_info = {}
    all_stocks = get_all_tot_qty()
    amt = get_user_amt()
    
    if request.method == 'POST' and 'search_btn' in request.POST:
        
        sym = request.POST.get('symbol_search')
        if sym != "":
            stock_info = getstock(sym)
            context = { 'stock_info' : stock_info ,'all_stocks' : all_stocks,'user_amt': amt}
            return render (request,'base/home.html',context)
        else:
            messages.error(request,'Please Enter A Valid Search Criteria')        
            return redirect('home')

    if request.method == 'POST' and 'snapshot_btn' in request.POST:
        all_stocks = get_all_tot_qty(True)
        context = { 'stock_info' : stock_info ,'all_stocks' : all_stocks,'disp_current_price' : 'true', 'user_amt': amt}
        return render (request,'base/home.html',context)

   
    context = { 'all_stocks' : all_stocks, 'user_amt': amt}
    return render (request,'base/home.html',context)

def success(request):
    amt = get_user_amt()
    if request.method == 'POST' and 'buy_btn' in request.POST :
        qty = request.POST.get('quantity')
        if(qty == "" or int(qty) < 0 ):
            qty = 0
        symbol = request.POST.get('symbol')
        current_price = request.POST.get('current_price')
        action = "Buy"
        
        current_buy = (float(current_price) * float(qty)) 
        print(current_buy)
        if(float(amt) < float(current_buy)):
             messages.error(request,'Funds less then Buy Price') 
             return redirect('home')

        if not save_action(symbol,qty,current_price,action):
            messages.error(request,'Please Enter A Valid Stock')
        if not save_user_amt(action,current_buy):
            messages.error(request,'Error Saving User Amt. Call Administrator!')        
        
    return redirect('home')
    


def shareinfo(request,symbol):
    amt = get_user_amt()
    stock_shares = Stocks.objects.filter(symbol=symbol)
    stock_info = getstock(symbol)
    stock_quant = get_stk_qty(symbol)
    context={'stocks': stock_shares, 'stock_info' : stock_info,'user_amt': amt,'stock_quant':stock_quant}
    return render (request,'base/stock_information.html',context )

def history(request):
    amt = get_user_amt()
    stocks = Stocks.objects.all()
    context={'stocks' : stocks , 'user_amt': amt}
    return render (request,'base/portfolio_history.html',context)



def sell_stock(request,symbol):
    
    if request.method == 'POST' and 'sell_btn' in request.POST :
       
        current_stck_qty = get_stk_qty(symbol)
        qty = request.POST.get('quantity')
        if(qty == "" or int(qty) < 0 ):
            qty = 0
        current_price = request.POST.get('current_price')
        current_sell = (float(current_price) * float(qty)) 
        action = "Sell"
        if (int(qty) > int(current_stck_qty)):
             messages.error(request,'Sell Qty greater Than Amt Owned!') 
             return redirect('shareinfo', symbol = symbol)

        if not save_action(symbol,qty,current_price,action):
            messages.error(request,'Please Enter A Valid Stock, or Qty')  
        if not save_user_amt(action,current_sell):
            messages.error(request,'Error Saving User Amt. Call Administrator!')
        
    return redirect('shareinfo', symbol = symbol)



    