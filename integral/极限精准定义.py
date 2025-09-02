import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 定义字体
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 定义函数
def f(x):
    return x**2

a = 2
L = 4
epsilon = 0.5

# 计算delta
x_lower = np.sqrt(L - epsilon)
x_upper = np.sqrt(L + epsilon)
delta = min(a - x_lower, x_upper - a)
print(f"对于 ε={epsilon}, 找到 δ={delta:.3f}")

# 创建x值
x = np.linspace(1.5, 2.5, 400)
y = f(x)

# 绘制函数
plt.plot(x, y, label='$f(x) = x^2$')
plt.axvline(x=a, color='gray', linestyle=':', label='$x = a$')
plt.axhline(y=L, color='gray', linestyle=':', label='$y = L$')
plt.plot(a, L, 'ro', label='点 (2,4)')

# 绘制ε带
plt.axhline(y=L - epsilon, color='r', linestyle='--', label='$L - \epsilon$')
plt.axhline(y=L + epsilon, color='r', linestyle='--', label='$L + \epsilon$')
plt.fill_between(x, L - epsilon, L + epsilon, color='red', alpha=0.2, label='$\epsilon$ 区域')

# 绘制δ区间
plt.axvline(x=a - delta, color='g', linestyle='--', label='$a - \delta$')
plt.axvline(x=a + delta, color='g', linestyle='--', label='$a + \delta$')
plt.fill_betweenx(y, a - delta, a + delta, color='green', alpha=0.2, label='$\delta$ 区域')

# 标签和标题
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('ε-δ定义图解 for $f(x)=x^2$ at $x=2$')
plt.legend()
plt.grid(True)
plt.show()