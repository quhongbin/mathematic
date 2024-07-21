import matplotlib.pyplot as plt
import numpy as np



fig=plt.figure()
ax=fig.add_subplot(projection="3d")
x=np.linspace(-5,5,5)
y=np.linspace(-5,5,5)
z=np.linspace(0,3,3)
X,Y=np.meshgrid(x,y)
ax.quiver(0,0,0,0,1,2,color="#ff0000",label="v")
ax.quiver(0,0,0,-1,3,4,color="#00ff00",label="w")
ax.quiver(0,0,0,0,-3,6,color="#0000ff",label="z")
Y_min=Y/2
ax.plot_surface(X,Y,Y*2,label="planV",alpha=0.2,color="#ff0000") ##记得绘制线性相关的图
ax.plot_surface(X,Y,Y*4/3,label="planW",alpha=0.2,color="#00ff00")
ax.plot_surface(X,Y,Y*-2,label="planZ",alpha=0.2,color="#0000ff")
#设置X,Y,Z轴标签
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
#设置各轴的值范围
ax.set_ylim(-12,12)
ax.set_xlim(-12,12)
ax.set_zlim(-12,12)
ax.view_init(elev=20,azim=50)
plt.legend()
plt.show()

