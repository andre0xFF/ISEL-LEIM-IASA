from psa5.util import mover
from psa5.util import dist
from psa5.accao import Mover
from pee.modprob.operador import Operador


class MoveOperator(Operador):

    def __init__(self, world_model, angle):
        self._world_model = world_model
        self._angle = angle
        self._action = Mover(angle, ang_abs=True)

    @property
    def action(self):
        return self._action

    # Overwrite
    def aplicar(self, state):
        new_state = mover(state, self._angle)
        element = self._world_model.obtain_elements(new_state)

        if element in ['vazio', 'alvo']:
            return new_state

        return None

    # Overwrite
    def custo(self, state, new_state):
        return max(dist(state, new_state), 1)
