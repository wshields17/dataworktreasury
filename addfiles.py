import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
def addcol(dtf,years):
    yr = str(years)
    clname = "chng" + yr
    clname2 = yr + "Price"
    dtf[clname] = (dtf[clname2] - dtf[clname2].shift(-1))/dtf[clname2]
    return dtf

def histvoldays(dtf,daynum,years):
    yr = str(years)
    dnm = str(daynum)
    addcl = yr + "vol" + dnm
    chngcol = "chng" + yr
    dtf[addcl] = (res2[chngcol].rolling(daynum).std() * math.sqrt(252)*100)
    dtf[addcl] = dtf[addcl].shift(-daynum)
    return dtf

stri = "10.csv"
sp = pd.read_csv(stri)
str2 = "5.csv"
sp2 = pd.read_csv(str2)
res= pd.merge(sp,sp2,how = 'inner', on = 'Date')
str3 = "30.csv"
sp3 = pd.read_csv(str3)
res2= pd.merge(res,sp3,how = 'inner', on = 'Date')


#res2.to_csv('treasury.csv')
#xcorr = res2[float('10Change %')].corr(res2[float('5Change %')])
res2 = addcol(res2,30) 
res2 = addcol(res2,10)
res2 = addcol(res2,5)
#res2['5/10'] = (res2['chng5'].rolling(25).std() * math.sqrt(252)*100)/(res2['chng10'].rolling(25).std() * math.sqrt(252)*100)
xdys = input("Input days  ")
res2 = histvoldays(res2,int(xdys),10)
#res2['5/10'] = (res2['chng5'].rolling(25).std() * math.sqrt(252)*100)/(res2['chng10'].rolling(25).std() * math.sqrt(252)*100)
#print(res2.head(40))
res2.fillna(0)
#pick range to graph
x=res2.iloc[0:25]

daysofhist = "10vol"+xdys
plt.plot(x[daysofhist])
plt.show() 