from prospector_agent.deliberative_control.planner import Planner


class PEEPlanner(Planner):

    def __init__(self, search_mechanism):
        self._search_mechanism = search_mechanism

    def plan(self, world_model, initial_state, objectives):
        pass

    def pending_plan(self):
        pass

    def finish_plan(self):
        pass