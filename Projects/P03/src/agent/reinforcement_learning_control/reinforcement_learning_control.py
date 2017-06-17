from psa5.util import dirmov
from agent.control import Control
from psa5.actuador import Mover
from agent.reinforcement_learning_control.learning_mechanism import LearningMechanism


class ReinforcementLearningControl(Control):

    def __init__(self):
        self._rmax = 100
        actions = dirmov()
        self._learning_mechanism = LearningMechanism(actions)
        self._state = None

    def process(self, perception):
        sn = perception.posicao

        if self._state is not None:
            action = perception.orientacao
            reward = self._generate_reward(perception)
            self._learning_mechanism.learn(self._state, action, reward, sn)

        an = self._learning_mechanism.select_action(sn)
        self._state = sn

        if an is not None:
            return Mover(an, ang_abs=True)

    def _generate_reward(self, perception):
        r = -1 * perception.custo_mov

        if perception.carga:
            r += self._rmax
        elif perception.colisao:
            r += -1 * self._rmax

        return r
