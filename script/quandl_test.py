import quandl


quandl.ApiConfig.api_key = 'API KEY'
mydata = quandl.get('EIA/PET_RWTC_D')

print(mydata)
