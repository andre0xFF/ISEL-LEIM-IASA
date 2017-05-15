# TODO: Add imports

import random
import sys
sys.path.append('../lib/psa')
from psa.actuador import ESQ, FRT, DIR
from psa.accao import Mover


class Roam(Behaviour):

    def __init__(self, perception):
        action = choice([
            Mover(ESQ),
            Mover(FRT),
            Mover(DIR)
        ])

        return Response(action)
