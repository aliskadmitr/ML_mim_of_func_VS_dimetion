import numpy as np
import matplotlib.pyplot as plt

#Создаем квадратичную функцию
def quadratic_func(w):
    return np.dot(w.T,w)

#Создаем массив диапазонов размерности N от 1 до 100
dimention = np.arange(1,101)

#Массив с минимальными значениями функции
min_val = []

#Количество случайных точек на гиперкубе [-1;1]*...
P=100
for n in dimention:
    # Говорим, что изначально минимальное значение будет в бесконечности
    optimum = float("inf")
    for i in range(P):
        #Генерируем равномерно распределенные веса (для каждой точки высчитывается значение функции)
        w = np.random.uniform(-1,1,n)
        val = quadratic_func(w)
        if val<optimum:
            optimum = val
    min_val.append(optimum)

#Построение графика минимального значения для каждого N
plt.plot(dimention,min_val)
plt.title("Minimum value of qudratic function VS input dimention")
plt.xlabel("input dimention, N")
plt.ylabel("Minimum value")
plt.show()