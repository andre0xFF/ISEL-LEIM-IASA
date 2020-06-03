from ..control import Control


class ReactiveControl(Control):

    def __init__(self, behaviour):
        self._behaviour = behaviour

    def process(self, perception):
        response = self._behaviour.activate(perception)

        if response is not None:
            return response.action
