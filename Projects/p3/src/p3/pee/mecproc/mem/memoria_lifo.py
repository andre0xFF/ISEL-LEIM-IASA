# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: pee\mecproc\mem\memoria_lifo.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 441 bytes
"""
Memória de procura do tipo LIFO
@author: Luís Morgado
"""
from .memoria_procura import MemoriaProcura

class MemoriaLIFO(MemoriaProcura):

    def inserir_fronteira(self, no):
        """Inserir nó no início da fronteira de exploração
        @param no: Nó a inserir"""
        self._fronteira.insert(0, no)