import gym
import numpy as np



env = gym.make("chrome_trex:Chrome_Trex-v0")



env.setgoal = 50
n_states = (600*150)/4
episodes = 1

initial_lr = 1.0
min_lr = 0.005
gamma = 0.99
max_steps = 300
epsilon = 0.05

env = env.unwrapped
env.seed(0)
np.random.seed(0)

def discrete(env, obs):
    env_low = np.array([0.01, -10.9],dtype='float64')
    env_high = np.array([0.1, 12],dtype='float64')
    env_den = (env_high-env_low)/n_states
    x_den = env_den[0]
    y_den = env_den[1]
    x_high = env_high[0]
    x_low = env_low[0]
    y_high = env_high[1]
    y_low = env_low[1]
    x_scaled = int((obs[0]-x_low)/x_den)
    y_scaled = int((obs[1]-y_low)/y_den)
    return x_scaled, y_scaled

q_table = np.zeros((n_states,n_states,env.action_space.n))
total_steps = 0
for episode in range(episodes):
    obs = env.reset()
    total_reward = 0
    alpha = max(min_lr,initial_lr*(gamma**(epsilon//100)))
    steps=0
    while True:
        env.render()
        x, y = discrete(env,obs)
        if np.random.uniform(low=0,high=1) < epsilon:
            a = np.random.choice(env.action_space.n)
        else:
            a = np.argmax(q_table[x][y])
        obs,reward,terminate,_=env.step(a)
        print(obs)
        total_reward += abs(obs[0]+0.5)
        x_,y_ = discrete(env,obs)
        q_table[x][y][a]  = (1-alpha)*q_table[x][y][a] + alpha*(reward+gamma*np.max(q_table[x_][y_]))
        steps +=1
        if terminate:
            break
    print("Episode {} completed with total reward {} in {} steps.".format(episode+1,total_reward,steps))
while True:
    env.render()
