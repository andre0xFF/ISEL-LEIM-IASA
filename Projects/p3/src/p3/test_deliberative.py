import os

from psa import executar as execute
from psa import iniciar as init
from pee.larg.procura_larg import ProcuraLarg as BreadthFirstSearch
from pee.melhorprim.procura_aa import ProcuraAA as AStarSearch
from agent import ProspectorAgent
from agent.controls import DeliberativeControl
from planner.search import SearchPlanner


def run():
    init(os.environ["AGENT_ENV"])

    execute(
        ProspectorAgent(
            DeliberativeControl(
                SearchPlanner(
                    AStarSearch()
                )
            )
        )
    )


if __name__ == "__main__":
    run()
