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
        next_state = perception.posicao

        if self._state is not None:
            action = perception.orientacao
            reward = self._generate_reward(perception)
            self._learning_mechanism.learn(self._state, action, reward, next_state)

        angle = self._learning_mechanism.select_action(next_state)
        self._state = next_state

        if angle is not None:
            return Mover(angle, ang_abs=True)

    def _generate_reward(self, perception):
        reward = -1 * perception.custo_mov

        if perception.carga:
            reward += self._rmax
        elif perception.colisao:
            reward += -1 * self._rmax

        return reward
