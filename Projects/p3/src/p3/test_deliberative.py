import os

from psa import executar as execute
from psa import iniciar as init
from pee.larg.procura_larg import ProcuraLarg as BreadthFirstSearch
from pee.melhorprim.procura_aa import ProcuraAA as AStarSearch
from agent import ProspectorAgent
from agent.controls import DeliberativeControl
from planner.pee.pee_planner import PEEPlanner


def run():
    init(os.environ["AGENT_ENV"])

    execute(
        ProspectorAgent(
            DeliberativeControl(
                PEEPlanner(
                    AStarSearch()
                )
            )
        )
    )


if __name__ == "__main__":
    run()
