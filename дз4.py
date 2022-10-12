import numpy as np
import matplotlib as Plt
import matplotlib.pyplot as plt
#Нарисуйте точками график ... для x со значениями от 0 до 100 с шагом 10
x=np.linspace(1,100,10)
y=np.sin(x)*(x**-2)
plt.plot(x,y)
#Добавьте сетку и описание осей для предыдущего графика
plt.grid(which='major', axis='both', alpha=1)
plt.ylabel('ось y')
plt.xlabel('ось x')
plt.show()
#Нарисуйте непрерывной прямой график ... для x со зачениями от 10 до 100,обавьте сетку и описание осей для графика
#Добавьте сетку и описание осей для графика
x=np.linspace(10,100,1001)
y=np.exp(-x*np.sin(x))
plt.grid(which='major',axis='both',alpha=1)
plt.minorticks_on()
plt.grid(which='minor',axis='both',alpha=0.5)
plt.xlabel('ось x')
plt.ylabel('ось y  f(x)=e^-xsin(x)')
plt.plot(x,y)
plt.show()
#Нарисуйте точками график ... для x со значениями от 10 до 100
x=np.linspace(10,100,10000)
y=np.exp(x*np.sin(x))
plt.ylim(0,15)
plt.plot(x,y, label='func(x)')
plt.show()
#Сделайте логарифмический масштаб по оси ординат. Отразите этот факт в подписи к оси
#Добавьте легенду точкам и подписи к графику
plt.plot(x, y, label='func')
plt.yscale('log')
plt.ylabel('логарифмическая ось у')
plt.legend()
plt.show()
