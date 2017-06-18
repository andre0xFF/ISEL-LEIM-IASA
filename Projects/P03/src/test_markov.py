import sys

sys.path.append('./lib')
sys.path.append('./lib/psa')
sys.path.append('./lib/pee')
sys.path.append('./agent')

import psa
from planner.pdm.planner_pdm import PlannerPDM
from agent.prospector_agent import ProspectorAgent
from agent.deliberative_control.deliberative_control import DeliberativeControl


def main():
    psa.iniciar('env/amb1.das')

    psa.executar(
        ProspectorAgent(
            DeliberativeControl(
                PlannerPDM()
            )))

if __name__ == '__main__':
    main()
