from agent.control import Control
from agent.deliberative_control.world_model import WorldModel


class DeliberativeControl(Control):

    def __init__(self, planner):
        self._planner = planner
        self._world_model = WorldModel()

    def reconsider(self):
        return self._world_model or self._planner.pending_plan()

    def deliberate(self):
        # means
        self._objectives = self._world_model.obtain_elements('alvo')

    def plan(self):
        # ends
        if self._objectives:
            return self._planner.plan()

    def execute(self):
        return self._planner.obtain_action()

    def process(self, perception):
        self.take(perception)

        if self.reconsider():
            self.deliberate()
            self.plan()

        action = self.execute()
        return action

    def take(self, perception):
        # Translation: assimilar
        self._world_model.update(perception)
