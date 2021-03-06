#!/usr/bin/env python3

# current version - rewrite to incorporate
# commandline arguments
# defines different possible fit functions
# uses scipy.optimize.curve_fit to fit the
# x, y data to deduce the parameters

import scipy, os, math
from scipy import optimize
curve_fit = optimize.curve_fit

class fitFunctions:
    """
    Base fitting class
    Initializes the data
    Performs the fit
    The subclasses redefines equation as per
    their requirement
    """
    def __init__(self, x, y):
        # the (x, y) data to be fit
        self.x = x
        self.y = y
    def equation(self):
        # subclasses redefines equation
        pass

    def run(self):
        popt, _ = curve_fit(self.equation, self.x, \
                self.y, bounds=([20000, 284, 0.5], [25000,285, 1]))
        return popt

class fitLinear(fitFunctions):
    """
    Defines linear equation for fitting
    """
    def __init__(self, x, y):
        fitFunctions.__init__(self, x, y)

    def equation(self, x, m, C):
        # linear euation of the form
        # y = mx + C
        # m --> slope
        # C --> y intercept
        return [m * value + C for value in x]


class fitGaussian(fitFunctions):
    """
    Defines Gaussian equation for fitting
    f(x) = A*e^ -(x-B)^2 / (2*C^2)
    """
    def __init__(self, x, y):
        fitFunctions.__init__(self, x, y)

    def equation(self, x, A, B, C):
        # fits guassian curve of the form
        # f(x) = A*e^ -(x-B)^2 / (2*C^2)
        return [A * math.exp(- (value - B)**2 / (2 * C**2) ) for value in x]

if __name__ == '__main__':
    """ perform test fit
    """
    import random, sys
    from matplotlib import pyplot as plt

    r = random.random

    #choice = sys.argv[2]
    if sys.argv[1] == '-h':
        print('Usage:  fitmycurve.py data.csv 1')
        print('1 --> linear \n 2 --> guassian')
    if sys.argv[2] == 1:
        # linear test equation
        from testcurves import Linear
        (x, y) = Linear()
        # x, y scatter plot of the test data
        #plt.plot(x, y, '*')
        # create a linear fitting instance
        I = fitLinear(x, y)
        # perform fit
        popt = I.run()
        # popt[0], popt[1] ... gives the optimized
        # fit parameter in the order defined in
        # function "equation"
        print("optimized fit parameters: ", popt)
        # define the fitted y curve
        yfit = lambda x: popt[0] * x + popt[1]
        # fitted y values
        Y = [yfit(X) for X in x]
        # plot fitted values
        plt.plot(x, Y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Linear Curve Fit')
        plt.legend(['data', 'fitted'])
        plt.show()
    else:
        from xyfromcsv import xyfromcsv
        from plot_csv import plotCSV
        #plotCSV('c.csv')
        x, y = xyfromcsv('c.csv')
        #plt.plot(x, y) ; plt.show()
#        I = fitGaussian(x, y)
#        popt = I.run()
#        print(popt)
        #f = lambda x: 5 * math.exp( - (x - 60) ** 2 / (2 * 10 ** 2) )
        #y = [f(x) + r() for x in range(100)]
        #plt.plot(range(100), y, '*')
        #plt.show()
        from cropmygraph import cropMyGraph
        (x, y) = cropMyGraph('c.csv')
        from substractbackground import bgLinear
        Ibg = bgLinear(x, y, 282.43, 600, 288.28, 2110)
        (x, y) = Ibg.substract()
        from plotmeagraph import Plot
        Plot(x, y).plot()
        I = fitGaussian(x, y)
        popt = I.run()
        print(popt)
        f = lambda x: popt[0] * math.exp( - (x - popt[1]) ** 2 / (2 * popt[2] ** 2) )
        y = [f(X) for X in x]
        Plot(x, y).plot()
        wait = input()

