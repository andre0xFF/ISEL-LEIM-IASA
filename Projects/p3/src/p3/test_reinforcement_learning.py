from agent import ProspectorAgent
from agent import ReinforcementLearningControl
from psa import executar as execute
from psa import iniciar as init


def main():
    init("env/amb3.das")

    execute(
        ProspectorAgent(
                ReinforcementLearningControl()
        )
    )


if __name__ == "__main__":
    main()
