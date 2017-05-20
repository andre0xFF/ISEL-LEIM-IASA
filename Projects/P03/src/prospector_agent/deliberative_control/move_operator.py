class MoveOperator():

    def MoveOperator(self, world_model, angle):
        self._world_model = world_model

    @property
    def action(self):
        return self._action

    def apply(self, state):
        pass

    def cost(self, state, new_state):
        pass
