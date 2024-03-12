import numpy as np
import matplotlib.pyplot as plt
def func_rosenbroke(w1, w2):
    return 100*(w2-w1**2)**2 + (1-w1)**2

def random_search_global_minimum(num_steps, start_point, num_direction, step_size):
    """
    Функция для случайного поиска глобального минимума функции.

    Параметры:
    function: функция, для которой мы ищем минимум.
    num_steps: количество шагов, за которые мы должна достигнуть минимума в худшем случае.
    start_point:  начальная точка.
    num_direction: количество направлений, в которых мы должны выполнить поиск
    step_size: размер шага в каждом направлении.

    Возвращает:
    Значение минимума функции и соответствующую точку.
    """
    min_value = float('inf')
    min_w1 = None
    min_w2 = None
    current_w1, current_w2 = start_point


    for P in range(num_steps):
        for _ in range(num_direction):
            #Генерируем случайное направление размерностью = 2, в диапаоне [-1,1)
            direction = np.random.uniform(-1,1,size=2)
            #Нормируем направление, так как длина вектора направления должна оставаться равной 1
            direction /= np.linalg.norm(direction)

            #Вычисляем новую точку
            new_w1 = current_w1 + step_size*direction[0]
            new_w2 = current_w2 + step_size*direction[1]
            new_value = func_rosenbroke(new_w1, new_w2)

            if new_value<min_value:
                min_value = new_value
                min_w1, min_w2 = new_w1, new_w2

        current_w1, current_w2 = min_w1, min_w2
        step_size = step_size/(P+1)


    return min_value


# Параметры для поиска
num_steps = 50
num_directions = 1000
step_size = 1
initial_point = (-2, -2)

arr_min_val = []
steps = range(1,51)
for step in steps:
    min_val = random_search_global_minimum(step,initial_point,num_directions,step_size)
    arr_min_val.append(min_val)

#Построение графика минимального значения для каждого N
plt.plot(steps,arr_min_val)
plt.title("Minimum value VS number of step")
plt.xlabel("step, K")
plt.ylabel("Minimum value")
plt.show()