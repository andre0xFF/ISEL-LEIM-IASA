from prospector_agent.control import Control


class ReactiveControl(Control):

    def __init__(self, catch):
        self._behaviour = catch

    def process(self, perception):
        response = self._behaviour.activate(perception)
        return response.action
