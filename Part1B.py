import numpy as np
import matplotlib.pyplot as plt

def quadratic_func(w):
    return np.dot(w, w)

dimention = np.arange(1, 101)
min_val_P100 = []
min_val_P1000 = []
min_val_P10000 = []

for N in dimention:
    optimum_P100 = float("inf")
    optimum_P1000 = float("inf")
    optimum_P10000 = float("inf")
    for _ in range(100):
        w = np.random.uniform(-1, 1, N)
        val = quadratic_func(w)
        if val < optimum_P100:
            optimum_P100 = val
    for _ in range(1000):
        w = np.random.uniform(-1, 1, N)
        val = quadratic_func(w)
        if val < optimum_P1000:
            optimum_P1000 = val
    for _ in range(10000):
        w = np.random.uniform(-1, 1, N)
        val = quadratic_func(w)
        if val < optimum_P10000:
            optimum_P10000 = val
    min_val_P100.append(optimum_P100)
    min_val_P1000.append(optimum_P1000)
    min_val_P10000.append(optimum_P10000)

plt.plot(dimention, min_val_P100, label="P=100")
plt.plot(dimention, min_val_P1000, label="P=1000")
plt.plot(dimention, min_val_P10000, label="P=10000")
plt.title("Min Value VS dimension for different number of steps")
plt.xlabel("Input dimension, N")
plt.ylabel("Minimum value")
plt.legend()
plt.show()
