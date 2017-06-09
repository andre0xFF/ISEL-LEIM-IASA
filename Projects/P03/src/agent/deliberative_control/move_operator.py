from accao import Mover
from psa5 import dist
from pee.modprob.operador import Operador


class MoveOperator(Operador):

    def __init__(self, world_model, angle):
        self._world_model = world_model
        self._angle = angle
        self._action = Mover(angle, ang_abs=True)

    @property
    def action(self):
        return self._action

    def aplicar(self, state):
        new_state = Mover.mover(self._state, self._angle)
        element = self._world_model.obtain_elements(state)

        if element is not 'obs':
            return new_state

        return None

    def custo(self, state, new_state):
        return max(dist(state, new_state), 1)
