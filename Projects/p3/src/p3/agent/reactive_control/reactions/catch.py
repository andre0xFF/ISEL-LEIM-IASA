from agent.reactive_control.reactions.approach.approach import Approach
from agent.reactive_control.reactions.avoid import Avoid
from agent.reactive_control.reactions.bypass import Bypass
from agent.reactive_control.reactions.explore import Explore
from ecr import Hierarchy


class Catch(Hierarchy):
    # Translation: recolher

    def __init__(self):
        super().__init__([
            Approach(),
            Avoid(),
            Bypass(),
            Explore(),
        ])
