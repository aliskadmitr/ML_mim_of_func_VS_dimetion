import numpy as np
import matplotlib.pyplot as plt

def g(w):
    """
    Заданная функция g(w).
    """
    return np.sin(3*w) + 0.3*w**2

def random_search_global_minimum(function, num_runs, start_points, num_iterations):
    """
    Функция для случайного поиска глобального минимума функции.

    Параметры:
    function: функция, для которой мы ищем минимум.
    num_runs: количество запусков алгоритма с разными начальными точками.
    start_points: список начальных точек.
    num_iterations: количество итераций для каждого запуска.

    Возвращает:
    Значение минимума функции и соответствующую точку.
    """
    min_value = float('inf')
    min_x = None
    points = []

    for start_point in start_points:
        for _ in range(num_runs):
            current_x = start_point
            for _ in range(num_iterations):
                # Вычисляем значение функции в текущей точке
                current_value = function(current_x)
                points.append((current_x, current_value))
                # Вычисляем значение функции на соседних точках
                next_values = [function(current_x + delta) for delta in [-0.1, 0.1]]
                # Находим наименьшее значение
                new_value = min(next_values)
                # Проверяем, обновлять ли текущую точку
                if new_value < current_value:
                    current_x += -0.1 if next_values.index(new_value) == 0 else 0.1
                    current_value = new_value
                    # Обновляем минимум
                    if current_value < min_value:
                        min_value = current_value
                        min_x = current_x

    return min_value, min_x, points

# Параметры для поиска
num_runs = 5
start_points = [4.5, -1.5]
num_iterations = 10

# Выполняем поиск глобального минимума
min_value, min_x, points = random_search_global_minimum(g, num_runs, start_points, num_iterations)

# График функции
w_values = np.linspace(-10, 10, 400)
g_values = g(w_values)

# Отображение значений итераций
plt.plot(w_values, g_values, label='g(w)')
for point in points:
    plt.scatter(point[0], point[1], color='red')
plt.scatter(min_x, min_value, color='green', label='Глобальный минимум')
plt.xlabel('w')
plt.ylabel('g(w)')
plt.title('График функции с отображением значений итераций')
plt.legend()
plt.grid(True)
plt.show()
