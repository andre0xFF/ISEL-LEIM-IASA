from platform import dist

import accao
from pee.modprob.operador import Operador


class MoveOperator(Operador):

    def __init__(self, world_model, angle):
        self._world_model = world_model
        self._angle = angle
        self._action = accao.Mover(angle, ang_abs=True)

    @property
    def action(self):
        return self._action

    def apply(self, state):
        new_state = accao.Mover.mover(self._state, self._angle)
        element = self._world_model.obtain_elements(state)

        if element is not 'obs':
            return new_state

        return None

    def cost(self, state, new_state):
        return max(dist(state, new_state), 1)
