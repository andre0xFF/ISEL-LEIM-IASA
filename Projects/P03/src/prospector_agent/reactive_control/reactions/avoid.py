# TODO: imports

import sys
sys.path.append('../lib/ecr')
sys.path.append('../lib/psa')


class Avoid(Reaction):

    def __init__(self):
        pass

    def detect_stimulus(self, perception):
        return perception[FRT].contacto and perception[FRT].obstaculo

    def generate_response(self, stimulus):
        action = Rodar(ESQ)
        return Response(action)
