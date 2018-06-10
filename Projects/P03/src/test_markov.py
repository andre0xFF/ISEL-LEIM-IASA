import sys

sys.path.append("./lib")
sys.path.append("./lib/psa")

import psa
from planner.mdp.mdp_planner import MDPPlanner
from agent.prospector_agent import ProspectorAgent
from agent.deliberative_control.deliberative_control import DeliberativeControl


def main():
    psa.iniciar("env/amb1.das")

    psa.executar(
        ProspectorAgent(
            DeliberativeControl(
                MDPPlanner()
            )))


if __name__ == "__main__":
    main()
