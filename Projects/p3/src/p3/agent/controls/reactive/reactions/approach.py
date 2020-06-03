from psa.actuador import DIR as RIGHT
from psa.actuador import ESQ as LEFT
from psa.actuador import FRT as FRONT

from ..behaviours import Priority
from .approach_direction import ApproachDirection


class Approach(Priority):

    def __init__(self):
        super(Approach, self).__init__([
            ApproachDirection(FRONT),
            ApproachDirection(LEFT),
            ApproachDirection(RIGHT),
        ])
