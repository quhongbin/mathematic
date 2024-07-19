import matplotlib.pyplot as plt
import numpy as np

# 定义多个起点和向量的位置信息
start_points = np.array([[ 0 , 0 ],
                         [ 1 , 1 ], 
                         [-1 , 1 ], 
                         [-1 ,-1 ]])
vectors = np.array([[ 3  , 4 ],
                    [ 4  ,-2 ],
                    [-2  , 4 ],
                    [-3  ,-5 ]])     #非0起点的向量，需要加上起点向量

# 绘制多个向量
plt.quiver(start_points[:,0], start_points[:,1], vectors[:,0], vectors[:,1], angles='xy', scale_units='xy', scale=1)

plt.xlim(-6,6)
plt.ylim(-6,6)
# 添加轴标签和网格线
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# 显示图形
plt.show()
