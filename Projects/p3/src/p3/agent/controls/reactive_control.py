from ..control import Control
from .reactive import Behaviour, Response


class ReactiveControl(Control):

    def __init__(self, behaviour: Behaviour):
        self._behaviour = behaviour

    def process(self, perception):
        response: Response = self._behaviour.activate(perception)

        if response is not None:
            return response.action
