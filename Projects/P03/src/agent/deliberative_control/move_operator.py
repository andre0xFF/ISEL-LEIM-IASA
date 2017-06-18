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

    def aplicar(self, state):
        new_state = mover(state, self._angle)
        # TODO state / new_state ?
        element = self._world_model.obtain_elements(new_state)

        # if element is not 'obst':
        #     return new_state
        if element in ['vazio', 'alvo']:
            return new_state
        else:
            return None

        # return None

    def custo(self, state, new_state):
        return max(dist(state, new_state), 1)
