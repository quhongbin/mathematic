import matplotlib
import matplotlib.pyplot as plt
import numpy
ax=plt.subplot()
thete=numpy.linspace(0,2*numpy.pi,120)
cos_x=numpy.cos(thete)
sin_x=numpy.sin(thete)
radian_ticks=numpy.arange(0,2*numpy.pi+numpy.pi/2,numpy.pi/2) #numpy.arange左闭右开区间
radian_tickslabels=[r'$0$',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$']
# 刻度值和刻度值的标签个数要一致
ax.set_xticks(radian_ticks)     #x的刻度为numpy.arange生成的五个数值
ax.set_xticklabels(radian_tickslabels)      #x的刻度标签为radian_tickslabels的五个值

plt.plot(thete,sin_x)
plt.show()