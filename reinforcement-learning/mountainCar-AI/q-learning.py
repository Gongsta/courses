#Q-Learning integration of the MountainCar solution
import numpy as np
import gym
import matplotlib.pyplot as plt

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 40000

SHOW_EVERY = 5000
RECORD_EVERY = 100

epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2
epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

ep_rewards = []
aggr_ep_rewards = {'ep':[], 'avg':[], 'min':[], 'max':[]}


#initializing the environment
env = gym.make('MountainCar-v0')
# env = gym.wrappers.Monitor(env, "./vid", video_callable=lambda episode_id: True, force=True)
recorder = gym.wrappers.monitoring.video_recorder.VideoRecorder(env = env, enabled=True, base_path='./mountainCar20')

#STEP 1. Build a Q-table of Q-values for each action possible per state.
"""
In this MoutainCar scenario, the environment returns 
2 observations in the form of a numpy array per step, with values of the observation ranging from env.observation_space.high to env.observation_space.low.
However, there are 8 decimal digits per observation, so if we were to build a Q-table using all possible Q-values determined by all possible 
states with all possible actions, it would be too much to compute. 

Hence, for the purpose of this environment, the q-table has been cut into buckets for all the possible observations. 
We do this below, splitting only for the observations and not for the actions since there are only 3 possible actions. 
The observations, on the other hand, has been split into 20 buckets, However, since there isn't 1 observation, there's 2 observations in this environment per step,
the final shape of the observations is  (20x20) because the len(env.observation_space.high or .low) is 2. If a environment n observations per step, the observations size would be (20x20x20...x20)
n times. 

--> To help you visualize a Q-table, think of the rows as the possible Observations and the columns as the possible actions. Each cell is a q-value for a possible state
for a possible action. The q-table becomes huge when there's more and more possible observations and actions.

--> We are building a Q-table of discrete values to accelerate the learning process.

**20 is an arbitrary number determined for a bucket**
"""

#OS stands for Observation Space. This gives us the number of buckets we need.
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)  #in this case same thing as [20,20]. We just want to automate this to other environments as well

#Gives us the size of each bucket
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

#(20x20x3), multiplied by 3 for the number of actions. Initializing the q_table with random values of the appropriate size
#
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))


#We use this function because the original env.reset() value has too many decimal values. This will accelerate the learning process
def get_discrete_state(state):
    #This seemed confusing at first, but internalize it!
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))


#Step 2. Training our AI by updating the Q-table
for episode in range(EPISODES):
    episode_reward = 0
    #Only show at every 2000 episodes by calling env.render() else it will take too much time
    if episode % SHOW_EVERY == 0 :
        render = True
        print(episode)

    else:
        render = False

    if episode % RECORD_EVERY == 0 :
        record = True

    else:
        record = False

    discrete_state = get_discrete_state(env.reset())
    done = False


    #Iteration of steps
    while not done:
        #Rendering the environment
        if render:
            env.render()

        if record:
            recorder.capture_frame()

        #Applying epsilon to encourage exploration, so the AI may find a more efficient solution.
        if np.random.random() > epsilon:
            # We take the argmax because it returns us the q-values for all possible actions, we want to take the "best" (highest valued) action based on the given discrete state.
            # Remember, q_table.shape = (20,20,3). This way you can easily index the table using the 20x20 possible observations
            action = np.argmax(q_table[discrete_state])

        else:
            action = np.random.randint(0, env.action_space.n)

        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        new_discrete_state = get_discrete_state(new_state)


        if not done:
            #Future max Q-value gets back-propagated, will be used in the equation below
            max_future_q = np.max(q_table[new_discrete_state])

            current_q = q_table[discrete_state + (action, )]

            #Using the formula for updating q-values.
            """
            DISCOUNT: Measure of how much we want to care about FUTURE reward rather than immediate rewards. Usually fairly high (because we put greater importance on long term gains) and between 0 and 1. 
            """
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

            #Updating the q-table
            q_table[discrete_state + (action, )] = new_q

        #This is specific to our environment. If goal position is achieved, update Q value with reward directly.
        elif new_state[0] >= env.goal_position:
            print(f"We made it on episode {episode}")
            q_table[discrete_state + (action, )] = 0


        #Updating the state
        discrete_state = new_discrete_state

    #Decaying is being done so that the model slowly shifts from exploration to exploitation.
    if END_EPSILON_DECAYING >- episode >= START_EPSILON_DECAYING :
        epsilon -= epsilon_decay_value

    #Part 3. Visualizing results
    #Section of rewards to determine overall performance of model
    ep_rewards.append(episode_reward)

    if not episode % SHOW_EVERY:
        average_reward = sum(ep_rewards[-SHOW_EVERY:]) / len(ep_rewards[-SHOW_EVERY:])
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(average_reward)
        aggr_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))
        aggr_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))

        print(f"Episode: {episode} Average: {average_reward} min:{min(ep_rewards[-SHOW_EVERY:])} max: {max(ep_rewards[-SHOW_EVERY:])}")

    #Saving the q-table every 10 episdoes
    # if episode % 10 == 0:
    #     np.save(f"qtables/{episode}-qtable.npy", q_table)
recorder.close()
env.close()

#Visualizing results on matplotlib
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label='avg')
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label='min')
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label='max')
plt.legend()
plt.show(block=True)