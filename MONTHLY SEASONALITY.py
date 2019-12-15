# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:39:27 2019

@author: Dell
"""






import pandas as pd
import matplotlib.pyplot as plt
variables=[]

data=pd.read_excel(r'C:\Users\Dell\Downloads\SIC VWAP closing prces.xlsx',parse_dates=[0]) 
Close=data['Closing Price VWAP (GHS)']

for i in Close:
    variables.append(i)

df=pd.DataFrame(Close,index=data['Date'])
df['adjustedCloseEGH']=variables

adjustedCloseEGH=df['adjustedCloseEGH']
monthlyReturnEGH=adjustedCloseEGH.pct_change().groupby([adjustedCloseEGH.index.year,\
                                            adjustedCloseEGH.index.month]).mean()

EGHmonthlyReturnList=[]

for x in range(len(monthlyReturnEGH)):
    EGHmonthlyReturnList.append({'month':monthlyReturnEGH.index[x][1],\
                                 'monthly return':monthlyReturnEGH[x]})



returns=pd.DataFrame(EGHmonthlyReturnList,columns=('month','monthly return'))    

returns.boxplot(column='monthly return',by='month')

fig=plt.gca()
labels=[item.get_text() for item in fig.get_xticklabels()]
labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fig.set_xticklabels(labels)
fig.set_ylabel(' Return')
plt.tick_params(axis='both', which='major', labelsize=7)
plt.title("S.I.C Monthly return 2010-2019")
plt.suptitle("")
plt.show()
    

    
    
    