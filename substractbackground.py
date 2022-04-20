# creates and substract background 

# import easy plotting utility and plot
from plotmeagraph import Plot
# set up matplotlib to cach mouse events
from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
# crop the graph as needed for bg fit
from cropmygraph import cropMyGraph
import pdb
import pickle

class backGround:

    """
    substracts background from data (x, y)
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate(self):
        """
        subcalsses redefines this method
        """

    def substract(self):
        # generates background
        yLine = self.generate()
        # substracts background
        y = [(y1 - y2) for (y1, y2) in zip(self.y, yLine)]
        # return the updated data
        return (self.x, y)
        

class bgLinear(backGround):
    def __init__(self, x, y, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        backGround.__init__(self, x, y)

    def generate(self):
        """
        Generates a linear background.
        Line --> two point form
        y - y1 = {(y2 - y1)/(x2 - x1)} * (x - x1)
        """
        f = lambda x: ((self.y2 - self.y1) / (self.x2 - self.x1))\
                * (x - self.x1) + self.y1
        y = [f(X) for X in self.x]
        return y

# to save the clicked data from the graph
#clicked = []
def onClick(event):
    """
    when right mouse button is clicked update 
    the `clicked` list with x, y data from
    the graph --> the end points of background
    """
    if event.button is MouseButton.LEFT:
        # the x and y are in opposite order
        clicked.append((event.xdata, event.ydata))
        print((event.xdata, event.ydata))

if __name__ == '__main__':

    # x, y are pd series
    (x, y) = cropMyGraph('o1s.csv')

    #pdb.set_trace()

    # clear the current figure
    plt.clf()

    #pdb.set_trace()

    # initialize clicked - same variable used 
    # also in cropmygraph and everywhere - Ha 
    clicked = []
    # catch mouse clicks
    plt.connect('button_press_event', onClick)
    
    # plot the graph after cropping to choose the 
    # end points for background
    Plot(x, y).plot()

    #pdb.set_trace()

    input('wait for click:  \n')

    #pdb.set_trace()

    # pass in the clicked co-ordinates to make bg
    # create a background fitting instance
    I = bgLinear(x, y, *clicked[0], *clicked[1])
    # substract the background and get the data
    (x, y) = I.substract()

    # plot the substracted x, y data
    Plot(x,y).plot()
    # waits - graph window disapears otherwise

    save = input('y for save: ')
    if save == 'y':
        pickle.dump((x, y), open('o1s.pkl', 'wb'))
