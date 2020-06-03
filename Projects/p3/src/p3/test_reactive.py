import os

from psa import executar as execute
from psa import iniciar as init
from agent import ProspectorAgent
from agent.controls.reactive.reactions import Catch
from agent.controls import ReactiveControl


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
