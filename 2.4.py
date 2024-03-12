import numpy as np
# import matplotlib.pyplot as plt

def g(w1,w2):
    """
    Заданная функция g(w).
    """
    return np.tanh(4*w1+4*w2) + max(0,4*w1**2, 1)+1

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
            new_value = g(new_w1, new_w2)

            if new_value<min_value:
                min_value = new_value
                min_w1, min_w2 = new_w1, new_w2

        current_w1, current_w2 = min_w1, min_w2


    return min_value, min_w1, min_w2

# Параметры для поиска
num_steps = 8
num_directions = 1000
step_size = 1
initial_point = (2, 2)

# Выполняем поиск глобального минимума
min_value, min_w1, min_w2 = random_search_global_minimum(num_steps, initial_point, num_directions, step_size)

print(f"Глобальный минимум функции: {min_value} достигается при w1 = {min_w1}, w2 = {min_w2}.")
