import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-180,180,1)

fig=plt.figure(figsize=[16,8])


plt.plot(x,-1/x,'-',label='-1/x')
plt.plot(x,1/x,'-',label='1/x')
plt.plot(x,np.sin(x)/x,'-',label='sin(x)/x')
plt.legend()
plt.show()