import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("data/winequality-red.csv",sep=';')
display(np.round(data.describe()))
