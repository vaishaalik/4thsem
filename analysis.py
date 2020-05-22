import matplotlib.pyplot as plt
from gcpgy import tt
gtt=tt
from gcpbt import tt
btt=tt
import numpy as np

alg=['greedy', 'backtracking']
tt=[gtt,btt]
ypos=np.arange(len(alg))
plt.xticks(ypos,alg)
plt.ylabel("Time(s)")
plt.xlabel("greedy vs backtracking")
plt.title ("Effeciencies Analysis of greedy vs backracking algorithms")
l=plt.bar(ypos,tt)
l[0].set_color('r')
plt.legend()
plt.show()
