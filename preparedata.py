# creates and substract background 
# v10 - bakup

# import easy plotting utility and plot
from plotmeagraph import Plot
# set up matplotlib to cach mouse events
from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
# crop the graph as needed for bg fit
from cropmygraph import cropMyGraph
import pdb
import pickle
from substractbackground import bgLinear
import sys, os
import pandas as pd

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

#if __name__ == '__main__':

def prepare(data):
    """
    select the region - crop it
    substract base line
    """
    # x, y are pd series
    (x, y) = cropMyGraph(data)

    # clear the current figure
    plt.clf()

    # create a clickMe instance to save clicks
    I = clickMe()
    I.clicked = []
    # catch mouse clicks
    plt.connect('button_press_event', I.on_click)
    
    # plot the graph after cropping to choose the 
    # end points for background
    Plot(x, y).plot()

    print('click select the end points for bg substraction')

    input('wait for click:  \n')

    # pass in the clicked co-ordinates to make bg
    # create a background fitting instance
    I = bgLinear(x, y, *I.clicked[0], *I.clicked[1])
    # substract the background and get the data
    (x, y) = I.substract()

    # plot the substracted x, y data
    Plot(x,y).plot()

    # waits - graph window disapears otherwise
    input('Enter to exit: ')

    #if save == 'y':
    #    pickle.dump((x, y), open('o1s.pkl', 'wb'))

    df = pd.DataFrame()
    df['x'] = x ; df['y'] = y
    file_noext = os.path.basename(data).split('.')[0]
    df.to_excel('bgcuttrim' + file_noext + '.xlsx',\
            index=False)
    return x, y

if __name__ == '__main__':
    try:
        datafile = sys.argv[1] or 'o1s.csv'
    except Exception:
        print('Usage: preparedata.py o1s.csv')
        print(sys.exc_info())
    else:
        prepare(datafile)
