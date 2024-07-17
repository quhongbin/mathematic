import matplotlib.pyplot as plt
import numpy as np


fig,ax=plt.subplots(2,2)
x_data=np.linspace(0,2*np.pi)

x_val=np.cos(x_data)
y_val=np.sin(x_data)
#反三角函数
arc_x_data=np.linspace(-1,1)
arccos_val=np.arccos(arc_x_data)  #sec
arcsin_val=np.arcsin(arc_x_data)  #csc



#设置三角函数0到2pi的标签
radian_ticks=np.arange(0,2*np.pi+np.pi/2,np.pi/2)
radian_tickslabels=[r'$0$',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$']



#设置反三角函数的定义域
arc_radian_ticks_x=np.arange(-1,2,1)



#设置arcsin的y轴的取值范围以及标签
arcsin_radian_ticks_y=np.arange(-np.pi/2,np.pi,np.pi/2)
arcsin_radian_tickslabels=[r'$-\frac{\pi}{2}$',r'$0$',r'$\frac{\pi}{2}$']



#设置arccos的y轴的取值范围以及标签
arccos_radian_ticks_y=np.arange(0,2*np.pi,np.pi)
arccos_radian_tickslabels=[r'$0$',r'$\frac{\pi}{2}$']




#cos函数图像
ax[0,0].plot(x_data,x_val)
ax[0,0].set_xticks(radian_ticks)
ax[0,0].set_xticklabels(radian_tickslabels)
ax[0,0].set_title(r'$f(x)=sin(x)$')


#sin函数图像
ax[0,1].plot(x_data,y_val)
ax[0,1].set_xticks(radian_ticks)
ax[0,1].set_xticklabels(radian_tickslabels)
ax[0,1].set_title(r'$f(x)=cos(x)$')


#arcsin函数图像
ax[1,0].plot(arc_x_data,arcsin_val)
ax[1,0].set_xticks(arc_radian_ticks_x)
ax[1,0].set_yticks(arcsin_radian_ticks_y)
ax[1,0].set_yticklabels(arcsin_radian_tickslabels)
ax[1,0].set_xlabel(r'$f(x)=arcsin(x)$')


#arccos函数
ax[1,1].plot(arc_x_data,arccos_val)
ax[1,1].set_xticks(arc_radian_ticks_x)
ax[1,1].set_yticks(arccos_radian_ticks_y)
ax[1,1].set_yticklabels(arccos_radian_tickslabels)
ax[1,1].set_xlabel(r'$f(x)=arccos(x)$')


plt.show()
# import numpy as np
# print(np.arcsin(-1))