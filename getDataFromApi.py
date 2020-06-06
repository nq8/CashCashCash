import requests
import pandas as pd
from bs4 import BeautifulSoup


def getKey():
    with open("alphavantage.key", "r") as f:
        return f.readline()

def retrieveCurrentSharePrice(key):
    API_URL = "https://www.alphavantage.co/query"
    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "LHA.FRK",
        "outputsize": "compact",
        "datatype": "csv",
        "apikey": key,
    }
    response = requests.get(API_URL, data)
    print(response.text)

def getSomeInfoForETF(etf, key):
    import json

    with open('example_response.json') as f:
        data = json.load(f)

    print (data)

def parseAvista(isin):
    response = requests.get("https://www.ariva.de/" + isin + "/zusammensetzung")
    soup = BeautifulSoup(response.text)
    print(soup.find(id == "CONTENT"))
    #print(response.text)

if __name__ == "__main__":
    key = getKey()
    #retrieveCurrentSharePrice(key)
    #getSomeInfoForETF("EUNL", eod_key)
    parseAvista("IE00B4L5Y983")