from prospector_agent.reactive_control.reactions.approach.approach_direction import ApproachDirection

import actuador
from lib.ecr.priority import Priority


class Approach(Priority):

    def __init__(self):
        super(Approach, self).__init__([
            ApproachDirection(actuador.FRT),
            ApproachDirection(actuador.FRT),
            ApproachDirection(actuador.FRT),
        ])
