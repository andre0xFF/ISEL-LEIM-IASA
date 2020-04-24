# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\mecproc\procura.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 445 bytes
"""
Interface Procura
@author: Luís Morgado
"""

class Procura:
    """Interface Procura"""
    __module__ = __name__
    __qualname__ = 'Procura'

    def resolver(self, problema, prof_max):
        """Resolver problema
        @param problema: Problema de procura
        @param prof_max: Profundidade máxima da procura
        @return: Solução"""
        raise NotImplementedError