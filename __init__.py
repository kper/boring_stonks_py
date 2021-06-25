import json
import requests
import pandas 

defaultConfig = dict()
defaultConfig['api'] = 'http://ipax:8081/graphql'
defaultConfig['timeout'] = 20

def getStocks(query, periods = 0, config = defaultConfig):
    mod_query = '{"query": "{ getStocks(periods: %d) { %s } } "}' % (periods, query)
    print(mod_query)
    headers = {'Content-type': 'application/json'}
    x = requests.post(config['api'], data=mod_query, timeout=config['timeout'], headers=headers)
    stocks = x.json()['data']['getStocks']
    print(stocks)
    frame = pandas.json_normalize(stocks)
    return frame

def main():
    query = "tradingSymbol balanceSheets { stockHoldersEquity }"
    x = getStocks(query, periods=1)
    print(x)

if __name__ == "__main__":
    main()