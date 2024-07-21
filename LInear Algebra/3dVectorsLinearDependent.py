import matplotlib.pyplot as plt
import numpy as np


matrix_vectors_zeors=np.array([[0,0,0],[0,0,0],[0,0,0]])
matrix_vectors=np.array([[1,1,6],[2,4,0],[3,5,6]])
Y,Z=np.meshgrid(matrix_vectors[:,1],matrix_vectors[:,2])
fig=plt.figure(figsize=[16,8])
ax=fig.add_subplot(projection="3d")



ax.quiver(matrix_vectors_zeors[:,0],matrix_vectors_zeors[:,1],matrix_vectors_zeors[:,2],
      matrix_vectors[:,0],matrix_vectors[:,1],matrix_vectors[:,2],color="#ff0000")
#设置各轴取值范围
ax.set_xlim(0,6)
ax.set_ylim(0,6)
ax.set_zlim(0,6)
#设置各轴坐标
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
plt.show()