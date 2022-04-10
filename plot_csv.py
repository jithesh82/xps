#!/usr/bin/env python3

# plot a csv 2 column data

import pandas as pd
import matplotlib.pyplot as plt
import sys

def plotCSV(data):
    # read the csv file
    df = pd.read_csv(data)
    # picking up first two columns of df
    df = df[[df.columns[0], df.columns[1]]]
    # rewrite the column names for ease of
    # plotting
    df.columns = ['x', 'y']
    plt.plot(df['x'], df['y'])
    plt.show()

# run as a top-level file by reading
# data as commnadline argument
if __name__ == '__main__':
    # help command line option
    if sys.argv[1] == '-h':
        print('Usage:  plot_csv.py mydata.csv ')
    else:
    # plot the file listed on the command line
    # only first two columns, (x,y) is considered
    # for plotting
        data = sys.argv[1]
        plotCSV(data)
