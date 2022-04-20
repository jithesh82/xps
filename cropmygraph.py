#!/usr/bin/env python3

# plot a csv 2 column data

import pandas as pd
import matplotlib.pyplot as plt
import sys
plt.ion()

def cropIt(df, xmin, xmax):
    # exclude values less than xmin
    df = df[df['x'] > xmin]
    # exclude values greater than xmax
    df = df[df['x'] < xmax]
    return df

# saves the clicked x, y data
clicked = []
def on_click(event):
    """
    To save the x, y data from right mouse click
    """
    if event.button is MouseButton.LEFT:
        clicked.append((event.xdata, event.ydata))
        print((event.xdata, event.ydata))

# set up matplotlib for catching mouse clicks
from matplotlib.backend_bases import MouseButton
plt.connect('button_press_event', on_click)

def cropMyGraph(data):
    # read the csv file
    df = pd.read_csv(data)
    # picking up first two columns of df
    df = df[[df.columns[0], df.columns[1]]]
    # rewrite the column names for ease of
    # plotting
    df.columns = ['x', 'y']
    while True:
        # turn stdin on
        #plt.ion()
        plt.plot(df['x'], df['y'])
        # wait to choose the end points
        wait = input('q to quit: ')
        # breakout of the infinite loop
        if wait == 'q': break
        # visualy inspect graph and click suitable
        # crop points
        #xmin = input('xmin: ')
        #xmax = input('xmax: ')
        xmin = clicked[0][0]
        xmax = clicked[1][0]
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
        df = cropMyGraph(data)
