from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .lib.stream import OpenSocket
import alpaca_trade_api as tradeapi
from alpaca_trade_api import Stream
from .models import Stocks
from .lib.api import getstock,add_current_price
import datetime


def home(request):
    stock_info = {}

    stock_dict= list(Stocks.objects.values())
    updated_stock = add_current_price(stock_dict)
   
  
    if request.method == 'POST' and 'search_btn' in request.POST:
        sym = request.POST.get('symbol_search')
        print(sym)
        stock_info = getstock(sym)
        context = {'stocks' : updated_stock, 'stock_info' : stock_info}
        return render (request,'base/home.html',context)
   
    context = {'stocks' : updated_stock, 'stock_info' : stock_info}
    return render (request,'base/home.html',context)

def success(request):
    if request.method == 'POST' and 'buy_btn' in request.POST:
        qty = request.POST.get('quantity')
       
        if qty != "" and int(qty) > 0:
          
            stock=Stocks()
            stock.symbol = request.POST.get('symbol')
            stock.value = request.POST.get('current_price')
            stock.quantity = qty
            stock.stockbuydate = datetime.datetime.now()
            stock.save()
      
            return redirect('home')

    