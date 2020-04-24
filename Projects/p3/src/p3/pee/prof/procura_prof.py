# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\prof\procura_prof.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 371 bytes
"""
Mecanismo de procura em profundidade
@author: Luís Morgado
"""
from pee.mecproc.mecanismo_procura import MecanismoProcura
from pee.mecproc.mem.memoria_lifo import MemoriaLIFO

class ProcuraProf(MecanismoProcura):
    """Mecanismo de procura em profundidade"""
    __module__ = __name__
    __qualname__ = 'ProcuraProf'

    def _iniciar_mem_procura(self):
        return MemoriaLIFO()