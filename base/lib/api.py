
from .stream_config import api_key,api_secret,base_url
from django.http import HttpResponse
import json
import alpaca_trade_api as tradeapi
from alpaca_trade_api import Stream
import yfinance as yf
from .api_helper import format_values
from ..models import Stocks


def getstock(symbol):
    print("running")

    msft = yf.Ticker(symbol)
    raw_json = json.dumps(msft.info)
  
    stock_data = json.loads(raw_json)
    
    return format_values(stock_data)
         
def get_portfolio_current_val():
    x = Stocks.objects.all().values_list('symbol', flat=True).distinct()
    current_price_dict = {}
    print(x)
    for y in x:
        print('whats happenin ' + y)
     
        print('got here')
        lookup = getstock(y)
        print('got here 2')
        # current_price_dict = {lookup['symbol'] : lookup['currentPrice']}
        # p["current"] = current_portfolio_prices[current_sym]
        current_price_dict[lookup['symbol']] =  lookup['currentPrice']
        print('got here 3')
    print(current_price_dict)
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