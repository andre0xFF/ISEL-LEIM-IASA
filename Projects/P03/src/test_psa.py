import site
import sys

sys.path.append("./lib")
sys.path.append("./lib/psa")

from agent.prospector_agent import ProspectorAgent
from agent.reactive_control.reactions.catch import Catch
from agent.reactive_control.reactive_control import ReactiveControl

import psa


def main():
    print(sys.executable)
    print(sys.version)
    print(sys.path)
    print(site.getsitepackages())
    psa.iniciar("env/amb1.das")
    psa.executar(ProspectorAgent(ReactiveControl(Catch())))


if __name__ == "__main__":
    main()
