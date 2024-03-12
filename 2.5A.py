import numpy as np
import matplotlib.pyplot as plt

def func_rosenbroke(w):
    return w**2 + 2

def random_search_global_minimum(num_steps, start_point, step_size):
    min_value = float('inf')
    min_w = None
    current_w = start_point

    for step in range(num_steps):
        direction = np.random.uniform(-1, 1, size=len(start_point))  # Учитываем размерность пространства
        direction /= np.linalg.norm(direction)
        new_w = current_w + step_size * direction
        new_value = func_rosenbroke(new_w)

        if new_value < min_value:
            min_value = new_value
            min_w = new_w

    current_w = min_w

    return min_value, min_w

def max_cos(start_point):
    grad = 2 * start_point
    norm_grad = np.linalg.norm(grad)
    normalized_grad = grad / norm_grad

    direction = np.random.uniform(-1, 1, size=len(start_point))  # Учитываем размерность пространства
    direction_norm = np.linalg.norm(direction)
    normalized_direction = direction / direction_norm

    cos_theta = np.dot(normalized_grad, normalized_direction)

    return cos_theta

# Параметры для поиска
num_steps = 50
step_size = 1
initial_point = np.array([1.0, 0.0])

max_cos_theta = max_cos(initial_point)
print(f"Максимальное значение cos(theta) в начальной точке: {max_cos_theta}")

# Проверка условия ограничения вероятности спуска сверху sqrt(3)/4
if max_cos_theta <= np.sqrt(3) / 4:
    print("Условие вероятности спуска выполняется.")
else:
    print("Условие вероятности спуска не выполняется.")

