import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
str = "30yr.csv"
sp = pd.read_csv(str)
print(sp.describe()) 
sp.rename(columns={'Price':'30Price','Open':'30Open','High':'30High','Low':'30Low','Vol.':'30Vol.','Change %':'30Change %'}, inplace=True)
print(sp.head())
sp.to_csv('30.csv', encoding='utf-8', index=False)
#y = sp.SP
""" x = sp['Squat'] 
plt.bar(y,x,)
plt.show() """