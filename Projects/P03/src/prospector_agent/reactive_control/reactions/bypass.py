# TODO: Add imports

import sys
sys.path.append('../lib/ecr')
# sys.path.append('../lib/psa')
from behaviour import Behaviour


class Bypass(Reaction):

    def detect_stimulus(self, perception):
        return perception[ESQ].contacto and perception[ESQ].obstaculo or \
         perception[DIR].contacto and perception[DIR].obstaculo

    def generate_response(self, stimulus):
        action = Mover(FRT)
        return Response(action)
