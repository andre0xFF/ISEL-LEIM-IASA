# import sys
# sys.path.append('../lib')
# sys.path.append('../agent_prospector')
import accao
import agente
import psa
from lib.ecr.behaviour import Behaviour
from prospector_agent.agent_prospector import ProspectorAgent
from prospector_agent.reactive_control.reactive_control import ReactiveControl


class TestAgent(agente.Agente):

    def executar(self):
        super.actuador.actuar(accao.Avancar())

def main():
    psa.iniciar('env/amb1.das')
    psa.executar(TestAgent())


if __name__ == '__main__':
    main()

