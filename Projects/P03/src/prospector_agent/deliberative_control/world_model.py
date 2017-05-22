import util
from prospector_agent.deliberative_control.model_planner import ModelPlanner
from prospector_agent.deliberative_control.move_operator import MoveOperator
# from psa.util import dirmov


class WorldModel(ModelPlanner):

    def WorldModel(self):
        self._changed = False
        self._elements = {}
        self._state = ()
        self._states = ()
        self._operators = []

        for angle in util.dirmov():
            self._operators.append([MoveOperator(self, angle)])

    @property
    def changed(self):
        return self._changed

    @property
    def state(self):
        return self._state

    @property
    def operators(self):
        return self._operators

    @property
    def states(self):
        return self._states

    def obtain_elements(self, state):
        return self._elements[state]

    def update(self, perception):
        self._state = perception.position

        if self._elements != perception.elements:
            self._states = perception.states
            self._elements = perception.elements
            self._changed = True
        else:
            self._changed = False
        pass

