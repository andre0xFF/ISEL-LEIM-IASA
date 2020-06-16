from mdp.mdp import MDP

from .. import Planner
from .mdp_model_plan import MDPModelPlan


class MDPPlanner(Planner):

    def __init__(self):
        gamma = 0.9
        delta_max = 12
        self.utility = {}
        self.policy = {}
        self._mdp = MDP(gamma, delta_max)

    def plan(self, model_planner, state, objectives):
        if objectives:
            mdp_model_planner = MDPModelPlan(model_planner, objectives)
            self._utility, self._policy = self._mdp.solve(mdp_model_planner)
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
