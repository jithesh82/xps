# a wrapper around matplotlib plot

from matplotlib import pyplot as plt

class Plot:
    def __init__(self, x, y, xlabel='x',\
            ylabel='y', legend=[], title='Graph x-y'):
        self.x = x
        self.y = y
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.legend = legend
        self.title = title

    def plot(self):
        plt.plot(self.x, self.y)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend(self.legend)
        plt.title(self.title)
        plt.show()

