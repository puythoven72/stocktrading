from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .lib.stream import OpenSocket
import alpaca_trade_api as tradeapi
from alpaca_trade_api import Stream
from .models import Stocks
from .lib.api import getstock,get_portfolio_current_val
import datetime


def home(request):
    stock_info = {}

    #stocks = Stocks.objects.all()
   
    stock_dict= list(Stocks.objects.values())
    current_portfolio_prices = get_portfolio_current_val()


    for p in stock_dict:
        current_sym = p['symbol']
        p["current"] = current_portfolio_prices[current_sym]
  
  
    if request.method == 'POST' and 'search_btn' in request.POST:
        sym = request.POST.get('symbol_search')
        print(sym)
        stock_info = getstock(sym)
        #stock_buy = stock_info
        print(stock_info)
        context = {'stocks' : stock_dict, 'stock_info' : stock_info}
        
        return render (request,'base/home.html',context)
   
    # if request.method == 'POST' and 'buy_btn' in request.POST:
    #     print(request.POST['current_price'] + "is current price")
    #     currentPrice = request.POST['current_price']

    #     stock=Stocks()
    #     stock.symbol = request.POST.get('symbol')
    #     stock.value = request.POST.get('current_price')
    #     stock.quantity = request.POST.get('quantity')
    #     stock.stockbuydate = datetime.datetime.now()
    #     stock.save()
       

    #     context = {'stocks' : stocks, 'stock_info' : stock_info}
    #     #return redirect('home', stock_info)
    #     return render (request,'base/success.html')
  
    
    #x = Stocks.objects.all().values_list('symbol', flat=True).distinct()
    #print(x )
    # for y in x:
    #     print('whats happenin')
    #     print(y)
    #     lookup = getstock(y)
    #     print(lookup['currentPrice'] )
    #     current_price_dict = {lookup['symbol'] : lookup['currentPrice']}

   


    context = {'stocks' : stock_dict, 'stock_info' : stock_info}
    return render (request,'base/home.html',context)

def success(request):
    if request.method == 'POST' and 'buy_btn' in request.POST:
        qty = request.POST.get('quantity')
        print(qty)
        if qty != "" and int(qty) > 0:
            print(qty)
            stock=Stocks()
            stock.symbol = request.POST.get('symbol')
            stock.value = request.POST.get('current_price')
            stock.quantity = qty
            stock.stockbuydate = datetime.datetime.now()
            stock.save()
        

       # context = {'stocks' : stocks, 'stock_info' : stock_info}
        #return redirect('home', stock_info)
        return redirect('home')

    