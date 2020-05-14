import requests


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

if __name__ == "__main__":
    key = getKey()
    retrieveCurrentSharePrice(key)
