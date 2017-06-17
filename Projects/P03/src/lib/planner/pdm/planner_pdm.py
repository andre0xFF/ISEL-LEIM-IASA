from pdm.pdm import PDM
from planner.pdm.model_pdm_plan import ModelPDMPlan
from planner.planner import Planner


class PlannerPDM(Planner):

    def __init__(self):
        self._gamma = 0.9
        self._delta_max = 1
        self.utility = {}
        self.policy = {}
        self._pdm = PDM(self._gamma, self._delta_max)

    def plan(self, model_planner, state, objectives):
        if objectives:
            model_pdm_planner = ModelPDMPlan(model_planner, objectives)
            self._utility, self._policy = self._pdm.solve(model_pdm_planner)
        else:
            self.finish_plan()

    def obtain_action(self, state):
        if self._policy:
            return self._policy.get(state)

    def pending_plan(self):
        return self._policy

    def finish_plan(self):
        self._utility = {}
        self._policy = {}

    def show(self, vismod, state):
        if self._policy:
            vismod.limpar()
            # vismod.campo(self._utility)
            # vismod.politica(self._policy)
