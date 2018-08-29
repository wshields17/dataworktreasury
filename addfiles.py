import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
str = "10.csv"
sp = pd.read_csv(str)
str2 = "5.csv"
sp2 = pd.read_csv(str2)
res= pd.merge(sp,sp2,how = 'inner', on = 'Date')
str3 = "30.csv"
sp3 = pd.read_csv(str3)
res2= pd.merge(res,sp3,how = 'inner', on = 'Date')


#res2.to_csv('treasury.csv')
#xcorr = res2[float('10Change %')].corr(res2[float('5Change %')])
res2['chng30'] = (res2['30Price'] - res2['30Price'].shift(-1))/res2['30Price'] 
res2['chng10'] = (res2['10Price'] - res2['10Price'].shift(-1))/res2['10Price'] 
res2['chng5'] = (res2['5Price'] - res2['5Price'].shift(-1))/res2['5Price'] 
#res2['5/10'] = (res2['chng5'].rolling(25).std() * math.sqrt(252)*100)/(res2['chng10'].rolling(25).std() * math.sqrt(252)*100)
res2['5vol'] = (res2['chng5'].rolling(5).std() * math.sqrt(252)*100)
res2['5/10'] = (res2['chng5'].rolling(5).std() * math.sqrt(252)*100)/(res2['chng10'].rolling(5).std() * math.sqrt(252)*100)
print(res2.head(40))