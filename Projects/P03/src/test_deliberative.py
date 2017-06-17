import sys

sys.path.append('./lib')
sys.path.append('./lib/psa')
sys.path.append('./lib/pee')
sys.path.append('./agent')

import psa
from lib.planner.pee.planner_pee import PlannerPEE
from agent.prospector_agent import ProspectorAgent
from agent.deliberative_control.deliberative_control import DeliberativeControl
from pee.melhorprim.procura_aa import ProcuraAA


def main():
    psa.iniciar('env/amb1.das')

    psa.executar(
        ProspectorAgent(
            DeliberativeControl(
                PlannerPEE(
                    ProcuraAA()
                ))))

if __name__ == '__main__':
    main()
