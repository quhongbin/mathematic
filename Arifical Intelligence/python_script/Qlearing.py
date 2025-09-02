"""
FrozenLake环境演示
这个脚本演示了如何使用OpenAI Gym的FrozenLake环境，并提供了可视化界面
"""
import numpy as np
from RL_brain import QLearning
import gymnasium as gym
import time
from RL_brain import CustomReward

def run_random_agent():
    """演示随机智能体在FrozenLake环境中的表现"""
    # 创建环境，使用human渲染模式以显示界面
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False, render_mode="human")
    env = CustomReward(env)
    action_space=env.action_space.n
    state_space=env.observation_space.n

    agent=QLearning(action_space,state_space,100)

    #重置环境
    state, _ = env.reset()

    # 运行随机智能体
    done = False
    
    print("演示开始: 随机智能体在冰冻湖面环境中")
    print("目标: 从起点(S)移动到目标(G)，同时避开洞(H)")
    print("控制: 程序自动执行随机动作")
    print("按窗口的关闭按钮可以退出演示")
    
    # 渲染初始状态
    env.render()

    time.sleep(0.5)  # 给用户一些时间看初始状态

    agent.train(env)
    print(agent.q_table)
    # 关闭环境
    env.close()

if __name__ == "__main__":
    print("冰冻湖面环境演示 - 随机智能体")
    print("使用Gym自带的渲染功能")
    run_random_agent()
