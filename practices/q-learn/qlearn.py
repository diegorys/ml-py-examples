import gym
import numpy as np

env = gym.make('NChain-v0')
env.reset()

def naive_sum_reward_agent(env, num_states, num_actions, num_episodes=500):
    # this is the table that will hold our summated rewards for
    # each action in each state
    r_table = np.zeros((num_states, num_actions))
    for g in range(num_episodes):
        s = env.reset()
        done = False
        while not done:
            if np.sum(r_table[s, :]) == 0:
                # make a random selection of actions
                a = np.random.randint(0, num_actions)
            else:
                # select the action with highest cummulative reward
                a = np.argmax(r_table[s, :])
            new_s, r, done, _ = env.step(a)
            r_table[s, a] += r
            s = new_s
    return r_table

qtable = naive_sum_reward_agent(env, 5, 2)
print(qtable)
