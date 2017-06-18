class Response():

    def __init__(self, action, priority=0):
        self._action = action
        self._priority = priority

    @property
    def action(self):
        return self._action

    @property
    def priority(self):
        return self._priority
