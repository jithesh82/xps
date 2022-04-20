# creates and substract background 

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
clicked = []
def on_click(event):
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
    # self test code
    # x, y pandas series from csv file
    from xyfromcsv import xyfromcsv
    (x, y) = xyfromcsv('c.csv')
    # create a linear background instance
    I = bgLinear(x, y, 280, 460, 297, 1600)
    # substract linear background
    (x, y) = I.substract()
    # import easy plotting utility and plot
    from plotmeagraph import Plot
    Plot(x, y).plot()
    # set up matplotlib to cach mouse events
    from matplotlib import pyplot as plt
    from matplotlib.backend_bases import MouseButton
    plt.connect('button_press_event', on_click)
    # retain access to stdin/out
    plt.ion()
    #from cropmygraph import cropMyGraph
    from plot_csv import plotCSV
    plotCSV('o1s.csv')
    # wait for clicking the bg endpoints
    input('wait: ')
    # get x, y data from csv file
    (x, y) = xyfromcsv('o1s.csv')
    # create a background fitting instance
    # pass in the clicked co-ordinates to make bg
    I = bgLinear(x, y, *clicked[0], *clicked[1])
    # substract the background and get the data
    (x, y) = I.substract()
    # plot the substracted x, y data
    Plot(x,y).plot()
    # waits - graph window disapears otherwise
    input('wait: ')
