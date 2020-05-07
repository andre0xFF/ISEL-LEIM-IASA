import os

from agent.prospector_agent import ProspectorAgent
from agent.reactive_control.reactions.catch import Catch
from agent.reactive_control.reactive_control import ReactiveControl
from psa import executar as execute
from psa import iniciar as init
from psa.agente import Agente


def run():
    init(os.environ["AGENT_ENV"])

    execute(
        ProspectorAgent(
            ReactiveControl(
                Catch()
            )
        )
    )


if __name__ == "__main__":
    run()
