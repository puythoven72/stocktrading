from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .lib.stream import OpenSocket
import alpaca_trade_api as tradeapi
from alpaca_trade_api import Stream
from .models import Stocks
from .lib.api import getstock

def home(request):
    print('in home')
    stock_info = {}
    if request.method == 'POST':
        sym = request.POST.get('symbol_search')
        print(sym)
        stock_info = getstock(sym)
    stocks = Stocks.objects.all()
    context = {'stocks' : stocks, 'stock_info' : stock_info}
    return render (request,'base/home.html',context)


def test(request,pk):
    print("IN TEST")
    stock_info = {}
    stocks = Stocks.objects.all()
    context = {'stocks' : stocks, 'stock_info' : stock_info}
    
    return render (request,'base/home.html',context)