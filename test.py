import boringstonks

config = {}
config['api'] = 'http://localhost:8081/graphql'
config['timeout'] = 10

print(boringstonks.getStocks("periods { period balanceSheet { assets liabilities  } } ", "access_token", config=config))

