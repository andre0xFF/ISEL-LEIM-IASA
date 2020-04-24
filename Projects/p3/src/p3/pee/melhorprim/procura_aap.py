# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\melhorprim\procura_aap.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 554 bytes
"""
Procura A* Ponderada (Weighted A*)
@author: Luís Morgado
"""
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraAAP(ProcuraMelhorPrim):
    """Mecanismo de procura A* ponderada (Weighted A*)"""
    __module__ = __name__
    __qualname__ = 'ProcuraAAP'

    def __init__(self, epsilon=0.5):
        super(ProcuraAAP, self).__init__()
        self.epsilon = epsilon

    def f(self, no):
        return no.custo + (1 + self.epsilon) * self.problema.heuristica(no.estado)