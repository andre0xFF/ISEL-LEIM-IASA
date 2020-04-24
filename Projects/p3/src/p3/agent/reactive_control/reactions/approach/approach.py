from agent.reactive_control.reactions.approach.approach_direction import ApproachDirection

from psa.actuador import FRT as FRONT
from psa.actuador import ESQ as LEFT
from psa.actuador import DIR as RIGHT
from ecr import Priority


class Approach(Priority):

    def __init__(self):
        super(Approach, self).__init__([
            ApproachDirection(FRONT),
            ApproachDirection(LEFT),
            ApproachDirection(RIGHT),
        ])
