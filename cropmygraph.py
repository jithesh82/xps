#!/usr/bin/env python3

# plot a csv 2 column data

import pandas as pd
import matplotlib.pyplot as plt
import sys

def cropIt(df, xmin, xmax):
    # exclude values less than xmin
    df = df[df['x'] > xmin]
    # exclude values greater than xmax
    df = df[df['x'] < xmax]
    return df

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
        plt.ion()
        plt.plot(df['x'], df['y'])
        # visualy inspect graph and enter suitable
        # crop points
        xmin = input('xmin: ')
        xmax = input('xmax: ')
        # breakout of the infinite loop
        if xmin == 'q': break
        # call cropIt with suitable crop points
        df = cropIt(df, float(xmin), float(xmax))
    return df

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
        df = cropMyGraph(data)
