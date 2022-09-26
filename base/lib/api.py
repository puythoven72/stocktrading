
from .stream_config import api_key,api_secret,base_url
from django.http import HttpResponse
import json
import alpaca_trade_api as tradeapi
from alpaca_trade_api import Stream
import yfinance as yf



def                     getstock(symbol):
    print("running")

    msft = yf.Ticker(symbol)
    raw_json = json.dumps(msft.info)
  
    stock_data = json.loads(raw_json)
    
    return format_values(stock_data)
         


def format_values(stock_data):
    if len(stock_data) > 0:
        for k, v in stock_data.items():
            if k == "currentPrice" or k == "previousClose" or k == "open" or k == "dayHigh" or k == "dayLow":
                stock_data[k] = format(v, ',.2f')
            if k == "averageVolume10days":
                stock_data[k] ="{:,}".format(v)    
    return stock_data


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