# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\melhorprim\procura_sofrega.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 416 bytes
"""
Mecanismo de procura sôfrega
@author: Luís Morgado
"""
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraSofrega(ProcuraMelhorPrim):
    """Mecanismo de procura sôfrega, critério de ordem: f = h"""
    __module__ = __name__
    __qualname__ = 'ProcuraSofrega'

    def f(self, no):
        return self.problema.heuristica(no.estado)