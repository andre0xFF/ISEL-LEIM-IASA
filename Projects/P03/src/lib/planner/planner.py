class Planner():

    def __init__(self):
        abstract

    def plan(self, plan_model, initial_state, objectives):
        # generate a plan based on the world model
        abstract

    def obtain_action(self, state):
        abstract

    def pending_plan(self):
        abstract

    def finish_plan(self):
        # cancel any pending plan
        abstract
