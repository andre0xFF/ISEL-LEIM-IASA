# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\mecproc\mem\memoria_fifo.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 434 bytes
"""
Memória de procura do tipo FIFO
@author: Luís Morgado
"""
from .memoria_procura import MemoriaProcura

class MemoriaFIFO(MemoriaProcura):

    def inserir_fronteira(self, no):
        """Inserir nó no fim da fronteira de exploração
        @param no: Nó a inserir"""
        self._fronteira.append(no)