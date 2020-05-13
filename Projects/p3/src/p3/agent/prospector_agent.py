from psa.agente import Agente as Agent
from psa.accao import Mover as Move
from .control import Control


class ProspectorAgent(Agent):
    def __init__(self, control: Control):
        Agent.__init__(self)
        self._control: Control = control

    # Overwrite
    def executar(self):
        self.execute()

    def execute(self):
        perception = self._perceive()
        action = self._process(perception)
        self._act(action)

    def _perceive(self):
        # Inherited from Agente
        return self.sensor_multiplo.detectar()

    def _process(self, perception) -> Move:
        return self._control.process(perception)

    def _act(self, action):
        if action is not None:
            # Inherited from Agente
            return self.actuador.actuar(action)
