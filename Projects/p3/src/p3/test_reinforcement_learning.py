import os

from agent import ProspectorAgent
from agent.controls import ReinforcementLearningControl
from psa import executar as execute
from psa import iniciar as init


def run():
    init(os.environ["AGENT_ENV"])

    execute(
        ProspectorAgent(
                ReinforcementLearningControl()
        )
    )


if __name__ == "__main__":
    run()
