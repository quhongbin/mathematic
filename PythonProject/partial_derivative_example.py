import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义二元函数 f(x, y) = x² + 3y²
def f(x, y):
    return x**2 + 3 * y**2

# 计算偏导数
def partial_derivative_x(x):
    return 2 * x  # ∂f/∂x = 2x

def partial_derivative_y(y):
    return 6 * y  # ∂f/∂y = 6y

# 生成网格数据
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 创建3D图像
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制函数曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='函数值 f(x, y)')

# 选择可视化偏导数的点 (1, 1)
x0, y0 = 1, 1
z0 = f(x0, y0)
fx = partial_derivative_x(x0)  # 在点(1,1)处对x的偏导数
fy = partial_derivative_y(y0)  # 在点(1,1)处对y的偏导数

# 绘制x方向偏导数切线 (固定y=y0)
x_tangent = np.linspace(x0 - 1, x0 + 1, 10)
y_tangent = np.ones_like(x_tangent) * y0
z_tangent_x = z0 + fx * (x_tangent - x0)  # 切线方程
ax.plot(x_tangent, y_tangent, z_tangent_x, color='red', linewidth=3, label=f'对x的偏导数 (∂f/∂x = {fx})')

# 绘制y方向偏导数切线 (固定x=x0)
y_tangent2 = np.linspace(y0 - 1, y0 + 1, 10)
x_tangent2 = np.ones_like(y_tangent2) * x0
z_tangent_y = z0 + fy * (y_tangent2 - y0)  # 切线方程
ax.plot(x_tangent2, y_tangent2, z_tangent_y, color='blue', linewidth=3, label=f'对y的偏导数 (∂f/∂y = {fy})')

# 标记偏导数计算点
ax.scatter([x0], [y0], [z0], color='black', s=100, marker='o', label=f'计算点 ({x0}, {y0}, {z0})')

# 设置图像属性
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('二元函数的偏导数可视化示例')
ax.legend()

plt.show()