from time import sleep
import apikeys
import subprocess
import pandas as pd
import websocket
import json, pprint, talib
import numpy as np
import csv
import sys
import math
from binance.enums import *
from binance.client import Client
from openpyxl import load_workbook

#Script to obtain data on for the variables, from spreadsheet (registry)
wb = pd.read_excel('Signals.xlsx', 
                         sheet_name = 'Data_for_entry_exit' , 
                                                  
                         )



#How many coins on LONG position
coins_up_0 = (wb.loc[3, 'E'])


#How many coins on the Short posiiton
coins_down_0 = (wb.loc[3, 'F'])


#variables for API on how many coins to buy
library_long = int(wb.loc[2, 'I'])
library_short = int(wb.loc[3, 'I'])


#value of usd to buy from spreadsheet
value_usd = (wb.loc[6, 'E'])
print("Amount of USD to trade {}".format(value_usd))





#variable to connect to socket taken from spreadsheet
SOCKET = str(wb.loc[5, 'I'])


#for inserting closes incomings data to a list
closes = []


in_position = False




#TRADE_SYMBOL  = to whatever variable is set on spreadsheet
TRADE_SYMBOL = str(wb.loc[4, 'I'])



#API variable for APi key and key secret
client = Client(apikeys.API_KEY, apikeys.API_SECRET)


#variables for websocket when opened, closed and incoming messages
def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    global closes, in_position

    #formatting incomning of data
    print("received message")
    json_message = json.loads(message)
    pprint.pprint(json_message)

    #coverting json_message variable to a candle which is the one containig that information and also estract info from the list depending 
    #what is needed, of course knowing where to extract from documentation from Binence
    candle = json_message["k"]

    is_candle_closed = candle["x"]
    close = candle["c"]

    last_price = close
    

    #lines of code to capture inmeadiate last closed price to take that price as entry price
    #for calculations on percentages
    if close:
        print("last closed price at {}".format(close))
        closes.append(float(close))
        


        print("last known close price")
        print(closes)

        ws.close()
        

           
#this last two line are key to keep all info from socket to keep coming in
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()    

#this is for showing last price of coin in terminal
last_price = closes[0]
print(last_price)


print("Last price for ticker on futures were {}".format(last_price))

#calculation on how many coin to buy dividind who much to spend in usd and what was the last price on the coin
value_future = math.floor(value_usd/last_price)
print(value_future)


#creates an order to but on long
order = client.futures_create_order(
    symbol= TRADE_SYMBOL,
    side=SIDE_BUY,
    positionSide = 'LONG',
    type =  ORDER_TYPE_MARKET,
    quantity= value_future)
print(order)



#creates an order to but on short
order = client.futures_create_order(
    symbol= TRADE_SYMBOL,
    side=SIDE_SELL,
    positionSide = 'SHORT',
    type =  ORDER_TYPE_MARKET,
    quantity= value_future)
print(order)





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



#editing and overwriting the amount of bought coins in the spreasheet(registry)
#long side
new_value1 = wb.loc[3,'E']  = amount_future_contracts_long

#short side
new_value2 = wb.loc[3,'F'] = amount_future_contracts_short






#editing and overwriting entry price in the spreasheet(registry)
new_entry_price = wb.loc[104, 'C'] = last_price


