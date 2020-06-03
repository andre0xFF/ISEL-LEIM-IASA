from psa.accao import Mover as Move
from psa.actuador import DIR as RIGHT
from psa.actuador import ESQ as LEFT
from psa.actuador import FRT as FRONT

from .. import Response
from ..behaviours import Reaction


class Bypass(Reaction):
    # Translation: contornar

    def _detect_stimulus(self, perception):
        return perception[LEFT].contacto and perception[LEFT].obstaculo or \
               perception[RIGHT].contacto and perception[RIGHT].obstaculo

    def _generate_response(self, stimulus):
        action = Move(FRONT)
        return Response(action)
