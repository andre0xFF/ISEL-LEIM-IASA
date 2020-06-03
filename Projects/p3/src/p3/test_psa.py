import os

from psa import executar as execute
from psa import iniciar as init
from psa.agente import Agente as Agent


class DummyAgent(Agent):
    def executar(self):
        self.execute()
    
    def execute(self):
        pass


def run():
    init(os.environ["AGENT_ENV"])

    execute(
        DummyAgent()
    )


if __name__ == "__main__":
    run()
