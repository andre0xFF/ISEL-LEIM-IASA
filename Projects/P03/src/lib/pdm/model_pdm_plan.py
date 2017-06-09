from pdm.model_pdm import ModelPDM
from planner.model_planner import ModelPlanner


class ModelPDMPlan(ModelPDM, ModelPlanner):

    def __init__(self):
        pass

    def start_model(self, model_planner):
        self._S = model_planner.states()
        self._A = model_planner.operators()

        for s in self._S:
            for a in self._A:
                self._generate_model(s, a)

    def _generate_model(self, s, a):
        # simulate the transition
        sn = a.aplicar(a)

        if sn is None:
            self._T[(s, a)] = []
        else:
            self._T[(s, a)] = [(1, sn)]
            self._R[(s, a, sn)] = self._generate_reward(s, a, sn)

    def _generate_reward(self, s, a, sn):
        r = -1 * a.custo()

        if sn in self._objectives:
            r += self._rmax

        return r

    def S(self):
        return self._S

    def A(self, state):
        return self._A

    def T(self, state, operator):
        return self._T.get(state, operator)

    def R(self, state, operator, next_state):
        return self._R.get(state, operator, next_state)