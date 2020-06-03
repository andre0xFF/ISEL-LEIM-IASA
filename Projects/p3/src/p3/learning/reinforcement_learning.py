class ReinforcementLearning(object):

    def __init__(self, learning_memory, action_selection):
        self._learning_memory = learning_memory
        self._action_selection = action_selection

    def learn(self, state, action, r, next_state):
        raise NotImplementedError("Abstract Method")
