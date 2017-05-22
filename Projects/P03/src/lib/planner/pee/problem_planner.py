class ProblemPlanner():

    def __init__(self, initial_state, final_state, operators):
        self._initial_state = initial_state
        self._final_state = final_state
        self.operators = operators

    def objective(self, state):
        pass

    def heuristic(self, state):
        pass