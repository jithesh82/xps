#!/usr/bin/env python3

# plot a csv 2 column data

import pandas as pd
import matplotlib.pyplot as plt
# get access to stdin/out
plt.ion()
import sys
from matplotlib.backend_bases import MouseButton

def cropIt(df, xmin, xmax):
    # exclude values less than xmin
    df = df[df['x'] > xmin]
    # exclude values greater than xmax
    df = df[df['x'] < xmax]
    return df

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
    # read the csv file
    df = pd.read_csv(data)
    # picking up first two columns of df
    df = df[[df.columns[0], df.columns[1]]]
    # rewrite the column names for ease of
    # plotting
    df.columns = ['x', 'y']
    while True:
        # turn stdin on
        plt.plot(df['x'], df['y'])
        plt.show()
        # wait to choose the end points
        wait = input('choose crop points and press enter; then q to quit: \n')
        # breakout of the infinite loop
        if wait == 'q': break
        # visualy inspect graph and click suitable
        # crop points
        xmin = I.clicked[0][0]
        xmax = I.clicked[1][0]
        # clear I.clicked for further use
        I.clicked = []
        # call cropIt with suitable crop points
        df = cropIt(df, float(xmin), float(xmax))

    return (df['x'], df['y'])

# run as a top-level file by reading
# data as commnadline argument
if __name__ == '__main__':
    # help command line option
    if sys.argv[1] == '-h':
        print('Usage:  plot_csv.py mydata.csv ')
    else:
        # visualize the data and choose crop points
        # the returned df will be a cropped graph
        data = sys.argv[1]
        # data --> o1s.csv 
        (df['x'], df['y']) = cropMyGraph(data)
