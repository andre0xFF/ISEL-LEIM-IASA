import actuador
import util
from lib.ecr.reaction import Reaction
from lib.ecr.response import Response


class Bypass(Reaction):
    # Translation: contornar

    def detect_stimulus(self, perception):
        return perception[actuador.ESQ].contacto and perception[actuador.ESQ].obstaculo or \
               perception[actuador.DIR].contacto and perception[actuador.DIR].obstaculo

    def generate_response(self, stimulus):
        action = util.Mover(actuador.FRT)
        return Response(action)
