from reinforcement_learning.memory.learning_memory import LearningMemory


class SparseMemory(LearningMemory):
    # Desorganized memory

    def __init__(self, value_omission=0.0):
        self._value_omission = value_omission
        self._memory = {}

    def update(self, state, action, q):
        self._memory[(state, action)] = q

    def acquire(self, state, action):
        q = self._memory.get((state, action))

        if q is not None:
            return q
        else:
            return self._value_omission

    @property
    def memory(self):
        return self._memory
