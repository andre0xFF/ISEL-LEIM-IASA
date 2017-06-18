import sys

sys.path.append('./lib')
sys.path.append('./lib/psa')
sys.path.append('./lib/pee')
sys.path.append('./agent')

import psa
from prospector_agent import ProspectorAgent
from reinforcement_learning_control.reinforcement_learning_control import ReinforcementLearningControl


def main():
    psa.iniciar('env/amb3.das')

    psa.executar(
        ProspectorAgent(
                ReinforcementLearningControl()
        ))

if __name__ == '__main__':
    main()
