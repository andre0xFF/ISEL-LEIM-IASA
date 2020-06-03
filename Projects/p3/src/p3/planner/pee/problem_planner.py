from pee.modprob.problema_heur import ProblemaHeur as HeuristicProblem
from psa.util import dist


class ProblemPlanner(HeuristicProblem):

    def __init__(self, initial_state, final_state, operators):
        # super(ProblemPlanner, self).__init__(initial_state, operators)
        HeuristicProblem.__init__(self, initial_state, operators)
        # super().__init__(initial_state, operators)
        self._final_state = final_state

    def objectivo(self, state):
        return self.objective(state)
    
    def objective(self, state):
        return self._final_state == state

    def heuristica(self, state):
        return self.heuristic(state)
    
    def heuristic(self, state):
        return dist(state, self._final_state)
