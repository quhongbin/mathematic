import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation
x=np.linspace(0,np.pi*500)
y=np.sin(x)
fig = plt.figure(figsize=([16,8]))    #图纸大小16:8
fig.subplots_adjust(hspace=0.3,wspace=0.2)
ax=fig.add_subplot()

arts=[]
for i in range (20):
    Y=y
    lines=ax.plot(Y,c="#ff0000")
    arts.append(lines)


ani=ArtistAnimation(fig,arts,interval=100)
plt.show()




