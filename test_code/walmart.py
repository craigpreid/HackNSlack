# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import urllib
import json
import sys
import pprint

api_key = "4tsbjxvbrwnpcjdsh277csqu"
url = "http://api.walmartlabs.com/v1/search" 
params = {
    "apiKey": api_key,
    "format": "json", # json|xml
    "numItems": 25,
    "start": 1
}
params["query"] = "ipad"

def walmart_search(q):
    params["query"] = q
    walmart_data = requests.get(url, params=params)
    walmart_url = walmart_data.url
    walmart_data = walmart_data.text
    #walmart_data = str(walmart_data, encoding='utf-8', errors = 'ignore')
    #walmart_url = walmart_url.encode('UTF-8')
    #print(walmart_url)
    #walmart_data = walmart_data.json()
    #walmart_url = walmart_url.encode('utf-8')
    #print(walmart_data)
    return walmart_data

arglen = len(sys.argv)
#print(arglen)
if arglen>1:
    for i in range(1,arglen):
        #print(sys.argv[i])
        if "=" in sys.argv[i]:
            k,v=sys.argv[i].split("=")
            if k in params:
                params[k] = v
    result = walmart_search(params["query"])
    print(result.encode('utf-8'))
    #print(params)
    #print(json.dumps(result, indent=4))
    

#print(sys.argv)
