from random import choice
from random import random
from random import shuffle
from .. import ActionSelection


class Greedy(ActionSelection):

    def __init__(self, learning_memory, actions, epsilon):
        self._learning_memory = learning_memory
        self._actions = actions
        self._epsilon = epsilon

    def select_action(self, state):
        if random() > self._epsilon:
            # Greed
            action = self.max_action(state)
        else:
            # Explore
            action = self.explore(state)

        return action

    def max_action(self, state):
        shuffle(self._actions)
        return max(self._actions, key=lambda action: self._learning_memory.acquire(state, action))

    def explore(self, state):
        return choice(self._actions)
