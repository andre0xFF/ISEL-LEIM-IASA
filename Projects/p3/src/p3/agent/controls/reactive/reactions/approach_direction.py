from psa.accao import Mover as Move

from .. import Response
from ..behaviours import Reaction


class ApproachDirection(Reaction):

    def __init__(self, direction):
        self._direction = direction
        self._action = Move(self._direction)

    def _detect_stimulus(self, perception):
        if perception[self._direction].alvo:
            return perception[self._direction].distancia

    def _generate_response(self, stimulus):
        priority = 1 / (1 + stimulus)
        return Response(self._action, priority)
