import gym
import numpy as np


#HYPERPARAMETERS
EPISODES = 5000

epsilon = 1




#Initializing the environment
env = gym.make('Pendulum-v0')

#PART 1: Preparing our Q-table
#In this scenario we are dealing with actions of continuous values, not discrete values such as in the case of MountainCar. Hence, we will need
#to split the actions into discrete values. Same for observations

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
DISCRETE_AS_SIZE = [20] * len(env.action_space.high)

#Returns to us the size of a single bucket
discrete_os_win_size =  (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE
# discrete_as_win_size = (env.action_space.high - env.action_space.low) / DISCRETE_AS_SIZE

#Initializing our q-table
q_table = np.random.uniform(low=-2, high=0, size = (DISCRETE_OS_SIZE + DISCRETE_AS_SIZE))

#Making the states discrete so we can easily index the q-table later on
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

#Step 2. Building the q-learning algorithm

done = False
while not done:

