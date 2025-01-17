import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from scores.score_logger import ScoreLogger

ENV_NAME = "Acrobot-v1"

GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995


class DQNSolver:

    def __init__(self, observation_space, action_space):
        self.exploration_rate = EXPLORATION_MAX

        self.action_space = action_space
        self.memory = deque(maxlen=MEMORY_SIZE)

        self.model = Sequential()
        self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
        self.model.add(Dense(24, activation="relu"))
        self.model.add(Dense(self.action_space, activation="linear"))
        self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE))

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:
            return random.randrange(self.action_space)
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, state_next, terminal in batch:
            q_update = reward
            if not terminal:
                q_update = (reward + GAMMA * np.amax(self.model.predict(state_next)[0]))
            q_values = self.model.predict(state)
            q_values[0][action] = q_update
            self.model.fit(state, q_values, verbose=0)
        self.exploration_rate *= EXPLORATION_DECAY
        self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)


def cartpole():
    #Creating the gym environment
    env = gym.make(ENV_NAME)

    env = gym.wrappers.Monitor(env, "./vid", video_callable=lambda episode_id: True, force=True)

    #initializing the score logger to visualize later on the performance of the AI
    score_logger = ScoreLogger(ENV_NAME)

    """
        Observation: 
        Type: Box(4)
        Num	Observation                 Min         Max
        0	Cart Position             -4.8            4.8
        1	Cart Velocity             -Inf            Inf
        2	Pole Angle                 -24 deg        24 deg
        3	Pole Velocity At Tip      -Inf            Inf
        
    Actions:
        Type: Discrete(2)
        Num	Action
        0	Push cart to the left
        1	Push cart to the right
        
    """
    #There are 4 possible observations in this environment, so observation space will be equal to 4
    observation_space = env.observation_space.shape[0]
    #There are 2 possible actions, moving to the left and moving to the right as seen above
    action_space = env.action_space.n
    #DQNSolver is the "AI", the agent that from the list of observations and actions will try to determine the best actions for given circumstances (observation)
    #Initializing the dqn_solver
    dqn_solver = DQNSolver(observation_space, action_space)
    #Run is a variable to track how many runs it has been
    run = 0
    while True:
        run += 1
        #When you call env.reset(), it returns the initial state as a np.ndarray of shape (4,) since there are 4 observations
        state = env.reset()
        #Reshaping the state into a 2d array of (1,4)
        state = state.reshape(1, observation_space)
        step = 0
        while True:
            #Each step is a new action undertaken by the agent
            step += 1
            env.render()
            action = dqn_solver.act(state)
            state_next, reward, terminal, info = env.step(action)
            reward = reward if not terminal else -reward
            state_next = np.reshape(state_next, [1, observation_space])
            dqn_solver.remember(state, action, reward, state_next, terminal)
            state = state_next
            if terminal:
                print("Run: " + str(run) + ", exploration: " + str(dqn_solver.exploration_rate) + ", score: " + str(step))
                score_logger.add_score(step, run)
                break
            dqn_solver.experience_replay()

    env.close()


if __name__ == "__main__":
    cartpole()
