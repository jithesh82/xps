# shift an xps peak by a certain amount of energy

import pandas as pd
import matplotlib.pyplot as plt

plt.ion()

df = pd.read_csv('Au.csv')
df.columns = ['BE', 'Int']

shift = 0
while True:
    plt.clf()
    df1 = df.copy()
    plt.plot(df1['BE'] - float(shift), df1['Int'])
    shift = input('enter the shift amount: ')
    if shift == 'q': break
    #df1['BE'] = df1['BE'] - float(shift)
