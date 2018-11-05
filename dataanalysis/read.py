import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

dat = pd.read_csv('data/test2.csv')
numpydat = dat.values.transpose()
dattag = dat.keys()

sfreq = 256
ch_types = ['mag', 'mag', 'grad', 'grad']
info = mne.create_info(ch_names=list(dat.keys()[1:5]), sfreq=sfreq, ch_types=ch_types)
raw = mne.io.RawArray(numpydat[1:5], info)
scalings = {'mag': 1000, 'grad': 1000}
raw.plot(n_channels=4, scalings=scalings, title='Data from arrays',
         show=True, block=True)


#plt.plot(dat["time"],dat["TP9"])
#plt.show()
#print(dat)"""
