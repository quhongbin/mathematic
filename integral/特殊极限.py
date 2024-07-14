import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation 
# input_angle=int(input('请输入角度数值:'))
# angle=np.pi/180
# rad=180/np.pi
# var_angle=input_angle*angle

# print(var_angle/np.pi)

x=np.arange(-100,100,0.1)
y=np.sin(x)/x
fig=plt.figure()
plt.axvline(0,color="#ff0000")      #把Y=0的垂直线以红色显示出来
plt.axhline(0,color="#ff0000")      #把X=0的水平线以红色显示出来
plt.title(r'assume  $\lim_{x \to \infty}f\left(x\right)=\frac{sin(x)}{x}$')     #Latex的数学表达式sin(x)/x
plt.xticks()        #X轴的数值显示
plt.plot(x,y)       #绘制图形f(x)=sin(x)/x
plt.annotate("buqu",(0.0,1.0),(5.0,1.0),arrowprops=dict(arrowstyle="->"))

plt.show()






