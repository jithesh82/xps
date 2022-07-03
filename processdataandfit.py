# read the data file - parse it
# read the paramete file - parse it
# perform fit and plot
# v1 - class skelton, process data funcion
# v2 - added readData to the class
# v3 - clean up
# v4 - working fit code
# v5 - adding commandline execution logic
# v6 - working code - not clean
# v7 - working code
# v8 - clean up


import pandas as pd
from multi_gauss import multiGauss as Gauss
from scipy.optimize import curve_fit as curveFit
from matplotlib import pyplot as plt
import sys
import os
import pdb

class ProcessAndFit:
    """
    - reads the data file data.txt
    - converts the data to x, y dataframe
    - reads the parameter file and saves the 
    - parameter in `guess'
    - performs fit
    - displays the final result
    """
    def __init__(self, dfile=None, pfile=None):
        """
        dfile -> contains the XPS binding energy data
        pfile -> contains the parameters
        """
        self.dfile = dfile
        self.pfile = pfile

    def readData(self):
        """
        - reads the excel data
        - assumes that first column is Binding Energy
        - assumes the second column is intensity
        - exports x, y where
        - x -> BE panda data frame
        - y -> Intensity panda data frame
        """
        df = pd.read_excel(self.dfile)
        x = df.columns[0]
        y = df.columns[1]
        return df[x], df[y]

    def readParam(self):
        """
        - read the fitting guess parameters from excel file
        - excel file format
           int     BE     width
          12304   233.4    0.5
          36303   238.2    0.5
        """
        df = pd.read_excel(self.pfile)
        # guess values 
        dfg = df[[df.columns[0], df.columns[1], \
                df.columns[2]]].copy()
        # lower bound
        df_lbound = df[[df.columns[3], df.columns[4], \
                df.columns[5]]].copy()
        # upper bound
        df_ubound = df[[df.columns[6], df.columns[7], \
                df.columns[8]]].copy()
        # guess
        guess = [x for row in dfg.iloc for x in row]
        # lower bound
        lbounds = [x for row in df_lbound.iloc for x in row]
        # upper bound
        ubounds = [x for row in df_ubound.iloc for x in row]
        #pdb.set_trace()
        return guess, lbounds, ubounds

    def fit(self):
        """
        performs fit
        """
        x, y = self.readData()
        guess, lbounds, ubounds = self.readParam()
        ytofit = Gauss(x, *guess)
        bounds = (lbounds, ubounds)
        popt, _ = curveFit(Gauss, x, y, p0=[*guess], bounds=bounds)
        yfit = Gauss(x, *popt)
        plt.plot(x, y)
        plt.plot(x, ytofit)
        plt.plot(x, yfit)
        plt.xlabel('B.E (eV)')
        plt.ylabel('Intensity (arb.units)')
        plt.legend(['data', 'guess', 'fit'])
        plt.show()

    def __call__(self):
        self.fit()


if __name__ == '__main__':
    try:
        dfile = sys.argv[1]
        pfile = sys.argv[2]
        #ProcessAndFit(dfile, pfile)()
    except Exception:
        print('Looking for files in the current working directory')
        print(sys.exc_info())
        if os.path.exists('testdata.xlsx') and \
            os.path.exists('testguess.xlsx'):
                ProcessAndFit('testdata.xlsx', 'testguess.xlsx')()
        else:
            print("Usage:  python3 data.xlsx param.xlsx")
            print("OR put the data and parameter file in the \
                    same directory as .py file")
    else:
        ProcessAndFit(dfile, pfile)()
