from ecr import Reaction
from ecr import Response
from psa.accao import Rodar as Turn
from psa.actuador import ESQ as LEFT
from psa.actuador import FRT as FRONT


class Avoid(Reaction):

    def _detect_stimulus(self, perception):
        return perception[FRONT].contacto and perception[FRONT].obstaculo

    def _generate_response(self, stimulus):
        action = Turn(LEFT)
        return Response(action)
