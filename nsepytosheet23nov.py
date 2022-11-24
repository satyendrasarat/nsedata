import requests
import pandas as pd
import time
import tempfile
import pygsheets
import json
from nsepython import *
# import urllib library 
from urllib.request import urlopen 
# store the URL in url as  
# parameter for urlopen 
url = "https://raw.githubusercontent.com/satyendrasarat/json-creds/main/creds.json"

# store the response of URL 
response1 = urlopen(url) 
response = json.loads(response1.read())

def _google_creds_as_file():
    temp = tempfile.NamedTemporaryFile()
    temp.write(json.dumps(response).encode('utf-8'))
    temp.flush()
    return temp

creds_file = _google_creds_as_file()
gc = pygsheets.authorize(service_account_file=creds_file.name)

#print(oi_data)
#print(ltp)
#print(crontime)
while True:
    print("running " )
    
    oi_data, ltp, crontime = oi_chain_builder("BANKNIFTY","latest","full")#    df2 = []
    df2 = oi_data
    print(type(df2))
    df3= []
    df3.append(ltp)
    print(type(df3))
    df2.iloc[0]=df3
    sh = gc.open('pytosheet')
#select the first sheet 
    wks = sh[0]
    #wks1 = sh[1]
#update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df2,(1,1))
  #  wks1.set_dataframe(df3,(1,1))
    time.sleep(30)

