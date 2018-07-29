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

bestbuy_api_key = "Jz4AJitfYbGIGGaOuTR09Lpl"
bestbuyUrl = "https://api.bestbuy.com/v1/products"

show_arr=[
    "accessories.sku",
    "color",
    "condition",
    "customerReviewAverage",
    "customerReviewCount",
    "customerTopRated",
    "depth",
    "description",
    "details.name",
    "details.value",
    "digital",
    "features.feature",
    "format",
    "height",
    "includedItemList.includedItem",
    "longDescription",
    "longDescriptionHtml",
    "manufacturer",
    "modelNumber",
    "name",
    "preowned",
    "productVariations.sku",
    "quantityLimit",
    "releaseDate",
    "shortDescription",
    "shortDescriptionHtml",
    "sku",
    "upc",
    "warrantyLabor",
    "warrantyParts",
    "weight",
    "width"
    ,"image"
    ,"largeImage"
    ,"thumbnailImage"
]
params = {
    "apiKey": bestbuy_api_key,
    "page": 1,
    "show": ",".join(show_arr),
    "pageSize": 15,
    "format": "json" # json|xml
}
params["query"] = "ipad"
print(bestbuyUrl)

def bestbuy_search(q):
    urlquery = bestbuyUrl + "(search=" + q + ")"
    bestbuy_data = requests.get(urlquery, params=params)
    bestbuy_url = bestbuy_data.url
    bestbuy_data = bestbuy_data.json()
    print(bestbuy_url)
    return bestbuy_data


arglen = len(sys.argv)
#print(arglen)
if arglen>1:
    for i in range(1,arglen):
        #print(sys.argv[i])
        if "=" in sys.argv[i]:
            k,v=sys.argv[i].split("=")
            if k in params:
                params[k] = v
            result = bestbuy_search(params["query"])
            print(params)
            print(json.dumps(result, indent=4))
    

