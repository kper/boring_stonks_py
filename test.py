import boringstonks

config = {}
config['api'] = 'http://localhost:8081/graphql'
config['timeout'] = 10

#print(boringstonks.getStocks("periods { period balanceSheet { assets liabilities  } } ", "access_token", config=config))

#print(boringstonks.getStockById(1, "periods { period balanceSheet { assets liabilities  } } ", "access_token", config=config))

#print(boringstonks.getStockByCIK("0001000228", "periods { period balanceSheet { assets liabilities  } } ", "access_token", config=config))

#print(boringstonks.getStocksByCIKs(["0001000228"], "periods { period balanceSheet { assets liabilities  } } ", "access_token", config=config))

print(boringstonks.getStocksByTradingSymbol(["B"], "periods { period balanceSheet { assets liabilities  } } ", "access_token", config=config))

