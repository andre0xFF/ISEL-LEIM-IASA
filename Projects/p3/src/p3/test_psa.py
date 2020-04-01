from agent.prospector_agent import ProspectorAgent
from agent.reactive_control.reactions.catch import Catch
from agent.reactive_control.reactive_control import ReactiveControl
from psa import executar as execute
from psa import iniciar as init


def run():
    init("env/amb1.das")

    execute(
        ProspectorAgent(
            ReactiveControl(
                Catch()
            )
        )
    )


if __name__ == "__main__":
    run()
