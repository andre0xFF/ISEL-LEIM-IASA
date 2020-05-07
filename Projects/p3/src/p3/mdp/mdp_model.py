class MDPModel():

    def S(self):
        # set of states
        raise NotImplementedError("Abstract Method")

    def A(self, state):
        # valid set of actions (operators) in a state
        raise NotImplementedError("Abstract Method")

    def T(self, state, operator):
        # [(state, probability)...]
        # possible transitions from state of action
        raise NotImplementedError("Abstract Method")

    def R(self, state, operator, next_state):
        # reward of doing the action (operator) in the state
        # if sn belongs to the objectives: Rmax - operator.cost
        # else: -1 * Operator cost
        raise NotImplementedError("Abstract Method")
