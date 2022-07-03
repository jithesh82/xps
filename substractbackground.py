# creates and substract background 
# v11 - bakup
# v12 - working code - updated __name__ == block

# import easy plotting utility and plot
from plotmeagraph import Plot
from matplotlib import pyplot as plt
# crop the graph as needed for bg fit
import sys
import os
from xyfromcsv import xyfromcsv
from xyfromexcel import xyfromexcel
import pandas as pd

class backGround:

    """
    substracts background from data (x, y)
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate(self):
        """
        subcalsses redefines this method
        """
    def substract(self):
        # generates background
        yLine = self.generate()
        # substracts background
        y = [(y1 - y2) for (y1, y2) in zip(self.y, yLine)]
        # return the updated data
        return (self.x, y)

class bgLinear(backGround):
    def __init__(self, x, y, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        backGround.__init__(self, x, y)

    def generate(self):
        """
        Generates a linear background.
        Line --> two point form
        y - y1 = {(y2 - y1)/(x2 - x1)} * (x - x1)
        """
        f = lambda x: ((self.y2 - self.y1) / (self.x2 - self.x1))\
                * (x - self.x1) + self.y1
        y = [f(X) for X in self.x]
        return y

if __name__ == '__main__':
    try:
        datafile = sys.argv[1]
    except Exception:
        print('Usage: python3 substractbackground.py data.csv')
        print(sys.exc_info())
    else:
        plt.ion()
        datafile = os.path.basename(datafile)
        ext = datafile.split('.')[1]
        if ext == 'csv':
            x, y = xyfromcsv(datafile)
        else:
            if ext == 'xls' or ext == 'xlsx':
                x, y = xyfromexcel(datafile)
        Plot(x, y).plot()
        # endpoints (x1, y1), (x2, y2)
        print('enter bg endpoints')
        x1 = float(input('x1: '))
        y1 = float(input('y1: '))
        x2 = float(input('x2: '))
        y2 = float(input('y2: '))
        I = bgLinear(x, y, x1, y1, x2, y2)
        x, y = I.substract()
        df = pd.DataFrame()
        df['x'] = x; df['y'] = y
        df.to_excel('bgcut'+datafile, index=False)
        Plot(x,y).plot()
        input('Enter to Quit: ')
