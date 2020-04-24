from mdp import MDPModel


class MDP(MDPModel):

    def __init__(self, gamma, delta_max):
        # Utility discount factor from Bellman equation
        self._gamma = gamma

        # Iteration stop criteria
        self._delta_max = delta_max

    def utility(self, model):
        # math functions as one upper case letter
        S = model.S
        A = model.A
        U = {}

        for s in S():
            U[s] = 0

        while True:
            previous_U = U.copy()
            delta = 0

            # Loop every state and calculate the utility of each action
            for state in S():
                utilities = []

                for action in A(state):
                    utilities.append(self.utility_action(state, action, previous_U, model))

                # Get the maximum utility
                U[state] = max(utilities)
                delta = max(delta, abs(U[state] - previous_U[state]))

            if delta < self._delta_max:
                break

        return U

    def utility_action(self, state, action, U, model):
        R = model.R
        T = model.T

        total = 0

        # When in state (s) and applying action (a) there might be multiple transaction states,
        # each with its probability
        for (p, sn) in T(state, action):
            total += p * (R(state, action, sn) + self._gamma * U[sn])

        return total

        # return sum(p * (R(state, action, sn) + self._gamma * U[sn]) for p, sn in T(state, action))

    def policy(self, U, model):
        S = model.S
        A = model.A
        policy = {}

        # for state in S():
        #     policy[state] = max(A(state), key=lambda action: self.utility_action(state, action, U, model))

        for state in S():
            utility = 0
            utility_idx = 0
            actions = A(state)

            for i in range(len(actions)):
                current_utility = self.utility_action(state, actions[i], U, model)

                if current_utility > utility:
                    utility = current_utility
                    utility_idx = i

            policy[state] = actions[utility_idx]

        return policy

    def solve(self, model):
        U = self.utility(model)
        policy = self.policy(U, model)

        return U, policy
