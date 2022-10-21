def task1():
    #TODO: первое задание
a=float(input())**2
print(a)


def task2():
    # TODO: второе задание
    y=input()
    a=0
    for i in y:
        if i in {1,2,3,4,5,6,7,8,9}:
            a=a+1
    print(a)

def task3():
    # TODO: третье задание
a=input()
a=a.split()
b=0
for i in a:
    if i.endswith('bus'):
        b=b+1
print(b)
def task4(generator):
    # TODO: четвертое задание
    a=generator
    for i in a:
        if 'usu' in i==True:
            a=a.replace(i)
    print(a)

def task5(list_of_smth):
    # TODO:
    print(list_of_smth[a[4:-1]])

def task6(list1, list2, list3, list4):
    # TODO: пятое задание
    list1=set(list1)
    list2=set(list2)
    list3=set(list3)
    list4=set(list4)
    lista = list1.intersection(list2)
    listb = list3.intersection(list4)
    a = lista.intersection(list2)
    b = listb.union(list2)
    print(b - a)


def task7():
    # TODO: ...
import numpy as np
np.random.seed(1)
a=np.random.randint(0,25,(5,5))
print(a)
a=np.delete(a, (0), axis=0)
a=np.delete(a,(4),axis=1)
print(np.linalg.det(a))

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth, n):
    # TODO: ...
    import numpy as np
    a = list_of_smth
    b=[]
    for i in a:
        x=b.append(np.mean(a[i:]))
print(b)

def task11(filename="infile.csv"):
    # TODO: ...
df="infile.csv"
import numpy as np
import pandas as pd
a=df.isnull()
print(a)
a=a.sum()
print(a)
df['x']=df['x'].fillna(df['x'].interpolate())
df['x_err']=df['x_err'].fillna(df['x_err'].mean())
print(df)
df2=df[df['y']!=np.nan]
df3=df2[df2['y_err']!=np.nan]
print(df3)

#def task12(filename="video-games.csv"):
    # TODO: ...
