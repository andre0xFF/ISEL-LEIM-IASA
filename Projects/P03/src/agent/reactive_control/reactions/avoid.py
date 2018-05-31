from lib.ecr.reaction import Reaction
from lib.ecr.response import Response

import actuador
import accao


class Avoid(Reaction):

    def _detect_stimulus(self, perception):
        return perception[actuador.FRT].contacto and perception[actuador.FRT].obstaculo

    def _generate_response(self, stimulus):
        action = accao.Rodar(actuador.ESQ)
        return Response(action)
