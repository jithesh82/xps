# find peaks in an xps general spectra

import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

plt.ion()

df = pd.read_csv('Au.csv')
df.columns = ['BE', 'Int']
prom = 1000
while True:
    plt.plot(df['Int'], '.')

    peaks, _ = find_peaks(df['Int'], prominence=prom)#, \
        #threshold=1.5,\
        #width=0.5, distance=10)
    plt.plot(peaks, df['Int'][peaks], 'X')
    prom = input('prom: ')
    plt.clf()
    if prom == 'q':
        break
    prom = int(prom)

#plt.show()
