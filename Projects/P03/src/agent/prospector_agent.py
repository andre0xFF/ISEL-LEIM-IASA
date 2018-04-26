import agente


class ProspectorAgent(agente.Agente):

    def __init__(self, control):
        self._control = control

    def executar(self):
        perception = self._perceive()
        action = self._process(perception)
        self._act(action)

    def _perceive(self):
        return self.sensor_multiplo.detectar()

    def _process(self, perception):
        return self._control.process(perception)

    def _act(self, action):
        if action is not None:
            # inherited from Agente
            return self.actuador.actuar(action)
