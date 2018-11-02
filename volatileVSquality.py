import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("data/winequality-red.csv",sep=';')
#display(np.round(data.describe()))


fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='volatile acidity', data=pd.read_csv("data/winequality-red.csv",sep=';'), ax=axs)
plt.title('quality VS volatile acidity')
plt.tight_layout()
plt.show()
plt.gcf().clear()
