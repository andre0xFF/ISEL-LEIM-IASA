from psa import vismod
from psa import visvec
from learning.selections.greedy import Greedy
from learning.mechanisms.q_learning import QLearning
from learning.memories.sparse_memory import SparseMemory


class LearningMechanism():

    def __init__(self, actions, alpha=1, gamma=0.9, epsilon=0.01, nsim=100):
        self._actions = actions
        self._learning_memory = SparseMemory()
        self._action_selection = Greedy(self._learning_memory, actions, epsilon)
        self._reinforcement_learning = QLearning(self._learning_memory, self._action_selection, alpha, gamma)
        self._nsim = nsim

    def learn(self, s, a, r, sn):
        self._reinforcement_learning.learn(s, a, r, sn)

    def select_action(self, s):
        return self._action_selection.select_action(s)

    def show(self, s):
        vismod.limpar()
        vismod.aprendref(self._reinforcement_learning)
        visvec.accoesestado(s, self._actions, self._learning_memory.memory)
