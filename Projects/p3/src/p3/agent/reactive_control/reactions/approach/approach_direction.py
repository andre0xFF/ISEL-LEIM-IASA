import accao
from lib.ecr.reaction import Reaction
from lib.ecr.response import Response


class ApproachDirection(Reaction):

    def __init__(self, direction):
        self._direction = direction
        self._action = accao.Mover(self._direction)

    def _detect_stimulus(self, perception):
        if perception[self._direction].alvo:
            return perception[self._direction].distancia

    def _generate_response(self, stimulus):
        priority = 1 / (1 + stimulus)
        return Response(self._action, priority)
