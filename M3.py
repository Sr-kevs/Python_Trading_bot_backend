import time
import apikeys
import subprocess
import pandas as pd
import websocket
import json, pprint, talib
import numpy as np
import csv
import sys
import threading
import math
from playsound import playsound
from binance.enums import *
from binance.client import Client
from openpyxl import load_workbook


#Script to obtain data on for the variables, from spreadsheet (registry)
wb1 = pd.read_excel('Signals.xlsx', 
                         sheet_name = 'Data_for_entry_exit' , 
                                                  
                         )




# variables for percentages + or - from entry price
dsup100 = wb1.loc[4, 'C']
dsup99 = wb1.loc[5, 'C']
dsup98 = wb1.loc[6, 'C']
dsup97 = wb1.loc[7, 'C']
dsup96 = wb1.loc[8, 'C']
dsup95 = wb1.loc[9, 'C']
dsup94 = wb1.loc[10, 'C']
dsup93 = wb1.loc[11, 'C']
dsup92 = wb1.loc[12, 'C']
dsup91 = wb1.loc[13, 'C']
dsup90 = wb1.loc[14, 'C']
dsup89 = wb1.loc[15, 'C']
dsup88 = wb1.loc[16, 'C']
dsup87 = wb1.loc[17, 'C']
dsup86 = wb1.loc[18, 'C']
dsup85 = wb1.loc[19, 'C']
dsup84 = wb1.loc[20, 'C']
dsup83 = wb1.loc[21, 'C']
dsup82 = wb1.loc[22, 'C']
dsup81 = wb1.loc[23, 'C']
dsup80 = wb1.loc[24, 'C']
dsup79 = wb1.loc[25, 'C']
dsup78 = wb1.loc[26, 'C']
dsup77 = wb1.loc[27, 'C']
dsup76 = wb1.loc[28, 'C']
dsup75 = wb1.loc[29, 'C']
dsup74 = wb1.loc[30, 'C']
dsup73 = wb1.loc[31, 'C']
dsup72 = wb1.loc[32, 'C']
dsup71 = wb1.loc[33, 'C']
dsup70 = wb1.loc[34, 'C']
dsup69 = wb1.loc[35, 'C']
dsup68 = wb1.loc[36, 'C']
dsup67 = wb1.loc[37, 'C']
dsup66 = wb1.loc[38, 'C']
dsup65 = wb1.loc[39, 'C']
dsup64 = wb1.loc[40, 'C']
dsup63 = wb1.loc[41, 'C']
dsup62 = wb1.loc[42, 'C']
dsup61 = wb1.loc[43, 'C']
dsup60 = wb1.loc[44, 'C']
dsup59 = wb1.loc[45, 'C']
dsup58 = wb1.loc[46, 'C']
dsup57 = wb1.loc[47, 'C']
dsup56 = wb1.loc[48, 'C']
dsup55 = wb1.loc[49, 'C']
dsup54 = wb1.loc[50, 'C']
dsup53 = wb1.loc[51, 'C']
dsup52 = wb1.loc[52, 'C']
dsup51 = wb1.loc[53, 'C']
dsup50 = wb1.loc[54, 'C']
dsup49 = wb1.loc[55, 'C']
dsup48 = wb1.loc[56, 'C']
dsup47 = wb1.loc[57, 'C']
dsup46 = wb1.loc[58, 'C']
dsup45 = wb1.loc[59, 'C']
dsup44 = wb1.loc[60, 'C']
dsup43 = wb1.loc[61, 'C']
dsup42 = wb1.loc[62, 'C']
dsup41 = wb1.loc[63, 'C']
dsup40 = wb1.loc[64, 'C']
dsup39 = wb1.loc[65, 'C']
dsup38 = wb1.loc[66, 'C']
dsup37 = wb1.loc[67, 'C']
dsup36 = wb1.loc[68, 'C']
dsup35 = wb1.loc[69, 'C']
dsup34 = wb1.loc[70, 'C']
dsup33 = wb1.loc[71, 'C']
dsup32 = wb1.loc[72, 'C']
dsup31 = wb1.loc[73, 'C']
dsup30 = wb1.loc[74, 'C']
dsup29 = wb1.loc[75, 'C']
dsup29 = wb1.loc[76, 'C']
dsup27 = wb1.loc[77, 'C']
dsup26 = wb1.loc[78, 'C']
dsup25 = wb1.loc[79, 'C']
dsup24 = wb1.loc[80, 'C']
dsup23 = wb1.loc[81, 'C']
dsup22 = wb1.loc[82, 'C']
dsup21 = wb1.loc[83, 'C']
dsup20 = wb1.loc[84, 'C']
dsup19 = wb1.loc[85, 'C']
dsup18 = wb1.loc[86, 'C']
dsup17 = wb1.loc[87, 'C']
dsup16 = wb1.loc[88, 'C']
dsup15 = wb1.loc[89, 'C']
dsup14 = wb1.loc[90, 'C']
dsup13 = wb1.loc[91, 'C']
dsup12 = wb1.loc[92, 'C']
dsup11 = wb1.loc[93, 'C']
dsup10 = wb1.loc[94, 'C']
dsup09 = wb1.loc[95, 'C']
dsup08 = wb1.loc[96, 'C']
dsup07 = wb1.loc[97, 'C']
dsup06 = wb1.loc[98, 'C']
dsup05 = wb1.loc[99, 'C']
dsup04 = wb1.loc[100, 'C']
dsup03 = wb1.loc[101, 'C']
dsup02 = wb1.loc[102, 'C']
dsup01 = wb1.loc[103, 'C']
dsup00 = wb1.loc[104, 'C']
dsupm01 = wb1.loc[105, 'C']
dsupm02 = wb1.loc[106, 'C']
dsupm03 = wb1.loc[107, 'C']
dsupm04 = wb1.loc[108, 'C']
dsupm05 = wb1.loc[109, 'C']
dsupm06 = wb1.loc[110, 'C']
dsupm07 = wb1.loc[111, 'C']
dsupm08 = wb1.loc[112, 'C']
dsupm09 = wb1.loc[113, 'C']
dsupm10 = wb1.loc[114, 'C']
dsupm11 = wb1.loc[115, 'C']
dsupm12 = wb1.loc[116, 'C']
dsupm13 = wb1.loc[117, 'C']
dsupm14 = wb1.loc[118, 'C']
dsupm15 = wb1.loc[119, 'C']
dsupm16 = wb1.loc[120, 'C']
dsupm17 = wb1.loc[121, 'C']
dsupm18 = wb1.loc[122, 'C']
dsupm19 = wb1.loc[123, 'C']
dsupm20 = wb1.loc[124, 'C']
dsupm21 = wb1.loc[125, 'C']
dsupm22 = wb1.loc[126, 'C']
dsupm23 = wb1.loc[127, 'C']
dsupm24 = wb1.loc[128, 'C']
dsupm25 = wb1.loc[129, 'C']
dsupm26 = wb1.loc[130, 'C']
dsupm27 = wb1.loc[131, 'C']
dsupm28 = wb1.loc[132, 'C']
dsupm29 = wb1.loc[133, 'C']
dsupm30 = wb1.loc[134, 'C']
dsupm31 = wb1.loc[135, 'C']
dsupm32 = wb1.loc[136, 'C']
dsupm33 = wb1.loc[137, 'C']
dsupm34 = wb1.loc[138, 'C']
dsupm35 = wb1.loc[139, 'C']
dsupm36 = wb1.loc[140, 'C']
dsupm37 = wb1.loc[141, 'C']
dsupm38 = wb1.loc[142, 'C']
dsupm39 = wb1.loc[143, 'C']
dsupm40 = wb1.loc[144, 'C']
dsupm41 = wb1.loc[145, 'C']
dsupm42 = wb1.loc[146, 'C']
dsupm43 = wb1.loc[147, 'C']
dsupm44 = wb1.loc[148, 'C']
dsupm45 = wb1.loc[149, 'C']
dsupm46 = wb1.loc[150, 'C']
dsupm47 = wb1.loc[151, 'C']
dsupm48 = wb1.loc[152, 'C']
dsupm49 = wb1.loc[153, 'C']
dsupm50 = wb1.loc[154, 'C']
dsupm51 = wb1.loc[155, 'C']
dsupm52 = wb1.loc[156, 'C']
dsupm53 = wb1.loc[157, 'C']
dsupm54 = wb1.loc[158, 'C']
dsupm55 = wb1.loc[159, 'C']
dsupm56 = wb1.loc[160, 'C']
dsupm57 = wb1.loc[161, 'C']
dsupm58 = wb1.loc[162, 'C']
dsupm59 = wb1.loc[163, 'C']
dsupm60 = wb1.loc[164, 'C']
dsupm61 = wb1.loc[165, 'C']
dsupm62 = wb1.loc[166, 'C']
dsupm63 = wb1.loc[167, 'C']
dsupm64 = wb1.loc[168, 'C']
dsupm65 = wb1.loc[169, 'C']
dsupm66 = wb1.loc[170, 'C']
dsupm67 = wb1.loc[171, 'C']
dsupm68 = wb1.loc[172, 'C']
dsupm69 = wb1.loc[173, 'C']
dsupm70 = wb1.loc[174, 'C']
dsupm71 = wb1.loc[175, 'C']
dsupm72 = wb1.loc[176, 'C']
dsupm73 = wb1.loc[177, 'C']
dsupm74 = wb1.loc[178, 'C']
dsupm75 = wb1.loc[179, 'C']
dsupm76 = wb1.loc[180, 'C']
dsupm77 = wb1.loc[181, 'C']
dsupm78 = wb1.loc[182, 'C']
dsupm79 = wb1.loc[183, 'C']
dsupm80 = wb1.loc[184, 'C']
dsupm81 = wb1.loc[185, 'C']
dsupm82 = wb1.loc[186, 'C']
dsupm83 = wb1.loc[187, 'C']
dsupm84 = wb1.loc[188, 'C']
dsupm85 = wb1.loc[189, 'C']
dsupm86 = wb1.loc[190, 'C']
dsupm87 = wb1.loc[191, 'C']
dsupm88 = wb1.loc[192, 'C']
dsupm89 = wb1.loc[193, 'C']
dsupm90 = wb1.loc[194, 'C']
dsupm91 = wb1.loc[195, 'C']
dsupm92 = wb1.loc[196, 'C']
dsupm93 = wb1.loc[197, 'C']
dsupm94 = wb1.loc[198, 'C']
dsupm95 = wb1.loc[199, 'C']
dsupm96 = wb1.loc[201, 'C']
dsupm97 = wb1.loc[202, 'C']
dsupm98 = wb1.loc[203, 'C']
dsupm99 = wb1.loc[204, 'C']



