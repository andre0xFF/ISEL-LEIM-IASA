# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\larg\procura_larg.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 359 bytes
"""
Mecanismo de procura em largura
@author: Luís Morgado
"""
from pee.mecproc.mecanismo_procura import MecanismoProcura
from pee.mecproc.mem.memoria_fifo import MemoriaFIFO

class ProcuraLarg(MecanismoProcura):
    """Mecanismo de procura em largura"""
    __module__ = __name__
    __qualname__ = 'ProcuraLarg'

    def _iniciar_mem_procura(self):
        return MemoriaFIFO()