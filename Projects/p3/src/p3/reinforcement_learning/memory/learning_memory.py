class LearningMemory(object):

    def update(self, state, action, q):
        raise NotImplementedError("Abstract Method")

    def acquire(self, state, action):
        raise NotImplementedError("Abstract Method")