#show in terminal entry price
print("This entry point {}".format(dsup00))



#how many "long" side coin are available, extracting data from spreadsheet (registry)
print('How many UP tokens I have to trade?')
coins_up_0 = (wb1.loc[3, 'E'])




#how many "short" side coin are available, extracting data from spreadsheet (registry)
coins_down_0 = (wb1.loc[3, 'F'])


#variables for API on how many coins to buy
library_long = int(wb1.loc[2, 'I'])
library_short = int(wb1.loc[3, 'I'])



#extracting variables from spreadsheet (registry) for which variable is for the symbol
TRADE_SYMBOL = "LRCUSDT"

#specify what order type is the one to execute
ORDER_TYPE = ORDER_TYPE_MARKET


#specify what order type is the one to execute
SOCKET = str(wb1.loc[5, 'I'])

#for inserting closes incomings data to a list
closes = []


in_position = True

#API variable for APi key and key secret
client = Client(apikeys.API_KEY, apikeys.API_SECRET)


#variables to indicate which side the ordern is going to take place
long = 'LONG'
short = 'SHORT'


#next 5 lines of code are for extracting info from client's account how many coin are availables 
# thus comparing if the amount bought is the amount shown in account
inside_library1 = client.futures_account()
inside_library2 = inside_library1['positions']
inside_library3_long= inside_library2[(library_long)]
amount_future_contracts_long = (float(inside_library3_long['positionAmt'] ))
print("Long Future Contracts: {}".format(amount_future_contracts_long) )

