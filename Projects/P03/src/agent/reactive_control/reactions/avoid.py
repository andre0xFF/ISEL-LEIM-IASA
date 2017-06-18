from lib.ecr.reaction import Reaction
from lib.ecr.response import Response

import actuador


class Avoid(Reaction):

    def detect_stimulus(self, perception):
        return perception[actuador.FRT].contacto and perception[actuador.FRT].obstaculo

    def generate_response(self, stimulus):
        action = actuador.Rodar(actuador.ESQ)
        return Response(action)
