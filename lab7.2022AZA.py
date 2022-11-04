import numpy as np
import pandas as pd
diamonds = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
df=diamonds
print(df)
#Найдите все алмазы которые по любому линейному размеру больше 5.
dx = df['x']>5
dy = df['y']>5
dz = df['z']>5
DF= df[dx & dy & dz]
print(DF)
#Создайте новый DataFrame в которому исключены все не чсиловые столбы исходного DataFrame.
df2=df.drop(columns=['cut', 'color', 'clarity'])
print(df2)
#Расчитатйте средние значения для каждого столбца
print(df2.mean())
#Посчитаете все пропущенные занчения в Dataframe
print(df.isnull().sum().sum())
#Напишите функцию возращающую 20 случайныз строчек из DataFrame (без повторений)
y=np.random.randint(0,len(df.index),20)
for i in y:
    print(df.iloc[i])
#Узнайте реальное использование оперативной памяти вашим DataFrame
print(diamonds.memory_usage().sum())
#Постройте график средних цен для каждой категории (cut) алмазов.
s=f.groupby('cut').agg({'price':'mean'}).sort_values(by="price", ascending=True)
print(s)
s.plot(kind="bar")
plt.show()
#Постройте гистрограмму веса ('carat') алмазов.
h=f['carat']
h.plot(kind="hist")
plt.show()

