from prospector_agent.reactive_control.reactions.approach.approach import Approach
from prospector_agent.reactive_control.reactions.avoid import Avoid
from prospector_agent.reactive_control.reactions.bypass import Bypass
from prospector_agent.reactive_control.reactions.roam import Roam

from lib.ecr.hierarchy import Hierarchy


class Behaviours(Hierarchy):
    # Translation: recolher

    def __init__(self):
        super(Behaviours, self).__init__([
            Approach(),
            Avoid(),
            Bypass(),
            Roam()
        ])