#editing and overwriting from entry price what are the precentages up or down in the spreasheet(registry)
new_entry_price_p100 = wb.loc[4, 'C'] = round((last_price * 2) , 6)
new_entry_price_p99 = wb.loc[5, 'C'] = round((last_price * 1.99) , 6)
new_entry_price_p98 = wb.loc[6, 'C'] = round((last_price * 1.98) , 6)
new_entry_price_p97 = wb.loc[7, 'C'] = round((last_price * 1.97) , 6)
new_entry_price_p96 = wb.loc[8, 'C'] = round((last_price * 1.96) , 6)
new_entry_price_p95 = wb.loc[9, 'C'] = round((last_price * 1.95) , 6)
new_entry_price_p94 = wb.loc[10, 'C'] = round((last_price * 1.94) , 6)
new_entry_price_p93 = wb.loc[11, 'C'] = round((last_price * 1.93) , 6)
new_entry_price_p92 = wb.loc[12, 'C'] = round((last_price * 1.92) , 6)
new_entry_price_p91 = wb.loc[13, 'C'] = round((last_price * 1.91) , 6)
new_entry_price_p90 = wb.loc[14, 'C'] = round((last_price * 1.90) , 6)
new_entry_price_p89 = wb.loc[15, 'C'] = round((last_price * 1.89) , 6)
new_entry_price_p88 = wb.loc[16, 'C'] = round((last_price * 1.88) , 6)
new_entry_price_p87 = wb.loc[17, 'C'] = round((last_price * 1.87) , 6)
new_entry_price_p86 = wb.loc[18, 'C'] = round((last_price * 1.86) , 6)
new_entry_price_p85 = wb.loc[19, 'C'] = round((last_price * 1.85) , 6)
new_entry_price_p84 = wb.loc[20, 'C'] = round((last_price * 1.84) , 6)
new_entry_price_p83 = wb.loc[21, 'C'] = round((last_price * 1.83) , 6)
new_entry_price_p82 = wb.loc[22, 'C'] = round((last_price * 1.82) , 6)
new_entry_price_p81 = wb.loc[23, 'C'] = round((last_price * 1.81) , 6)
new_entry_price_p80 = wb.loc[24, 'C'] = round((last_price * 1.80) , 6)
new_entry_price_p79 = wb.loc[25, 'C'] = round((last_price * 1.79) , 6)
new_entry_price_p78 = wb.loc[26, 'C'] = round((last_price * 1.78) , 6)
new_entry_price_p77 = wb.loc[27, 'C'] = round((last_price * 1.77) , 6)
new_entry_price_p76 = wb.loc[28, 'C'] = round((last_price * 1.76) , 6)
new_entry_price_p75 = wb.loc[29, 'C'] = round((last_price * 1.75) , 6)
new_entry_price_p74 = wb.loc[30, 'C'] = round((last_price * 1.74) , 6)
new_entry_price_p73 = wb.loc[31, 'C'] = round((last_price * 1.73) , 6)
new_entry_price_p72 = wb.loc[32, 'C'] = round((last_price * 1.72) , 6)
new_entry_price_p71 = wb.loc[33, 'C'] = round((last_price * 1.71) , 6)
new_entry_price_p70 = wb.loc[34, 'C'] = round((last_price * 1.70) , 6)
new_entry_price_p69 = wb.loc[35, 'C'] = round((last_price * 1.69) , 6)
new_entry_price_p68 = wb.loc[36, 'C'] = round((last_price * 1.68) , 6)
new_entry_price_p67 = wb.loc[37, 'C'] = round((last_price * 1.67) , 6)
new_entry_price_p66 = wb.loc[38, 'C'] = round((last_price * 1.66) , 6)
new_entry_price_p65 = wb.loc[39, 'C'] = round((last_price * 1.65) , 6)
new_entry_price_p64 = wb.loc[40, 'C'] = round((last_price * 1.64) , 6)
new_entry_price_p63 = wb.loc[41, 'C'] = round((last_price * 1.63) , 6)
new_entry_price_p62 = wb.loc[42, 'C'] = round((last_price * 1.62) , 6)
new_entry_price_p61 = wb.loc[43, 'C'] = round((last_price * 1.61) , 6)
new_entry_price_p60 = wb.loc[44, 'C'] = round((last_price * 1.60) , 6)
new_entry_price_p59 = wb.loc[45, 'C'] = round((last_price * 1.59) , 6)
new_entry_price_p58 = wb.loc[46, 'C'] = round((last_price * 1.58) , 6)
new_entry_price_p57 = wb.loc[47, 'C'] = round((last_price * 1.57) , 6)
new_entry_price_p56 = wb.loc[48, 'C'] = round((last_price * 1.56) , 6)
new_entry_price_p55 = wb.loc[49, 'C'] = round((last_price * 1.55) , 6)
new_entry_price_p54 = wb.loc[50, 'C'] = round((last_price * 1.54) , 6)
new_entry_price_p53 = wb.loc[51, 'C'] = round((last_price * 1.53) , 6)
new_entry_price_p52 = wb.loc[52, 'C'] = round((last_price * 1.52) , 6)
new_entry_price_p51 = wb.loc[53, 'C'] = round((last_price * 1.51) , 6)
new_entry_price_p50 = wb.loc[54, 'C'] = round((last_price * 1.50) , 6)
new_entry_price_p49 = wb.loc[55, 'C'] = round((last_price * 1.49) , 6)
new_entry_price_p48 = wb.loc[56, 'C'] = round((last_price * 1.48) , 6)
new_entry_price_p47 = wb.loc[57, 'C'] = round((last_price * 1.47) , 6)
new_entry_price_p46 = wb.loc[58, 'C'] = round((last_price * 1.46) , 6)
new_entry_price_p45 = wb.loc[59, 'C'] = round((last_price * 1.45) , 6)
new_entry_price_p44 = wb.loc[60, 'C'] = round((last_price * 1.44) , 6)
new_entry_price_p43 = wb.loc[61, 'C'] = round((last_price * 1.43) , 6)
new_entry_price_p42 = wb.loc[62, 'C'] = round((last_price * 1.42) , 6)
new_entry_price_p41 = wb.loc[63, 'C'] = round((last_price * 1.41) , 6)
new_entry_price_p40 = wb.loc[64, 'C'] = round((last_price * 1.40) , 6)
new_entry_price_p39 = wb.loc[65, 'C'] = round((last_price * 1.39) , 6)
new_entry_price_p38 = wb.loc[66, 'C'] = round((last_price * 1.38) , 6)
new_entry_price_p37 = wb.loc[67, 'C'] = round((last_price * 1.37) , 6)
new_entry_price_p36 = wb.loc[68, 'C'] = round((last_price * 1.36) , 6)
new_entry_price_p35 = wb.loc[69, 'C'] = round((last_price * 1.35) , 6)
new_entry_price_p34 = wb.loc[70, 'C'] = round((last_price * 1.34) , 6)
new_entry_price_p33 = wb.loc[71, 'C'] = round((last_price * 1.33) , 6)
new_entry_price_p32 = wb.loc[72, 'C'] = round((last_price * 1.32) , 6)
new_entry_price_p31 = wb.loc[73, 'C'] = round((last_price * 1.31) , 6)
new_entry_price_p30 = wb.loc[74, 'C'] = round((last_price * 1.30) , 6)
new_entry_price_p29 = wb.loc[75, 'C'] = round((last_price * 1.29) , 6)
new_entry_price_p29 = wb.loc[76, 'C'] = round((last_price * 1.28) , 6)
new_entry_price_p27 = wb.loc[77, 'C'] = round((last_price * 1.27) , 6)
new_entry_price_p26 = wb.loc[78, 'C'] = round((last_price * 1.26) , 6)
new_entry_price_p25 = wb.loc[79, 'C'] = round((last_price * 1.25) , 6)
new_entry_price_p24 = wb.loc[80, 'C'] = round((last_price * 1.24) , 6)
new_entry_price_p23 = wb.loc[81, 'C'] = round((last_price * 1.23) , 6)
new_entry_price_p22 = wb.loc[82, 'C'] = round((last_price * 1.22) , 6)
new_entry_price_p21 = wb.loc[83, 'C'] = round((last_price * 1.21) , 6)
new_entry_price_p20 = wb.loc[84, 'C'] = round((last_price * 1.20) , 6)
new_entry_price_p19 = wb.loc[85, 'C'] = round((last_price * 1.19) , 6)
new_entry_price_p18 = wb.loc[86, 'C'] = round((last_price * 1.18) , 6)
new_entry_price_p17 = wb.loc[87, 'C'] = round((last_price * 1.17) , 6)
new_entry_price_p16 = wb.loc[88, 'C'] = round((last_price * 1.16) , 6)
new_entry_price_p15 = wb.loc[89, 'C'] = round((last_price * 1.15) , 6)
new_entry_price_p14 = wb.loc[90, 'C'] = round((last_price * 1.14) , 6)
new_entry_price_p13 = wb.loc[91, 'C'] = round((last_price * 1.13) , 6)
new_entry_price_p12 = wb.loc[92, 'C'] = round((last_price * 1.12) , 6)
new_entry_price_p11 = wb.loc[93, 'C'] = round((last_price * 1.11) , 6)
new_entry_price_p10 = wb.loc[94, 'C'] = round((last_price * 1.10) , 6)
new_entry_price_p09 = wb.loc[95, 'C'] = round((last_price * 1.09) , 6)
new_entry_price_p08 = wb.loc[96, 'C'] = round((last_price * 1.08) , 6)
new_entry_price_p07 = wb.loc[97, 'C'] = round((last_price * 1.07) , 6)
new_entry_price_p06 = wb.loc[98, 'C'] = round((last_price * 1.06) , 6)
new_entry_price_p05 = wb.loc[99, 'C'] = round((last_price * 1.05) , 6)
new_entry_price_p04 = wb.loc[100, 'C'] = round((last_price * 1.04) , 6)
new_entry_price_p03 = wb.loc[101, 'C'] = round((last_price * 1.03) , 6)
new_entry_price_p02 = wb.loc[102, 'C'] = round((last_price * 1.02) , 6)
new_entry_price_p01 = wb.loc[103, 'C'] = round((last_price * 1.01) , 6)

