import matplotlib.pyplot as plt
import numpy as np
# input_angle=int(input('请输入角度数值:'))
# angle=np.pi/180
# rad=180/np.pi
# var_angle=input_angle*angle

# print(var_angle/np.pi)

x=np.arange(-100,100,0.1)
y=np.sin(x)/x
plt.axvline(0,color="#ff0000")
plt.axhline(0,color="#ff0000")
plt.title(r'assume  $\lim_{x \to \infty}f\left(x\right)=\frac{sin(x)}{x}$')
plt.xticks()
plt.plot(x,y)
plt.show()






