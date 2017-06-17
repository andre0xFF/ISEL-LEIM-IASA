from reinforcement_learning.action_selection.greedy_action_selection import GreedyActionSelection as ActionSelection
from reinforcement_learning.mechanisms.q_learning import QLearning as ReinforcementLearning
from reinforcement_learning.memory.sparse_memory import SparseMemory as LearningMemory
from reinforcement_learning.reinforcement_learning import ReinforcementLearning


class LearningMechanism():

    def __init__(self, actions, alpha=1, gamma=0.9, epsilon=0.01, nsim=100):
        self._learning_memory = LearningMemory()
        self._action_selection = ActionSelection(self._learning_memory, actions, epsilon)
        self._reinforcement_learning = ReinforcementLearning(self._learning_memory, self._action_selection, alpha, gamma)
        self._nsim = nsim

    def learn(self):
        self._reinforcement_learning.learn()

    def select_action(self):
        self._action_selection.select_action()
