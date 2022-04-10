# defines different possible fit functions
# uses scipy.optimize.curve_fit to fit the
# x, y data to deduce the parameters

import scipy
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
                self.y)
        return popt

class fitLinear(fitFunctions):
    """
    Defines linear equation for fitting
    """
    def __init__(self, x, y):
        fitFunctions.__init__(self, x, y)

    def equation(self,x, m, C):
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
    def __init__(self):
        fitFunctions.__init__(self)

    def equation(x, A, B, C):
        # fits guassian curve of the form
        # f(x) = A*e^ -(x-B)^2 / (2*C^2)
        return [A * math.exp(- (value - B)^2 / (2 * C^2) ) \
            for value in x]

if __name__ == '__main__':
    """ perform test fit
    """
    import random
    from matplotlib import pyplot as plt
    # linear test equation
    f = lambda x: 5 * x + 10
    r = random.random
    # x data
    x = list(range(10))
    # y data introducting noise
    y = [f(X) + r() * 2 for X in x]
    # x, y scatter plot of the test data
    plt.plot(x, y, '*')
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


