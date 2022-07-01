# read the data file - parse it
# read the paramete file - parse it
# perform fit and plot
# v1 - class skelton, process data funcion
# v2 - added readData to the class
# v3 - clean up
# v4 - working fit code

import pandas as pd
from multi_gauss import multiGauss as Gauss
from scipy.optimize import curve_fit as curveFit
from matplotlib import pyplot as plt

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
        guess = [x for row in df.iloc for x in row]
        return guess

    def fit(self):
        """
        performs fit
        """
        x, y = self.readData()
        guess = self.readParam()
        ytofit = Gauss(x, *guess)
        # bound -> lower and upper bound of fitting params
        bounds = (0, [20000] * len(guess))
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
    ProcessAndFit('testdata.xlsx', 'testguess.xlsx')()
