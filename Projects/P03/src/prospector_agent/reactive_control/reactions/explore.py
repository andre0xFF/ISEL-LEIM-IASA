from random import choice

import actuador
import util
from lib.ecr.behaviour import Behaviour
from lib.ecr.response import Response


class Explore(Behaviour):

    def __init__(self, perception):
        action = choice([
            util.Mover(actuador.ESQ),
            util.Mover(actuador.FRT),
            util.Mover(actuador.DIR)
        ])

        return Response(action)
