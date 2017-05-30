import accao
import actuador
from lib.ecr.reaction import Reaction
from lib.ecr.response import Response


class Bypass(Reaction):
    # Translation: contornar

    def _detect_stimulus(self, perception):
        return perception[actuador.ESQ].contacto and perception[actuador.ESQ].obstaculo or \
               perception[actuador.DIR].contacto and perception[actuador.DIR].obstaculo

    def _generate_response(self, stimulus):
        action = accao.Mover(actuador.FRT)
        return Response(action)
