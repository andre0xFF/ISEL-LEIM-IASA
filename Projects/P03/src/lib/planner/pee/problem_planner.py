from pee.modprob.problema_heur import ProblemaHeur
from psa5 import dist


class ProblemPlanner(ProblemaHeur):

    def __init__(self, initial_state, final_state, operators):
        # super(ProblemPlanner, self).__init__(initial_state, operators)
        ProblemaHeur.__init__(self, initial_state, operators)
        self._final_state = final_state

    def objectivo(self, state):
        return self._final_state == state

    def heuristica(self, state):
        return dist(state, self._final_state)