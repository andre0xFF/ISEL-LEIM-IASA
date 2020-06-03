from .. import ReinforcementLearning


class QLearning(ReinforcementLearning):

    def __init__(self, learning_memory, action_selection, alpha, gamma):
        super(QLearning, self).__init__(learning_memory, action_selection)
        self._alpha = alpha
        self._gamma = gamma

    def learn(self, state, action, r, next_state):
        next_action = self._action_selection.max_action(next_state)
        qsa = self._learning_memory.acquire(state, action)
        qsnan = self._learning_memory.acquire(next_state, next_action)
        q = qsa + self._alpha * (r + self._gamma * (qsnan - qsa))
        self._learning_memory.update(state, action, q)
