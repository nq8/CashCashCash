import requests

def getKey():
    with open("alphavantage.key", "r") as f:
        return f.readline()

def retrieveCurrentSharePrice(key):
    API_URL = "https://www.alphavantage.co/query"
    data = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": "IS3N.FRK",
        "outputsize": "compact",
        "datatype": "csv",
        "interval": "1min",
        "apikey": key,
    }
    response = requests.get(API_URL, data)
    print(response.text)

if __name__ == "__main__":
    key = getKey()
    retrieveCurrentSharePrice(key)

#BMW: BMW.FRK
#Lufthanse: LHA.FRK
#ishares World: EUNL.FRK
#ishares EM: IS3N.FRK
#ETF110: X010.FRK
#ETF127: E127.FRK
#Franklin: XQ1Z.FRK