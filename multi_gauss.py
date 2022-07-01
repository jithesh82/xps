# a multi gaussian maker for to use with scipy curve_fit

import math

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

    When a piece of code like this function works I just 
    remember the verse from Bhagavat Gita
       aash-charya-vat pasyati kash-chid enam
       aash-charyavad vadati tathaiva chaanyaha
       aashcharya-vach chainyam anyaha srunoti
       shrutvapyenam veda na chaiva kash-chit || 2.29 ||
    'One sees this Self as a wonder, 
    another speaks of it in wonder, 
    another hears of it as a wonder;
    yet having heard none understands this at all'
    """
    # number of peaks to fit
    # make N global; N = 3 #3
    N = int(len(par)/3.0)

    # number of unknown parameters in the equation
    n = 3 #3
    # (i, j, k) for three parameters
    def term(X, i, j, k): 
        return par[i] * math.exp(- (X - par[j])**2 / (2 * par[k]**2))
    #print('par: ', par)
    #print(x)
    #print('term: ', term(2, 0, 1, 2))

    #pdb.set_trace()

    split = []
    # split [0..9] --> [0, 1, 2], [3, 4, 5] etc.
    for i in range(0, n * N, 3):
        # split_ -->  [0, 1, 2] etc.
        # range(0, 3), range(3, 6) etc.
        split_ = list(range(i, i + 3))
        # split --> [[0, 1, 2], ...]
        split.append(split_)
    # create multi-equation with multiple gaussian
    # terms as a sum
    
    #print(split)
    #pdb.set_trace()

    def multiterm(X):
        """
        sum all the terms in the gaussian
        """
        return sum((term(X, i, j, k) for (i, j, k) in \
                split))    

    #print('multiterm2: ', multiterm(2))
    # sum the terms over the entire x range 
    return [multiterm(X) for X in x]