new_entry_price_m01 = wb.loc[105, 'C'] = round((last_price * .99) , 6)
new_entry_price_m02 = wb.loc[106, 'C'] = round((last_price * .98) , 6)
new_entry_price_m03 = wb.loc[107, 'C'] = round((last_price * .97) , 6)
new_entry_price_m04 = wb.loc[108, 'C'] = round((last_price * .96) , 6)
new_entry_price_m05 = wb.loc[109, 'C'] = round((last_price * .95) , 6)
new_entry_price_m06 = wb.loc[110, 'C'] = round((last_price * .94) , 6)
new_entry_price_m07 = wb.loc[111, 'C'] = round((last_price * .93) , 6)
new_entry_price_m08 = wb.loc[112, 'C'] = round((last_price * .92) , 6)
new_entry_price_m09 = wb.loc[113, 'C'] = round((last_price * .91) , 6)
new_entry_price_m10 = wb.loc[114, 'C'] = round((last_price * .90) , 6)
new_entry_price_m11 = wb.loc[115, 'C'] = round((last_price * .89) , 6)
new_entry_price_m12 = wb.loc[116, 'C'] = round((last_price * .88) , 6)
new_entry_price_m13 = wb.loc[117, 'C'] = round((last_price * .87) , 6)
new_entry_price_m14 = wb.loc[118, 'C'] = round((last_price * .86) , 6)
new_entry_price_m15 = wb.loc[119, 'C'] = round((last_price * .85) , 6)
new_entry_price_m16 = wb.loc[120, 'C'] = round((last_price * .84) , 6)
new_entry_price_m17 = wb.loc[121, 'C'] = round((last_price * .83) , 6)
new_entry_price_m18 = wb.loc[122, 'C'] = round((last_price * .82) , 6)
new_entry_price_m19 = wb.loc[123, 'C'] = round((last_price * .81) , 6)
new_entry_price_m20 = wb.loc[124, 'C'] = round((last_price * .80) , 6)
new_entry_price_m21 = wb.loc[125, 'C'] = round((last_price * .79) , 6)
new_entry_price_m22 = wb.loc[126, 'C'] = round((last_price * .78) , 6)
new_entry_price_m23 = wb.loc[127, 'C'] = round((last_price * .77) , 6)
new_entry_price_m24 = wb.loc[128, 'C'] = round((last_price * .76) , 6)
new_entry_price_m25 = wb.loc[129, 'C'] = round((last_price * .75) , 6)
new_entry_price_m26 = wb.loc[130, 'C'] = round((last_price * .74) , 6)
new_entry_price_m27 = wb.loc[131, 'C'] = round((last_price * .73) , 6)
new_entry_price_m28 = wb.loc[132, 'C'] = round((last_price * .72) , 6)
new_entry_price_m29 = wb.loc[133, 'C'] = round((last_price * .71) , 6)
new_entry_price_m30 = wb.loc[134, 'C'] = round((last_price * .70) , 6)
new_entry_price_m31 = wb.loc[135, 'C'] = round((last_price * .69) , 6)
new_entry_price_m32 = wb.loc[136, 'C'] = round((last_price * .68) , 6)
new_entry_price_m33 = wb.loc[137, 'C'] = round((last_price * .67) , 6)
new_entry_price_m34 = wb.loc[138, 'C'] = round((last_price * .66) , 6)
new_entry_price_m35 = wb.loc[139, 'C'] = round((last_price * .65) , 6)
new_entry_price_m36 = wb.loc[140, 'C'] = round((last_price * .64) , 6)
new_entry_price_m37 = wb.loc[141, 'C'] = round((last_price * .63) , 6)
new_entry_price_m38 = wb.loc[142, 'C'] = round((last_price * .62) , 6)
new_entry_price_m39 = wb.loc[143, 'C'] = round((last_price * .61) , 6)
new_entry_price_m40 = wb.loc[144, 'C'] = round((last_price * .60) , 6)
new_entry_price_m41 = wb.loc[145, 'C'] = round((last_price * .59) , 6)
new_entry_price_m42 = wb.loc[146, 'C'] = round((last_price * .58) , 6)
new_entry_price_m43 = wb.loc[147, 'C'] = round((last_price * .57) , 6)
new_entry_price_m44 = wb.loc[148, 'C'] = round((last_price * .56) , 6)
new_entry_price_m45 = wb.loc[149, 'C'] = round((last_price * .55) , 6)
new_entry_price_m46 = wb.loc[150, 'C'] = round((last_price * .54) , 6)
new_entry_price_m47 = wb.loc[151, 'C'] = round((last_price * .53) , 6)
new_entry_price_m48 = wb.loc[152, 'C'] = round((last_price * .52) , 6)
new_entry_price_m49 = wb.loc[153, 'C'] = round((last_price * .51) , 6)
new_entry_price_m50 = wb.loc[154, 'C'] = round((last_price * .50) , 6)
new_entry_price_m51 = wb.loc[155, 'C'] = round((last_price * .49) , 6)
new_entry_price_m52 = wb.loc[156, 'C'] = round((last_price * .48) , 6)
new_entry_price_m53 = wb.loc[157, 'C'] = round((last_price * .47) , 6)
new_entry_price_m54 = wb.loc[158, 'C'] = round((last_price * .46) , 6)
new_entry_price_m55 = wb.loc[159, 'C'] = round((last_price * .45) , 6)
new_entry_price_m56 = wb.loc[160, 'C'] = round((last_price * .44) , 6)
new_entry_price_m57 = wb.loc[161, 'C'] = round((last_price * .43) , 6)
new_entry_price_m58 = wb.loc[162, 'C'] = round((last_price * .42) , 6)
new_entry_price_m59 = wb.loc[163, 'C'] = round((last_price * .41) , 6)
new_entry_price_m60 = wb.loc[164, 'C'] = round((last_price * .40) , 6)
new_entry_price_m61 = wb.loc[165, 'C'] = round((last_price * .39) , 6)
new_entry_price_m62 = wb.loc[166, 'C'] = round((last_price * .38) , 6)
new_entry_price_m63 = wb.loc[167, 'C'] = round((last_price * .37) , 6)
new_entry_price_m64 = wb.loc[168, 'C'] = round((last_price * .36) , 6)
new_entry_price_m65 = wb.loc[169, 'C'] = round((last_price * .35) , 6)
new_entry_price_m66 = wb.loc[170, 'C'] = round((last_price * .34) , 6)
new_entry_price_m67 = wb.loc[171, 'C'] = round((last_price * .33) , 6)
new_entry_price_m68 = wb.loc[172, 'C'] = round((last_price * .32) , 6)
new_entry_price_m69 = wb.loc[173, 'C'] = round((last_price * .31) , 6)
new_entry_price_m70 = wb.loc[174, 'C'] = round((last_price * .30) , 6)
new_entry_price_m71 = wb.loc[175, 'C'] = round((last_price * .29) , 6)
new_entry_price_m72 = wb.loc[176, 'C'] = round((last_price * .28) , 6)
new_entry_price_m73 = wb.loc[177, 'C'] = round((last_price * .27) , 6)
new_entry_price_m74 = wb.loc[178, 'C'] = round((last_price * .26) , 6)
new_entry_price_m75 = wb.loc[179, 'C'] = round((last_price * .25) , 6)
new_entry_price_m76 = wb.loc[180, 'C'] = round((last_price * .24) , 6)
new_entry_price_m77 = wb.loc[181, 'C'] = round((last_price * .23) , 6)
new_entry_price_m78 = wb.loc[182, 'C'] = round((last_price * .22) , 6)
new_entry_price_m79 = wb.loc[183, 'C'] = round((last_price * .21) , 6)
new_entry_price_m80 = wb.loc[184, 'C'] = round((last_price * .20) , 6)
new_entry_price_m81 = wb.loc[185, 'C'] = round((last_price * .19) , 6)
new_entry_price_m82 = wb.loc[186, 'C'] = round((last_price * .18) , 6)
new_entry_price_m83 = wb.loc[187, 'C'] = round((last_price * .17) , 6)
new_entry_price_m84 = wb.loc[188, 'C'] = round((last_price * .16) , 6)
new_entry_price_m85 = wb.loc[189, 'C'] = round((last_price * .15) , 6)
new_entry_price_m86 = wb.loc[190, 'C'] = round((last_price * .14) , 6)
new_entry_price_m87 = wb.loc[191, 'C'] = round((last_price * .13) , 6)
new_entry_price_m88 = wb.loc[192, 'C'] = round((last_price * .12) , 6)
new_entry_price_m89 = wb.loc[193, 'C'] = round((last_price * .11) , 6)
new_entry_price_m90 = wb.loc[194, 'C'] = round((last_price * .10) , 6)
new_entry_price_m91 = wb.loc[195, 'C'] = round((last_price * .09) , 6)
new_entry_price_m92 = wb.loc[196, 'C'] = round((last_price * .08) , 6)
new_entry_price_m93 = wb.loc[197, 'C'] = round((last_price * .07) , 6)
new_entry_price_m94 = wb.loc[198, 'C'] = round((last_price * .06) , 6)
new_entry_price_m95 = wb.loc[199, 'C'] = round((last_price * .05) , 6)
new_entry_price_m96 = wb.loc[200, 'C'] = round((last_price * .04) , 6)
new_entry_price_m97 = wb.loc[201, 'C'] = round((last_price * .03) , 6)
new_entry_price_m98 = wb.loc[202, 'C'] = round((last_price * .02) , 6)
new_entry_price_m99 = wb.loc[203, 'C'] = round((last_price * .01) , 6)




#overwriting ans saving spreadsheet file (registry)
wb.to_excel('Signals.xlsx',
                sheet_name = 'Data_for_entry_exit' , 
                index=False
                        )

#line to execute (automate) once we have bought our coins to close a position later depending on hoe parameters are set
subprocess.run ([sys.executable,'C:/Users/kevin/Documents/Inversion/Bit trading/FuturesBot3/P1.3.py' ] )

