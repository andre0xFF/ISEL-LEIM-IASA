import sys

sys.path.append("./lib")
sys.path.append("./lib/psa")

import psa
from lib.planner.pee.pee_planner import PEEPlanner
from agent.prospector_agent import ProspectorAgent
from agent.deliberative_control.deliberative_control import DeliberativeControl
from pee.melhorprim.procura_aa import ProcuraAA


def main():
    psa.iniciar("env/amb1.das")

    psa.executar(
        ProspectorAgent(
            DeliberativeControl(
                PEEPlanner(
                    ProcuraAA()
                ))))


if __name__ == "__main__":
    main()
