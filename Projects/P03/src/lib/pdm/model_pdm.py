class ModelPDM():

    def S(self):
        # "conjunto de estados"
        # states
        abstract

    def A(self, state):
        # valid actions in a stae
        abstract

    def T(self, state, operator):
        # "transicoes possiveis a partir de s por a"
        # pair of [(state, probability)...]
        # the possible transitions from the state of action
        abstract

    def R(self, state, operator, next_state):
        # "recompensa de em s realizar a transitando por s"
        # reward of doing the action (operator) in the state
        # if sn belongs to the objectives: Rmax - operator.cost
        # else: -1 * Operator cost
        abstract
