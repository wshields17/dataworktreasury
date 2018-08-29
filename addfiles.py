import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
str = "10.csv"
sp = pd.read_csv(str)
str2 = "5.csv"
sp2 = pd.read_csv(str2)
res= pd.merge(sp,sp2,how = 'inner', on = 'Date')
str3 = "30.csv"
sp3 = pd.read_csv(str3)
res2= pd.merge(res,sp3,how = 'inner', on = 'Date')

print(res2.head())
res2.to_csv('treasury.csv')