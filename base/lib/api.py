import json
import yfinance as yf
from .api_helper import format_values
from ..models import Stocks,User
import datetime


def getstock(symbol):
    stock_data = {}
    try:
        msft = yf.Ticker(symbol)
        raw_json = json.dumps(msft.info)
        stock_data = json.loads(raw_json)
        return format_values(stock_data)
    except:
        print("An exception occurred in getstock")
        return stock_data
 


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


def get_all_tot_qty(get_current_price = False):
  
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
        total_Quant = get_stk_qty(sym)
        stock_data['symbol'] = sym
        stock_data['tot_quant'] = total_Quant
        stock_data['id'] = count
        stock_data_list.append(stock_data)
    return stock_data_list



def save_action(symbol,qty,current_price,action):
   
    if qty != "" and int(qty) > 0 and current_price != "":
        try:
            stock=Stocks()
            stock.symbol = symbol
            stock.value = current_price
            stock.quantity = qty
            stock.stockbuydate = datetime.datetime.now()
            stock.action = action
            stock.save()
            return True
        except:
            print('error saving stock action')    

                
    else:
        return False


def save_user_amt(action,change_amt):
    user = User.objects.get(firstName="Stock")
    amt = get_user_amt()
    if (action == 'Buy'):
        try:
            user.amount = float(amt) - float(change_amt)
            user.save() 
            return True
        except:
            print("error in Buying funds")
    elif (action == 'Sell'):
        try:
            user.amount = float(amt) + float(change_amt)
            user.save() 
            return True
        except:
            print("error in Selling funds")
            return False    
    else:
        try:
            user.amount =  change_amt
            user.save() 
            return True
        except:
            print("error in Resetting funds")
            return False



def get_stk_qty(symbol):
    total_Quant = 0
    stock_shares = Stocks.objects.filter(symbol= symbol).values()
    
    for data in stock_shares:
            stock_action = data['action']
            
            if stock_action == 'Buy':
                total_Quant = total_Quant + data['quantity']
            else:
                total_Quant = total_Quant - data['quantity']
   
    return total_Quant


def get_user_amt():
    amt = 0
    userdata = User.objects.filter(firstName='Stock').values()
    for data in userdata:
        if(data['amount']):
            amt = data['amount']
    return amt
       