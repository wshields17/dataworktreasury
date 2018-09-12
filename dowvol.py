import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
def addcol(dtf,yr):
    
    clname = "chng" + yr
    clname2 = yr + "Price"
    dtf[clname] = (dtf[clname2] - dtf[clname2].shift(-1))/dtf[clname2]
    return dtf

def histvoldays(dtf,daynum):
    
    dnm = str(daynum)
    addcl = "vol" + dnm
    chngcol = "Dow change"
    dtf[addcl] = (dtf[chngcol].rolling(daynum).std() * math.sqrt(252)*100)
    
    return dtf

   
stri = "DJI.csv"
sp = pd.read_csv(stri)
# Get Input of days to use for historical vol
xdys = input("Input days  ")
# Add Column with daily change
sp["Dow change"] = (sp['Adj Close'] - sp["Adj Close"].shift(-1))/sp["Adj Close"]
# Compute historical volatility and add column to hold value
sp = histvoldays(sp,int(xdys))

x=sp.iloc[int(xdys):]
# Get name of column with historical volatility
daysofhist = "vol" +xdys

#plot this column
plt.plot(x[daysofhist])
plt.ylabel('Vol')
plt.xlabel('Day')
plt.show() 