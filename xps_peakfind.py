# find peaks in an xps general spectra

import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

plt.ion()

df = pd.read_csv('Au.csv')
df.columns = ['BE', 'Int']
prom = 1000
thresh = None
width = None
distance = None
while True:
    plt.plot(df['Int'], '.')

    peaks, _ = find_peaks(df['Int'], prominence=prom, \
        threshold=thresh,\
        width=width,\
        distance=distance\
        )
    plt.plot(peaks, df['Int'][peaks], 'X')
    prom = input('prom: ')
    thresh = float(input('threshold: '))
    width = float(input('width: '))
    height = float(input('height: '))
    plt.clf()
    if prom == 'q':
        break
    prom = float(prom)
    #thresh = float(thresh)


