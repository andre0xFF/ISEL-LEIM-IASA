from random import choice

import accao
import actuador
from lib.ecr.behaviour import Behaviour
from lib.ecr.response import Response


class Explore(Behaviour):

    def activate(self, perception):
        action = choice([
            accao.Mover(actuador.ESQ),
            accao.Mover(actuador.FRT),
            accao.Mover(actuador.DIR)
        ])

        return Response(action)
