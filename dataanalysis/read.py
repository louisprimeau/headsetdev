import pandas as pd
import matplotlib.pyplot as plt

dat = pd.read_csv('data/test1.csv')

plt.plot(dat["time"],dat["TP9"])
plt.show()
#print(dat)
