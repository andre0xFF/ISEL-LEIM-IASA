from lib.planner.pee.problem_planner import ProblemPlanner
from lib.planner.planner import Planner


class PlannerPEE(Planner):

    def __init__(self, search_mechanism):
        self._search_mechanism = search_mechanism
        self._plan = None

    def plan(self, plan_model, initial_state, objectives):
        problem = ProblemPlanner(initial_state, objectives[0], plan_model.objectives())
        solution = self._search_mechanism.solve(problem)

        if solution:
            # root node has node operator so [1:]
            # for node in solution[1:]:
            #     self._plan.append(node.operator)
            self._plan = [node.operator for node in solution[1:]]

    def obtain_action(self, state):
        # state is not used here
        if self._plan is not None:
            return self._plan.pop(0)

    def pending_plan(self):
        return self._plan and self._plan.__len__() > 0

    def finish_plan(self):
        self._plan = None
