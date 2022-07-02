#!/usr/bin/env python3

# return first (x,y) data from csv file
# first two columns

import pandas as pd
import sys

def xyfromcsv(data):
    # read the csv file
    df = pd.read_csv(data)
    # picking up first two columns of df
    df = df[[df.columns[0], df.columns[1]]]
    # rewrite the column names for ease of
    # plotting
    df.rename(columns={df.columns[0]:'x', df.columns[1]:'y'},\
            inplace=True)
    (x, y) = df['x'], df['y']
    return (x, y)

# run as a top-level file by reading
# data as commnadline argument
if __name__ == '__main__':
    # help command line option
    if sys.argv[1] == '-h':
        print('Usage:  xyfromcsv.py  mydata.csv ')
    else:
    # plot the file listed on the command line
    # only first two columns, (x,y) is considered
    # for plotting
        data = sys.argv[1]
        (x, y) = xyfromcsv(data)
