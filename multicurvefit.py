# fit multiple peaks

import math

# number of peaks
N = 3

#par =[1, 2, 3]
def v1equation(x, *par):
    # previous version
    # fits guassian curve of the form
    # f(x) = A*e^ -(x-B)^2 / (2*C^2)
    return [par[0] * math.exp(- (X - par[1])**2 / (2 * par[2]**2) ) for X in x]

import pdb

def multiGauss(x, *par):
    """
    Fits single or multiple Gaussian peaks
    Algorithm :
        1. create single gaussian term as a function
        2. here number of unknowns 3 --> p0, p1, p2. 
        3. say number of peaks to fit --> 3
        4. total parameters: p0, p1,...p8 --> (3*3)
        5. construct a list --> [0, 1, 2....3*3-1]
        6. break it down to chunks of 3 --> [0, 1, 2] etc
        7. use the chunks to create terms and use sum func 
            to sum it up
        8. list comprehend the sum over all element in x data
    """
    # number of peaks to fit
    N = 1 #3
    # number of unknown parameters in the equation
    n = 3 #3
    # (i, j, k) for three parameters
    def term(X, i, j, k): 
        return par[i] * math.exp(- (X - par[j])**2 / (2 * par[k]**2))
    print(par)
    print(x)
    print('term: ', term(2, 0, 1, 2))

    #pdb.set_trace()

    split = []
    # split [0..9] --> [0, 1, 2], [3, 4, 5] etc.
    for i in range(0, n * N, 3):
        # split_ -->  [0, 1, 2] etc.
        split_ = list(range(i + 3))
        # split --> [[0, 1, 2], ...]
        split.append(split_)
    # create multi-equation with multiple gaussian
    # terms as a sum
    
    print(split)

    def multiterm(X):
        return sum((term(X, i, j, k) for (i, j, k) in \
                split))    

    print('multiterm2: ', multiterm(2))
    # sum the terms over the entire x range 
    return [multiterm(X) for X in x]

x = range(1, 100)
y = multiGauss(x, 5, 50, 5)
from plotmeagraph import Plot
Plot(x, y).plot()
print(y)
