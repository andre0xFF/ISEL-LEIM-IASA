from planner.pdm.model_pdm import ModelPDM


class PDM(ModelPDM):

    def __init__(self, gamma, delta_max):
        self._gamma = gamma
        self._delta_max = delta_max

    def utility(self, model):
        # math functions as one upper case letter
        S = model.S
        A = model.A
        U = {s: 0 for s in S()}

        while True:
            U_previous = U.copy()
            delta = 0

            for s in S():
                U[s] = max(self.utility_action(s, a, U_previous, model) for a in A(s))
                delta = max(delta, abs(U[s] - U_previous[s]))

            if delta < self._delta_max:
                break

        return U

    def utility_action(self, state, operator, U, model):
        R = model.R
        T = model.T
        pass
        # return sum(p * R(state, operator, sn) + self._gamma * U[sn]) for (p, sn) in T(s, a))

    def policy(self, U, model):
        S = model.S
        A = model.A
        policy = []

        for state in S():
            policy[state] = max(A(state), key=lambda action: self.utility_action(state, action, U, model))

        return policy

    def solve(self, model):
        U = self.utility(model)
        policy = self.policy(U, model)

        return U, policy
