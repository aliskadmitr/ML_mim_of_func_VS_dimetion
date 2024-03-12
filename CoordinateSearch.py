import numpy as np

def coordinate_search(g, alpha, max_iteration, w):


    """g: целевая функция
       alpha: размер шага,
       max_its: максимальное количество итераций,
       w: начальное значение весов"""

    #Создаем набор всех координатных направлений
    #Функция np.eye создает единичную матрицу размером np.size(w) x np.size(w) для положительных и отрицательных направлений
    directions_plus = np.eye(np.size(w), np.size(w))
    directions_minus = -np.eye(np.size(w), np.size(w))

    #объединяются в один массив,чтобы получить всевозможные направления, в которых можно сдвинуться в текущей точке
    directions = np.concatenate((directions_plus, directions_minus), axis=0)

    #Начинаем координатный поиск
    weight_history = []  # container for weight history
    cost_history = []  # container for corresponding cost function history
    for i in range(1, max_iteration+1):
        weight_history.append(w)
        cost_history.append(g(w))

        ### выберите наилучшее направление спуска
        # вычислите все новые точки-кандидаты
        candidates = [w + alpha * direction for direction in directions]

        ## оценивайте всех кандидатов
        candidate_costs = [g(candidate) for candidate in candidates]

        # если мы найдем реальное направление спуска, сделаем шаг в его направлении
        best_index = np.argmin(candidate_costs)
        w = candidates[best_index]

    # запись весов и оценка затрат
    weight_history.append(w)
    cost_history.append(g(w))
    return weight_history, cost_history