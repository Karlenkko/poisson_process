import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def poisson_process(n):
    p = random.poisson(lam=300, size=n)
    plt.hist(p)
    plt.title("simulation in 10 years")
    plt.show()
    return p

def one_day():
    p = random.exponential(1/300, 6000)
    sum = 0
    idx = 0
    for i in p:
        idx += 1
        sum += i
        if sum > 1:
            break
    plt.hist(p[:idx])
    print(idx)
    plt.title("arrival in 1 day")
    plt.show()


if __name__ == '__main__':
    # poisson_process(3650)
    one_day()