import psa
from agent.control import Control
from agent.deliberative_control.world_model import WorldModel


class DeliberativeControl(Control):

    def __init__(self, planner):
        self._planner = planner
        self._world_model = WorldModel()
        self._objectives = []

    def _reconsider(self):
        return self._world_model or self._planner.pending_plan()

    # ends
    def _deliberate(self):
        # loop every states from .obtain_elements() looking for targets ("alvo")
        objectives = []

        for state in self._world_model.states:
            if self._world_model.obtain_elements(state) == "alvo":
                objectives.append(state)

        self._objectives = objectives

    # means
    def _plan(self):
        if self._objectives:
            self._planner.plan(self._world_model, self._world_model.state, self._objectives)
        else:
            self._planner.finish_plan()

    def execute(self):
        action = self._planner.obtain_action(self._world_model.state)

        if action is not None:
            return action.action

        return None

    def process(self, perception):
        self._take(perception)

        if self._reconsider():
            self._deliberate()
            self._plan()

        action = self.execute()
        self.show()

        return action

    def _take(self, perception):
        # Translation: assimilar
        self._world_model.update(perception)

    def show(self):
        vismod = psa.vis(1)
        vismod.limpar()
        self._planner.show(vismod, self._world_model.state)
        self._world_model.show(vismod)
