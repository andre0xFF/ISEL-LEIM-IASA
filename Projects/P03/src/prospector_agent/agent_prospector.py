import sys
# sys.path.append('../lib/psa')
from psa.agente import Agente


class ProspectorAgent(Agente):

    def __init__(self, control):
        self._control = control

    def execute(self):
        perception = self._percept()
        action = self.process()
        self._act(action)

    def _percept(self):
        return self.multiple_sensor.detect()

    def _process(self, percept):
        return self._control.process(percept)

    def _act(self, action):
        if action is not None:
            # inherited from Agente
            self.actuador(action)
