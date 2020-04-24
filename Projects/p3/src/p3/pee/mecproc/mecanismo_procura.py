# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\mecproc\mecanismo_procura.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 2622 bytes
"""
Mecanismo geral de procura
@author: Luís Morgado
"""
from .no import No
from .solucao import Solucao

class MecanismoProcura(object):
    """Mecanismo geral de procura em espaços de estados"""
    __module__ = __name__
    __qualname__ = 'MecanismoProcura'

    def __init__(self):
        self.memoria_procura = self._iniciar_mem_procura()
        self.problema = None

    def _iniciar_mem_procura(self):
        """Iniciar memória de procura"""
        raise NotImplementedError

    def resolver(self, problema, prof_max=float('inf'), parcial=False):
        """Resolver problema
        @param problema: Problema de procura
        @param prof_max: Profundidade máxima da procura
        @param parcial: Solução parcial com profundidade máxima (sim/não)
        @return: Solução"""
        self.problema = problema
        self.memoria_procura.limpar()
        no_inicial = No(problema.estado_inicial)
        self.memoria_procura.inserir(no_inicial)
        while not self.memoria_procura.fronteira_vazia():
            no = self.memoria_procura.remover()
            if problema.objectivo(no.estado):
                return self._gerar_solucao(no)
                if no.profundidade < prof_max:
                    self._expandir(no)
            elif parcial:
                return self._gerar_solucao(no)

    def _expandir(self, no):
        """Expandir nó por aplicação dos operadores definidos no problema
            @param no: Nó a expandir"""
        estado = no.estado
        for operador in self.problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                no_suc = No(estado_suc, operador, no)
                self.memoria_procura.inserir(no_suc)

    def _gerar_solucao(self, no_final):
        """Gerar solução do nó inicial até ao nó final
        @param no_final: Nó final
        @return: Solução"""
        solucao = Solucao()
        no = no_final
        while no is not None:
            solucao.juntar_inicio(no)
            no = no.antecessor

        return solucao

    def obter_explorados(self):
        """Obter informação de estados explorados @return: [(estado, avaliação de custo), ...]"""
        mem_exp = self.memoria_procura.explorados
        if hasattr(self, 'f'):
            explorados = {s:-self.f(no) for s, no in mem_exp.items()}
        else:
            explorados = {s:-no.custo for s, no in mem_exp.items()}
        return explorados