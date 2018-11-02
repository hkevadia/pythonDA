import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt

data=pd.read_csv("data/winequality-red.csv",sep=';')

wineN = data.count(0)
goodQ = data.loc[(data['quality'] > 6)]
goodC = goodQ.count(0)

poorQ = data.loc[(data['quality'] < 5)]
poorC = poorQ.count(0)

avgQ = data.loc[(data['quality'] >= 5) & (data['quality'] <= 6)]
avgC = avgQ.count(0)

good_percent = goodC*100/wineN

print("Total number of wine data: {}".format(wineN))
print("Wines with rating 7 and above: {}".format(goodC))
print("Wines with rating less than 5: {}".format(poorC))
print("Wines with rating 5 and 6: {}".format(avgC))
#print("Percentage of wines with quality 7 and above: {:f}%".format(good_percent))


