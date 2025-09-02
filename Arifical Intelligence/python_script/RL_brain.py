import random
import numpy as np
import gymnasium as gym



class CustomReward(gym.Wrapper):
    def step(self, action):
        obs, reward, terminated,truncated, info = self.env.step(action)
        new_reward = -0.1
        if obs == 15:
            new_reward = reward + 5
        if terminated or truncated:
            new_reward = reward -1
        return obs, new_reward, terminated,truncated, info

class QLearning:
    def __init__(self,action_space,state_space,n_training_episodes=100,learning_rate=0.7,gamma=0.95,max_steps=99,max_epsilon=1.0,min_epsilon=0.05,decay_rate=0.0005):
        self.n_training_episodes = n_training_episodes  # 训练回合数
        self.learning_rate = 0.7          # 学习率
        self.gamma = 0.95                 # 折扣因子
        self.max_steps = 99               # 每回合最大步数
        self.max_epsilon = 1.0            # 初始探索概率
        self.min_epsilon = 0.05           # 最小探索概率
        self.decay_rate = 0.0005          # 探索概率衰减率
        self.q_table=np.zeros((state_space,action_space))

    def train(self,env):
        for episode in range(self.n_training_episodes):
            # 初始化环境
            state, _ = env.reset()
            done = False
            total_reward = 0
            step = 0 
            while step < self.max_steps:
                # 选择动作
                action = self.choose_action(state,env)
                # 执行动作
                next_state, reward, terminated, truncated, _ = env.step(action)
                print(action,reward,total_reward)
                
                done = terminated or truncated
                # 更新Q表
                self.q_table[state, action] = self.q_table[state, action] + self.learning_rate * (
                    reward + self.gamma * np.max(self.q_table[next_state]) - self.q_table[state, action]
                )
                # 状态转移
                state = next_state
                if done:
                    total_reward = reward - 0.1
                    break
                total_reward += reward
                if step == self.max_steps:
                    step = 0
                    break
                else:
                    step +=step
    def choose_action(self,state,env):

        # 探索-利用策略
        if np.random.uniform(0, 1) < 0.2:
            return random.randint(0, env.action_space.n - 1)  # 探索：随机选择动作
        else:
            return np.argmax(self.q_table[state])  # 利用：选择Q值最大的动作