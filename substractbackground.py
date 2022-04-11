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
