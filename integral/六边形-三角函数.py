import matplotlib.pyplot as plt
import numpy as np

r=1
x=np.cos(np.arange(9)/6*np.pi*2)
y=np.sin(np.arange(9)/6*np.pi*2)

plt.plot(x,y)
plt.show()