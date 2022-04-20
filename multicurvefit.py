"""
my peak fitting suite
"""

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

    # number of unknown parameters in the equation
    n = 3 #3
    # (i, j, k) for three parameters
    def term(X, i, j, k): 
        return par[i] * math.exp(- (X - par[j])**2 / (2 * par[k]**2))
    #print(par)
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


# global N --> number of peaks to fit
N = 3

from plotmeagraph import Plot
from matplotlib import pyplot as plt
plt.ion()
from scipy.optimize import curve_fit

# open saved xps data - c1s - already bg substracted
import pickle
(x, y) = pickle.load(open('fitsample.pkl', 'rb'))
Plot(x, y, linestyle='dotted').plot()

# for catching mouse events from graph
from matplotlib.backend_bases import MouseButton

class savePeaks:
    """
    save peaks as clicked
    create instances and save it in a list
    """
    def __init__(self, pos, height):
        # pos --> position of the peak
        # height --> height of the peak
        self.pos = pos
        self.height = height

# to save peak position and height to use as guess
clicked =[]

# to catch right mouse click - and save x,y data
def on_click(event):
    if event.button is MouseButton.LEFT:
        print('data coords: ', event.xdata, event.ydata)
        clicked.append((event.xdata, event.ydata))

# connect button press event
plt.connect('button_press_event', on_click)

input('wait: ')

# guesses for 3 peaks to fit
#peaks = [(284.7918548387097, 23678.924688024308), (286.47733870967744, 5252.790677685957), (288.9612096774194, 2075.8710207310705)]
peaks = clicked

# guesses for 3 peaks to fit (height, pos, width)
g1 = (peaks[0][1], peaks[0][0], 0.5)
g2 = (peaks[1][1], peaks[1][0], 0.5)
g3 = (peaks[2][1], peaks[2][0], 0.5)

width_guess = 0.5

# no. of peaks to fit
N = len(clicked)

# (x, y) --> clicked(1,0)
guess = [(clicked[i][1], clicked[i][0], width_guess) for \
        i in range(len(clicked))]

# unpack all (a, b, c) in guess
guess = [g  for item in guess for g in item]

print(*g1, *g2, *g3)

# guessed peaks
#ytofit = multiGauss(x, *g1, *g2, *g3)
ytofit = multiGauss(x, *guess)
Plot(x, ytofit).plot()

#pdb.set_trace()

# perform fit
#popt, _ = curve_fit(multiGauss, x, y, p0=[*g1, *g2, *g3])
popt, _ = curve_fit(multiGauss, x, y, p0=[*guess])

# fitted result
yfit = multiGauss(x, *popt)
Plot(x, yfit).plot()

# wait - plt.ion is on - otherwise windows disappears
input('wait: ')

print('opt: \n', popt)
print('clicked: \n', clicked)
print('guess :\n', guess)
