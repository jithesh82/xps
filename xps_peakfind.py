# find peaks in an xps general spectra

import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

df = pd.read_csv('Au.csv')
df.columns = ['BE', 'Int']
plt.plot(df['Int'], '.')

peaks, _ = find_peaks(df['Int'], prominence=2200)
plt.plot(peaks, df['Int'][peaks], 'X')
plt.show()
