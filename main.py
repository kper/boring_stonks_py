import boringstonks

data = boringstonks.getLastOhlcBySymbol("VEND", "fromDate open close", "access_token")
data2 = boringstonks.getStocks("entityCentralIndexKey entityRegistrantName periods { balanceSheet { cashAndCashEquivalentsAtCarryingValue marketableSecurities receivablesNetCurrent stockHoldersEquity assetsCurrent liabilitiesCurrent assets goodwill liabilities entityCommonStockSharesOutstanding commonStockSharesOutstanding  } incomeStatement { revenueFromContractWithCustomerIncludingAssessedTax operatingIncomeLoss netIncomeLoss } } ohlc { close }", "access_token", periods=1)
print(data)
print(data2)

for col in data2.columns:
    print(col)
