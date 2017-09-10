'''
Basic plotting
==============

'''

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,100,0.1)
plt.plot(x, np.sin(x))
