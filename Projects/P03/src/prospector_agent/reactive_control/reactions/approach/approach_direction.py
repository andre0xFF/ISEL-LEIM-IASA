# TODO: imports

import sys

sys.path.append('../lib/ecr')
# sys.path.append('../lib/psa')


class ApproachDirection(Reaction):

    def __init__(self, direction):
        self._direction = direction
        self._action = Mover(action)

    def detect_stimulus(self, perception):
        if perception[self._direction].alvo:
            return perception[self._direction].distancia

    def generate_response(self, stimulus):
        priority = 1 / (1 + stimulus)
        return Response(self._action, priority)
