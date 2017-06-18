from lib.pdm.model_pdm import ModelPDM


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

            for state in S():
                U[state] = max(self.utility_action(state, action, U_previous, model) for action in A(state))
                delta = max(delta, abs(U[state] - U_previous[state]))

            if delta < self._delta_max:
                break

        return U

    def utility_action(self, state, action, U, model):
        R = model.R
        T = model.T

        total = 0
        for (p, sn) in T(state, action):
            total += p * R(state, action, sn) + self._gamma * U[sn]

        return total

        # return sum(p * (R(state, action, sn) + self._gamma * U[sn]) for p, sn in T(state, action))

    def policy(self, U, model):
        S = model.S
        A = model.A
        policy = {s: 0 for s in S()}

        for state in S():
            policy[state] = max(A(state), key=lambda action: self.utility_action(state, action, U, model))

        return policy

    def solve(self, model):
        U = self.utility(model)
        policy = self.policy(U, model)

        return U, policy
