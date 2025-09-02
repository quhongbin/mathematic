import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import rcParams

# 定义字体
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 定义常数 e
e = math.e

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 第一个图: x -> ∞
x1 = np.linspace(1, 1000, 1000)  # x从1到1000
y1 = (1 + 1/x1)**x1
ax1.plot(x1, y1, label=r'$y = (1 + \frac{1}{x})^x$')
ax1.axhline(y=e, color='r', linestyle='--', label=r'$y = e$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('$x \\to \infty$')
ax1.legend()
ax1.grid(True)

# 第二个图: x -> 0
x2 = np.linspace(0.001, 1, 1000)  # x从0.001到1，避免x=0
y2 = (1 + x2)**(1/x2)
ax2.plot(x2, y2, label=r'$y = (1 + x)^{\frac{1}{x}}$')
ax2.axhline(y=e, color='r', linestyle='--', label=r'$y = e$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('$x \\to 0$')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()