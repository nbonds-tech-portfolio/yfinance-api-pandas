import yfinance as yf
import pandas as pd


symbols=['QQQ']

for a in symbols:

	tickers = yf.Tickers(a)
	b=tickers.tickers[a].history(period="1mo")

	lenClose=len(b['Close'])
	#print(lenB)
	
	print('\n\n*****Pandas DataFrame*****')
	print('Object Type Is: '+str(type(b))+'\n\n')
	print(b)

	print('\n\n')


	print('\n\n*****Extract Closing Price from Pandas DataFrame*****')
	for d in b['Close']:
		print(d)
		
		
	print('\n\n************Last Closing Price*************************')
	count=0
	for c in b['Close']:
		if count== lenClose-1:
			print(c)
			break;
		else:
			count=count+1



