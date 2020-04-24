# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\modprob\problema_heur.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 511 bytes
"""
Definição de problema com heurística
@author: Luís Morgado
"""
from .problema import Problema

class ProblemaHeur(Problema):
    """Definição geral de um problema com heurística"""
    __module__ = __name__
    __qualname__ = 'ProblemaHeur'

    def heuristica(self, estado):
        """Obter heurística de um estado
        @param estado: Estado a avaliar
        @return: Heurística do estado"""
        raise NotImplementedError