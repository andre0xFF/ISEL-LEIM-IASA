# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\mecproc\mem\memoria_prioridade.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 792 bytes
"""
Memória de procura com prioridade
@author: Luís Morgado
"""
from heapq import heappush, heappop
from .memoria_procura import MemoriaProcura

class MemoriaPrioridade(MemoriaProcura):

    def __init__(self, avaliador):
        self._avaliador = avaliador

    def inserir_fronteira(self, no):
        """Inserir nó no fim da fronteira de exploração"""
        prioridade = self._avaliador.prioridade(no)
        heappush(self._fronteira, (prioridade, no))

    def remover_fronteira(self):
        """Remover nó da _fronteira de exploração
            @return: Nó removido"""
        _, no = heappop(self._fronteira)
        return no