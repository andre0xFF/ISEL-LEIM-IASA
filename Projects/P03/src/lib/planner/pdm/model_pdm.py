class ModelPDM():

    def S(self):
        abstract

    def A(self, state):
        abstract

    def T(self, state, operator):
        abstract

    def R(self, state, operator, previous_state):
        abstract
        # check previous_state
