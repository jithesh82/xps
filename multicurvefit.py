# fit multiple peaks

import math

#par =[1, 2, 3]
def equation(x, *par):
    # fits guassian curve of the form
    # f(x) = A*e^ -(x-B)^2 / (2*C^2)
    return [par[0] * math.exp(- (value - par[1])**2 / (2 * par[2]**2) ) for value in x]

import pickle
(x, y) = pickle.load(open('fitsample.pkl', 'rb'))

import  matplotlib.pyplot as plt
plt.ion()

from plotmeagraph import Plot
Plot(x,y).plot()

from scipy.optimize import curve_fit
popt, _ = curve_fit(equation, x, y, p0=(22000, 284.6, 0.6))

print(popt)

Plot(x, equation(x, *popt)).plot()

input()
