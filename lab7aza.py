import pandas as pd
import numpy as np
from pandas import DataFrame
from numpy import nan as nan
df: DataFrame = pd.DataFrame({
'ord_no': [70001, nan, 70002, 70004, nan, 70005, nan, 70010, 70003, 70012, nan, 70013],
'purch_amt': [150.5, nan, 65.26, 110.5, 948.5, nan, 5760, 1983.43, nan, 250.45, 75.29, 3045.6],
'sale_amt': [10.5, 20.65, nan, 11.5, 98.5, nan, 57, 19.43, nan, 25.45, 75.29, 35.6],
'ord_date': ['2012-10-05', '2012-09-10', nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
'salesman_id': [5002, 5003, 5001, nan, 5002, 5001, 5001, nan, 5003, 5002, 5003, nan]})
#Найдите и выведи индексы пропущенных значений. Заполните пропущеные значения следующими способами:
for col in df.columns:
    mask=pd.isnull(df[col])
    print(col, df[mask].index.values)
#1Среднимим значения
for i in range(1,3):
    df.iloc[:,i]=df.iloc[:,i].fillna(df.iloc[:,i].mean(),inplace=False)
print(df)
#Медианными значениями
for i in range(1,3):
    df.iloc[:,i]=df.iloc[:,i].fillna(df.iloc[:,i].median(),inplace=False)
#Наиболее часто встечающимися
for col in df.columns:
    mask=df[col].value_counts()
    df[col]=df[col].fillna(mask.idxmax(),inplace=False)
print(df)
#Линейной интерполяцией
df=df.fillna(df.interpolate())
print(df)