#next 5 lines of code are for extracting info from client's account how many coin are availables 
# thus comparing if the amount bought is the amount shown in account
inside_library1 = client.futures_account()
inside_library2 = inside_library1['positions']
inside_library3_short= inside_library2[(library_short)]
amount_future_contracts_short = float(inside_library3_short['positionAmt'] )
print("Short Future Contracts: {}".format(amount_future_contracts_short) )



#variables for websocket when opened, closed, incoming messages and placing an order to make a transaction
def order(symbol, side, quantity, order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.futures_create_order(symbol=symbol, side=side, positionSide = short , quantity=quantity, type=order_type)
        print(order)
    except Exception as e:
        print("An exception occurred - {}".format(e))
        return False

    return True



#variables for websocket when opened, closed, incoming messages and placing an order to make a transaction
def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")
    time.sleep(60)
    subprocess.run ([sys.executable,'filepath/M3.py'] ) 
    sys.exit()

def on_message(ws, message):
    global closes, in_position

    #formatting incomning of data
    print("received message")
    json_message = json.loads(message)
    pprint.pprint(json_message)

    #coverting json_message variable to a candle which is the one containig that information and also estract info from the list depending 
    #what is needed, of course knowing where to extract from documentation from Binance
    candle = json_message["k"]

    is_candle_closed = candle["x"]
    close = candle["c"]
    
    if close:
        print("last closed price at {}".format(close))
        closes.append(float(close))
        
        
        # inside of script load a copy of the same spreadsheet (registry)        
        wb2 = pd.read_excel('Signals.xlsx', 
                         sheet_name = 'Data_for_entry_exit' , 
                                                  
                         )

        
        #this is to identify which script is the one running from the rest 
        print("last known close price")
        print(closes)
        print("M3")

        #make script to check if both copies loaded are the same
        check_wb = wb1.equals(wb2)                 
        print("Are excel files the same? {}".format(check_wb))   
        #if not the same execute another script, this to automate in case of any changes on the transaction manually or from other scripts running                  
        if not check_wb ==True:
            subprocess.run ([sys.executable,'filepath/P1.1.py'] ) 
            sys.exit()


        #the next lines of code are for supervising in real time the last price of the coin
        #this is to trigger an action once a condition is met
        if len(closes):
            last_closed = closes[-1]
            #for selling -3% down in FuturesBot3, sell 1/10 sushidown
            if last_closed < dsupm07 :
                order = client.futures_create_order(
                    symbol= TRADE_SYMBOL,
                    side=SIDE_BUY,
                    positionSide = short,
                    type =  ORDER_TYPE_MARKET,
                    quantity = round( ( (amount_future_contracts_short*-1) /8) )
                    )
                print(order)   
                #playsound('filepath/cashingmachine.mp3')
                #subprocess.run ([sys.executable,'filepath/M4.py' ] )
                sys.exit() 
   
   
                    
        #the next lines of code are for supervising in real time the last price of the coin
        #this is to trigger an action once a condition is met
        #this would be a copy of the the previous script this is if you want to execute a second action on the same script when the requirements are met
        if len(closes):
            last_closed = closes[-1]
            if last_closed > dsupm04 :
                #last_closed > dsup10   :
                if in_position:
                    print("Sold all DOWN token @ 2 percent down")                    
                    #playsound('filepath/cashingmachine.mp3')
                    #once condition is met and action triggerred automates to intiate next script                    
                    subprocess.run ( [sys.executable, 'filepath/selldownmarket2.py' ] )
                    sys.exit()



#line to execute (automate) once we have bought our coins to close a position later depending on hoe parameters are set
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()             