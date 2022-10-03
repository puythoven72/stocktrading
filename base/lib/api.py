
from re import T
from .stream_config import api_key,api_secret,base_url
from django.http import HttpResponse
import json
import alpaca_trade_api as tradeapi
from alpaca_trade_api import Stream
import yfinance as yf
from .api_helper import format_values
from ..models import Stocks
from datetime import date


def getstock(symbol):
    msft = yf.Ticker(symbol)
  
    raw_json = json.dumps(msft.info)

    stock_data = json.loads(raw_json)

    return format_values(stock_data)


def add_current_price(stock_dict):
    current_portfolio_prices = get_portfolio_current_val()
    for stk in stock_dict:
        current_sym = stk['symbol']
        stk["current"] = current_portfolio_prices[current_sym]
    return stock_dict


         
def get_portfolio_current_val():
    symbol_list = Stocks.objects.all().values_list('symbol', flat=True).distinct()
    current_price_dict = {}

    for symbol in symbol_list:
        lookup = getstock(symbol)
        current_price_dict[lookup['symbol']] =  lookup['currentPrice']
    return current_price_dict




def get_tot_qty(get_current_price = False):
  
    stock_data_list = []
    symbol_list = Stocks.objects.all().values_list('symbol', flat=True).distinct()
    
    count = 0
    for sym in symbol_list:
        count += 1
        stock_data = {}
        if get_current_price:
            lookup = getstock(sym)
            stock_data['current_price'] = lookup['currentPrice']
        else:
            stock_data['current_price'] = '!'
        mydata = Stocks.objects.filter(symbol= sym).values()
        total_Quant = 0

        for data in mydata:
            total_Quant = total_Quant + data['quantity']
            
        stock_data['symbol'] = sym
        stock_data['tot_quant'] = total_Quant
        stock_data['id'] = count
        stock_data_list.append(stock_data)
    return stock_data_list



    # #quotes = api.get_quotes(symbol, limit=10)
    # quotes = api.get_trades(symbol, limit=10)
    # #quotes = api.get_trades(symbol, limit = 10).df
    # # quotes = api.get_quotes(symbol, limit = 10).df
    # print(quotes)
    # # for quote in quotes:
    # #     print(quote.p)

    # # gme_snapshot = api.list_positions
    # # latest_quote = gme_snapshot.latest_quote
    # # print(gme_snapshot)