import os

from psa import executar as execute
from psa import iniciar as init
from agent.controls import DeliberativeControl
from agent import ProspectorAgent
from planner.mdp.mdp_planner import MDPPlanner


def run():
    init(os.environ["AGENT_ENV"])

    execute(
        ProspectorAgent(
            DeliberativeControl(
                MDPPlanner()
            )
        )
    )


if __name__ == "__main__":
    run()
