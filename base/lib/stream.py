import websocket,json
from .stream_config import api_key,api_secret,socket
class OpenSocket :
   
    
    def __init__(self):
        #socket = "wss://data.alpaca.markets/stream"
        self.api_key = api_key
        self.api_secret = api_secret
        self.socket = socket
        
       

    def run_socket(self):
         self.ws =websocket.WebSocketApp(self.socket,on_open = self.on_open,on_message = self.on_message)
         self.ws.run_forever()

    def on_open(self,ws):
        print("opened message")
      
        auth_data = {
              "action" : "auth",
              "key": self.api_key, 
              "secret": self.api_secret
        }
        ws.send(json.dumps(auth_data))
        
    #{"action":"subscribe","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["AAPL","VOO"]}
       
    
    def on_message(self,ws,message):
        print(message)




    def get_data(self,):
        listen_message =  {
               "action" : "subscribe",
             "trades":["BBBY"],"quotes":["BBBY"],"bars":["BBBY"]
        }
        print(json.dumps(listen_message))
        self.ws.send(json.dumps(listen_message))