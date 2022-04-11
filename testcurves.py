# provides test curves: linear, gaussian etc.

import random

r = random.random

def Linear():
    # linear test sample
    f = lambda x: 5 * x + 10
    # x data
    x = list(range(10))
    # y data with noise introduced through r()
    y = [f(X) + r() * 2 for X in x]
    return (x, y)

def Gaussian():
    # gaussian test sample
    # gaussian equation f(x) = A*e^ -(x-B)^2 / (2*C^2)
    f = lambda x: 5 * math.exp( - (x - 60) ** 2 / (2 * 10 ** 2) )
    # gaussian with nose through r()
    y = [f(x) + r() for x in range(100)]
    return (x, y)
