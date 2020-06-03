from .. import ReinforcementLearning


class QELearning(ReinforcementLearning):

    def __init__(self, learning_memory, action_selection, alpha, gamma, nsim):
        self._learning_memory = learning_memory
        self._action_selection = action_selection
        self._alpha = alpha
        self._gamma = gamma
        self._nsim = nsim

    def learn(self, state, action, r, next_state):
        pass

    def _memorise_episode(self, state, action, r, next_state):
        pass

    def _simulate(self):
        pass
