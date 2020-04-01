from planner.pee.problem_planner import ProblemPlanner
from planner.planner import Planner


class PEEPlanner(Planner):

    def __init__(self, search_mechanism):
        self._search_mechanism = search_mechanism
        self._plan = []

    def plan(self, model_planner, initial_state, objectives):
        problem = ProblemPlanner(initial_state, objectives[0], model_planner.operators)
        solution = self._search_mechanism.resolver(problem)

        if solution is not None:
            plan = []

            # root node does not have a node operator [1:]
            for node in solution[1:]:
                plan.append(node.operador)

            self._plan = plan

    def obtain_action(self, state):
        # state is not used here
        if self._plan is not None and self._plan.__len__() > 0:
            return self._plan.pop(0)

    def pending_plan(self):
        return self._plan is not None and self._plan.__len__() > 0

    def finish_plan(self):
        self._plan = []

    def show(self, vismod, state):
        if self._plan:
            vismod.campo(self._search_mechanism.obter_explorados())
            # vismod.plano(state, self._plan)
            # vismod.marcar([state], linha=1)
