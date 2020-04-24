# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\melhorprim\procura_melhor_prim.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 769 bytes
"""
Mecanismo de procura do tipo melhor-primeiro
@author: Lu�s Morgado
"""
from pee.mecproc.mecanismo_procura import MecanismoProcura
from pee.mecproc.mem.memoria_prioridade import MemoriaPrioridade

class ProcuraMelhorPrim(MecanismoProcura):
    """Mecanismo de procura do tipo melhor-primeiro"""
    __module__ = __name__
    __qualname__ = 'ProcuraMelhorPrim'

    def _iniciar_mem_procura(self):
        return MemoriaPrioridade(self)

    def prioridade(self, no):
        """Função de prioridade de um nó
        @param no: Nó a avaliar"""
        return self.f(no)

    def f(self, no):
        """Função de custo de um nó
            @param no: Nó a avaliar"""
        raise NotImplementedError