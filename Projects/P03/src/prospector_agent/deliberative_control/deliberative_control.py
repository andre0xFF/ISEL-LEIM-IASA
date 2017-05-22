from prospector_agent.control import Control
from prospector_agent.deliberative_control.world_model import WorldModel


class DeliberativeControl(Control):

    def __init__(self, planner):
        self._planner = planner
        self._world_model = WorldModel()

    def reconsider(self):
        return self._world_model or self._planner.pending_plan()

    def deliberate(self):
        # means
        self._objectives = self._world_model.obtain_elements('alvo')
        pass

    def plan(self):
        # ends
        pass

    def execute(self):
        pass

    def process(self, perception):
        self.take(perception)

        if self.reconsider():
            self.deliberate()
            self.plan()

        action = self.execute()
        return action

    # Translation: assimilar
    def take(self, perception):
        self._world_model.update(perception)
