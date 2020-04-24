# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\melhorprim\procura_custo_unif.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 413 bytes
"""
Mecanismo de procura de custo uniforme
@author: Luís Morgado
"""
from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """Mecanismo de procura de custo uniforme, critério de ordem: f = g"""
    __module__ = __name__
    __qualname__ = 'ProcuraCustoUnif'

    def f(self, no):
        return no.custo