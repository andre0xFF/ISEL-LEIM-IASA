# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\prof\procura_prof_iter.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 744 bytes
"""
Procura em profundidade iterativa
@author: Luís Morgado
"""
from .procura_prof import ProcuraProf

class ProcuraProfIter(ProcuraProf):
    """Procura em profundidade iterativa"""
    __module__ = __name__
    __qualname__ = 'ProcuraProfIter'

    def resolver(self, problema, prof_max=1000, inc_prof=1):
        """Procurar solução com incremento de profundidade indicado
        @param problema: Problema associado
        @param prof_max: Profundidade máxima da procura
        @param inc_prof: Incremento de profundidade por cada iteração
        @return: Solução"""
        for prof in range(inc_prof, prof_max + 1, inc_prof):
            solucao = ProcuraProf.resolver(self, problema, prof)
            if solucao:
                return solucao