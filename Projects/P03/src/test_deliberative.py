# psa.vis(1)
# limpar()
# elementos(dicionario_elementos)
# plano(posicicao_inicial, plano)

import psa
from lib.planner.pee.planner_pee import PlannerPEE
from agent.prospector_agent import ProspectorAgent
from agent.deliberative_control.deliberative_control import DeliberativeControl
from pee.melhorprim.procura_aa import ProcuraAA


def main():
    psa.iniciar('env/amb1.das')

    psa.executar(
        ProspectorAgent(
            DeliberativeControl(
                PlannerPEE(
                    ProcuraAA()
                ))))

if __name__ == '__main__':
    main()
