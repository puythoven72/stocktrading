from django.shortcuts import render,redirect
from .models import Stocks
from .lib.api import getstock,get_tot_qty
import datetime
from django.contrib import messages


def home(request):
    stock_info = {}
    all_stocks = get_tot_qty()
  
    if request.method == 'POST' and 'search_btn' in request.POST:
        
        sym = request.POST.get('symbol_search')
        if sym != "":
            stock_info = getstock(sym)
            context = { 'stock_info' : stock_info ,'all_stocks' : all_stocks}
            return render (request,'base/home.html',context)
        else:
            messages.error(request,'Please Enter A Valid Search Criteria')        
            return redirect('home')


    if request.method == 'POST' and 'snapshot_btn' in request.POST:
        all_stocks = get_tot_qty(True)
        context = { 'stock_info' : stock_info ,'all_stocks' : all_stocks,'disp_current_price' : 'true'}
        return render (request,'base/home.html',context)
   
    context = { 'all_stocks' : all_stocks}
    return render (request,'base/home.html',context)

def success(request):
    if request.method == 'POST' and 'buy_btn' in request.POST :
        qty = request.POST.get('quantity')
       
        if qty != "" and int(qty) > 0 and request.POST.get('current_price') != "":
          
            stock=Stocks()
            stock.symbol = request.POST.get('symbol')
            stock.value = request.POST.get('current_price')
            stock.quantity = qty
            stock.stockbuydate = datetime.datetime.now()
            stock.save()
        else:
            messages.error(request,'Please Enter A Valid Stock')        
      
    return redirect('home')
    


def shareinfo(request,symbol):
    
    stock_shares = Stocks.objects.filter(symbol=symbol)
    stock_info = getstock(symbol)

    context={'stocks': stock_shares, 'stock_info' : stock_info}
    return render (request,'base/stock_information.html',context)

def history(request):
    stocks = Stocks.objects.all()
    context={'stocks' : stocks}
    return render (request,'base/portfolio_history.html',context)




   
    