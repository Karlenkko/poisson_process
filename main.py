import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def poisson_process(n):
    p = random.poisson(lam=300, size=n)
    print(np.average(p))
    return p


if __name__ == '__main__':
    plt.plot(range(100), poisson_process(100))
    plt.title("simulation of poisson process")
    plt.xlabel("Days")
    plt.ylabel("number of visitors")
    plt.show()
