


def format_values(stock_data):
    if len(stock_data) > 0:
        for k, v in stock_data.items():
            if k == "currentPrice" or k == "previousClose" or k == "open" or k == "dayHigh" or k == "dayLow":
                stock_data[k] = format(v, ',.2f')
            if k == "averageVolume10days":
                stock_data[k] ="{:,}".format(v)    
    return stock_data

