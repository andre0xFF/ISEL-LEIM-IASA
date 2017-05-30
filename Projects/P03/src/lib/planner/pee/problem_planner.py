from pee.modprob.problema_heur import ProblemaHeur


class ProblemPlanner(ProblemaHeur):

    def __init__(self, initial_state, final_state, operators):
        super(ProblemPlanner, self).__init__(initial_state, operators)
        self._final_state = final_state

    def objective(self, state):
        return self._final_state == state

    def heuristic(self, state):
        return psa.util.dist(state, self._final_state)