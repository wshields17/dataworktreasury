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
res2['chng'] = (res2['30Price'] - res2['30Price'].shift(-1))/res2['30Price'] 
yy = res2.loc[:,"10Price"].std()
print(res2['chng'].rolling(25).std() * math.sqrt(252))