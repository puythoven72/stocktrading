
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
    for p in stock_dict:
        current_sym = p['symbol']
        p["current"] = current_portfolio_prices[current_sym]
    return stock_dict


         
def get_portfolio_current_val():
    symbol_list = Stocks.objects.all().values_list('symbol', flat=True).distinct()
    current_price_dict = {}

    for symbol in symbol_list:
        lookup = getstock(symbol)
        current_price_dict[lookup['symbol']] =  lookup['currentPrice']
    return current_price_dict




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