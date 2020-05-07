class Planner():

    def plan(self, model_planner, initial_state, objectives):
        # generate a plan based on the world model
        raise NotImplementedError("Abstract Method")

    def obtain_action(self, state):
        raise NotImplementedError("Abstract Method")

    def pending_plan(self):
        # check if there's a pending plan
        raise NotImplementedError("Abstract Method")

    def finish_plan(self):
        # cancel any pending plan
        raise NotImplementedError("Abstract Method")
