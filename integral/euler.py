import matplotlib.pyplot as plt
import numpy as np

data=np.linspace(-2*np.pi,2*np.pi)
fig=plt.figure()
ax=fig.add_subplot(projection="3d")

sin_val=np.sin(data)
cos_val=np.cos(data)

ax.plot(cos_val,sin_val,data)

ax.set_xlabel("it's x轴")
ax.set_ylabel("it's y轴")
ax.set_zlabel("z轴")
ax.axline([0,0],[0,1])
plt.show()