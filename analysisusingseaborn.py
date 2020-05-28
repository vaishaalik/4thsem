import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('10.csv')
sns.set(style='darkgrid')
ax = sns.catplot(x="alg", y="runtime",data = df,kind='box')
ax.set(ylim=(1,None))
plt.xticks(rotation=-15)
plt.show()
