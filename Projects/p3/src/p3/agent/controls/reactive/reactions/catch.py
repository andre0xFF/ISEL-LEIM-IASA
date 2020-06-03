from ..behaviours import Hierarchy
from .approach import Approach
from .avoid import Avoid
from .bypass import Bypass
from .explore import Explore


class Catch(Hierarchy):
    # Translation: recolher

    def __init__(self):
        super().__init__([
            Approach(),
            Avoid(),
            Bypass(),
            Explore(),
        ])
