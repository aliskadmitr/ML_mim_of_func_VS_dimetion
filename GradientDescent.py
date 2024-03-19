from autograd import grad
import numpy as np
import matplotlib.pyplot as plt
def GradientDes(g, max_iter, w, alpha):
    history_weight = []
    coast_history = []
    gradient = grad(g)
    for k in range(max_iter):
        grad_new = gradient(w)
        w = w - alpha*grad_new
        history_weight.append(w)
        coast_history.append(g(w))

    plt.plot(coast_history, history_weight)
    plt.title("Gradient Descent")
    plt.xlabel("weight")
    plt.ylabel("coast")
    plt.show()

    return history_weight, coast_history
def func(w):
    return 1 / 50 * (w ** 4 + w ** 2 + 10 * w)
history_weight, coast_history = GradientDes(func, 1000, np.array([2.0]), 0.1)
