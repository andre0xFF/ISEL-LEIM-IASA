import os

from agent import ProspectorAgent
from agent import ReinforcementLearningControl
from psa import executar as execute
from psa import iniciar as init


def main():
    init(os.environ["AGENT_ENV"])

    execute(
        ProspectorAgent(
                ReinforcementLearningControl()
        )
    )


if __name__ == "__main__":
    main()
