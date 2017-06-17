from planner.planner import Planner


class PlannerPDM(Planner):

    def __init__(self):
        # TODO
        pass

    def plan(self, model_planner, state, objectives):
        # generate a plan based on the world model
        # iniciar ModeloPDMPlan
        # utilidade, politica = plan.resolver(ModeloPDMPlan)
        # politica e' o plano
        # pi: S -> A
        # pi(s) = a
        pass

    def obtain_action(self, s):
        pass

    def pending_plan(self):
        # check if there's a pending policy
        pass

    def finish_plan(self):
        # cancel any pending plan
        pass
