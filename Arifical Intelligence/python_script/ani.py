import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
import os
from contextlib import contextmanager

FILENAME = os.path.basename(__file__).split('.')[0]
DIROFFILE = os.path.dirname(__file__)
@contextmanager
def change_directory(new_path):
    original_path = os.getcwd()
    try:
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        os.chdir(new_path)
        yield
    finally:
        os.chdir(original_path)


# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 创建图形和坐标轴
fig, (ax,ax2) = plt.subplots(figsize=(8,6), dpi=100,nrows=2, ncols=1)
fig.suptitle('正弦波动画 - FuncAnimation 示例', fontsize=16)

# 初始化数据
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot(x, np.sin(x), 'b-', linewidth=2, label='正弦波')
line2, = ax2.plot(x, np.cos(x), 'r-', linewidth=2, label='余弦波')
point, = ax.plot([], [], 'ro', markersize=8)

# 添加网格和标签
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_xlabel('X轴', fontsize=12)
ax.set_ylabel('Y轴', fontsize=12)
ax.set_title('动态正弦波演示', fontsize=14)
ax.legend(loc='upper right')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# 添加文本说明
info_text = ax.text(0.0, 1.1, '', transform=ax.transAxes, ha='center', fontsize=12)

# 设置cosine wave subplot
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_title('余弦波', fontsize=14)
ax2.set_xlim(0, 2 * np.pi)
ax2.set_ylim(-1.5, 1.5)
ax2.legend(loc='upper right')
# 动画更新函数
def update(frame):
    # 更新正弦波
    y = np.sin(x + frame * 0.1)
    line.set_ydata(y)
    y2 = np.cos(x + frame * 0.1)   
    line2.set_ydata(y2)
    # 更新移动点
    point_x = frame * 0.1 % (2 * np.pi)
    point.set_data([point_x], [np.sin(point_x)])
    
    # 更新文本
    info_text.set_text(f'帧: {frame}/100 | 相位: {frame * 0.1:.1f} rad')
    
    return line,line2,point, info_text

# 创建动画
ani = FuncAnimation(
    fig, 
    update, 
    frames=100,  # 帧数
    interval=1,  # 帧间隔(ms)
    blit=True,    # 优化渲染
    repeat=True,
)

plt.tight_layout()
# with change_directory(f"{DIROFFILE}/images/{FILENAME}"):
#     ani.save('sine_cosine_wave_animation.gif', writer='pillow', fps=30, dpi=100,)
plt.show()
print(os.getcwd())