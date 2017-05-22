from prospector_agent.control import Control


class ReactiveControl(Control):

    def __init__(self, behaviour):
        self.behaviour = behaviour

    def process(self, perception):
        response = self.behaviour.activate(perception)
        return response.action
