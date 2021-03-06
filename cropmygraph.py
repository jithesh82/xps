#!/usr/bin/env python3

# plot a csv 2 column data

import pandas as pd
import matplotlib.pyplot as plt
# get access to stdin/out
plt.ion()
import sys
from matplotlib.backend_bases import MouseButton
from xyfromfile import xyfromfile
import sys
import os

def cropIt(x, y, xmin, xmax):
    # exclude values less than xmin
    y = y[x > xmin]
    # exclude values greater than xmax
    y = y[x  < xmax]
    # exclude values less than xmin
    x = x[x > xmin]
    # exclude values greater than xmax
    x = x[x  < xmax]
    return x, y

# saves the clicked x, y data
class clickMe:
    """
    saves the clicked co-ordinates in `clicked`
    aim: to removed `clicked` from global scope
    """
    def __init__(self):
        self.clicked = []
    def on_click(self, event):
        """
        To save the x, y data from right mouse click
        """
        if event.button is MouseButton.LEFT:
            self.clicked.append((event.xdata, event.ydata))
            print((event.xdata, event.ydata))

def cropMyGraph(data):
    # create a clickMe instance to store clicks
    I = clickMe()
    # set up matplotlib for catching mouse clicks
    plt.connect('button_press_event', I.on_click)
    # read the file
    x, y = xyfromfile(data)
    while True:
        # turn stdin on
        plt.plot(x, y)
        plt.show()
        # wait to choose the end points
        wait = input('choose crop points and press enter; \nq to quit: \n')
        # breakout of the infinite loop
        if wait == 'q': break
        # visualy inspect graph and click suitable
        # crop points
        xmin = I.clicked[0][0]
        xmax = I.clicked[1][0]
        # clear I.clicked for further use
        I.clicked = []
        # call cropIt with suitable crop points
        x, y = cropIt(x, y, float(xmin), float(xmax))
    df = pd.DataFrame()
    df['x']=x ; df['y'] = y
    file_noext = os.path.basename(data).split('.')[0]
    df.to_excel('trim'+ file_noext + '.xlsx', index=False)
    return (x, y)

# run as a top-level file by reading
# data as commnadline argument
if __name__ == '__main__':
    # help command line option
    try:
        datafile = sys.argv[1] or 'o1s.csv'
    except Exception:
        print('Usage:  cropmygraph.py mydata.ext ')
        print(sys.exc_info())
    else:
        # visualize the data and choose crop points
        # the returned df will be a cropped graph
        data = sys.argv[1]
        # data --> o1s.csv 
        (x, y) = cropMyGraph(data)
