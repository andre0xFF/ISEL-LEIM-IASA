class Planner():

    def plan(self, model_planner, initial_state, objectives):
        # generate a plan based on the world model
        abstract

    def obtain_action(self, state):
        abstract

    def pending_plan(self):
        # check if there's a pending plan
        abstract

    def finish_plan(self):
        # cancel any pending plan
        abstract
