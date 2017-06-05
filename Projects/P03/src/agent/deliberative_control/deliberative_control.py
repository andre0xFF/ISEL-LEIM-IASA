from agent.control import Control
from agent.deliberative_control.world_model import WorldModel


class DeliberativeControl(Control):

    def __init__(self, planner):
        self._planner = planner
        self._world_model = WorldModel()

    def _reconsider(self):
        return self._world_model or self._planner.pending_plan()

    def _deliberate(self):
        # ends
        # loop every states from .obtain_elements() looking for targets ('alvo')

        # states = self._world_model.states
        #
        # for state in states:
        #     element = self._world_model.obtain_elements(state)
        #
        #     if element == 'alvo':
        #         self._objectives.append(state)

        self._objectives = [ state for state in self._world_model.states if self._world_model.obtain_elements(state) == 'alvo' ]

    def _plan(self):
        # means
        if self._objectives:
            return self._planner.plan()

    def execute(self):
        return self._planner.obtain_action('')

    def process(self, perception):
        self._take(perception)

        if self._reconsider():
            self._deliberate()
            self._plan()

        action = self.execute()
        return action

    def _take(self, perception):
        # Translation: assimilar
        self._world_model.update(perception)
