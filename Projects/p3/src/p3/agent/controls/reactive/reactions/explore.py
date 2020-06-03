from random import choice

from psa.accao import Mover as Move
from psa.actuador import DIR as RIGHT
from psa.actuador import ESQ as LEFT
from psa.actuador import FRT as FRONT

from ..behaviour import Behaviour
from ..response import Response


class Explore(Behaviour):

    def activate(self, perception):
        action = choice([
            Move(LEFT),
            Move(FRONT),
            Move(RIGHT)
        ])

        return Response(action)
