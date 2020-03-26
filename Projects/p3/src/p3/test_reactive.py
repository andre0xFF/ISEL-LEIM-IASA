import sys

sys.path.append("./lib")
sys.path.append("./lib/psa")

import psa
from agent.prospector_agent import ProspectorAgent
from agent.reactive_control.reactions.catch import Catch
from agent.reactive_control.reactive_control import ReactiveControl


def main():
    psa.iniciar("./env/amb1.das")
    psa.executar(ProspectorAgent(ReactiveControl(Catch())))


if __name__ == "__main__":
    main()
