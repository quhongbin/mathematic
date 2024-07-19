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
fig=plt.figure(figsize=([16,8]))    #图纸大小16:8
fig.subplots_adjust(hspace=0.3,wspace=0.2)
plt.subplot(2,1,1)                  #子图2行1列 当前位置1
plt.axvline(0,color="#ff0000")      #把Y=0的垂直线以红色显示出来
plt.axhline(0,color="#ff0000")      #把X=0的水平线以红色显示出来
plt.title(r'assume  $\lim_{x \to \infty}f\left(x\right)=\frac{sin(x)}{x}$')     #Latex的数学表达式sin(x)/x
plt.xticks()        #X轴的数值显示
plt.plot(x,y)       #绘制图形f(x)=sin(x)/x
plt.annotate("non-value",(0.0,1.0),(5.0,1.0),arrowprops=dict(arrowstyle="->"))    #规定在x=0处没有意义


plt.subplot(2,1,2)                  #子图2行1列 当前位置2
tan_val_y=np.tan(x)/x               #f(x)=tan(x)/x
plt.plot(x,tan_val_y)               #绘制图形f(x)=tan(x)/x
plt.title(r'assume  $\lim_{x \to \infty}f\left(x\right)=\frac{tan(x)}{x}$')     #Latex的数学表达式tan(x)/x
plt.axhline(1,-100,100,color="#ff0000")
plt.annotate("y=1",[-100,1],[-100,5],arrowprops=dict(arrowstyle="->"))
plt.show()



