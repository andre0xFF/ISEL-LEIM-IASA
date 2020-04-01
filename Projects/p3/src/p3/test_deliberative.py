from agent.deliberative_control.deliberative_control import DeliberativeControl
from agent.prospector_agent import ProspectorAgent
from pee.melhorprim.procura_aa import ProcuraAA as AStarSearch
from planner.pee.pee_planner import PEEPlanner
from psa import executar as execute
from psa import iniciar as init


def main():

    init("env/amb1.das")

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
    main()
