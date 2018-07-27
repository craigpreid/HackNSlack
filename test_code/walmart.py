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
    "format": "json" # json|xml
}
params["query"] = "ibad"

def walmart_serch(q):
    params["query"] = q
    walmart_data = requests.get(url, params=params)
    walmart_url = walmart_data.url
    walmart_data = walmart_data.json()
    print(walmart_url)
    #print(walmart_data)
    result = {}
    result["totalResults"] = walmart_data["totalResults"]
    result["start"] = walmart_data["start"]
    result["numItems"] = walmart_data["numItems"]
    result["items"] = walmart_data["items"]
    return walmart_data

print(sys.argv)
arglen = len(sys.argv)
if arglen>1:
    for i in range(1,arglen):
        #print(sys.argv[i])
        k,v=sys.argv[i].split("=")
        if k in params:
            params[k] = v
        result = walmart_serch(params["query"])
        print(params)
        print(json.dumps(result, indent=4))
    

