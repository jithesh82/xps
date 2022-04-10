#!/usr/bin/env python3

# make df from csv file 
# commandline utility
# usage: csv_to_df mydata.csv

import pandas as pd
import sys

def csvTodf(data):
    # read the csv file
    df = pd.read_csv(data)
    return df

# run as a top-level file by reading
# data as commnadline argument
if __name__ == '__main__':
    # help command line option
    if sys.argv[1] == '-h':
        print('Usage:  csv_to_df.py mydata.csv ')
    else:
    # print df
        data = sys.argv[1]
        df = csvTodf(data)
        print(df)
