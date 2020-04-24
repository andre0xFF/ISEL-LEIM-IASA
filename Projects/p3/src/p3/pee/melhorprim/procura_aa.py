# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\melhorprim\procura_aa.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 448 bytes
"""
Mecanismo de procura A*
@author: Luís Morgado
"""
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraAA(ProcuraMelhorPrim):
    """Mecanismo de procura A*, critério de ordem: f = g + h,
    com heurística admissível"""
    __module__ = __name__
    __qualname__ = 'ProcuraAA'

    def f(self, no):
        return no.custo + self.problema.heuristica(no.estado)