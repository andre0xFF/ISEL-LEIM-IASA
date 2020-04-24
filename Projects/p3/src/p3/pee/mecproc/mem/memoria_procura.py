# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\mecproc\mem\memoria_procura.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 1772 bytes
"""
Memória de procura
@author: Luís Morgado
"""

class MemoriaProcura:
    """Memória de procura"""
    __module__ = __name__
    __qualname__ = 'MemoriaProcura'

    def __init__(self):
        self.limpar()

    @property
    def fronteira(self):
        return self._fronteira

    @property
    def explorados(self):
        return self._explorados

    @property
    def fechados(self):
        return self._fechados

    def limpar(self):
        """Limpar memória"""
        self._fronteira = []
        self._explorados = {}
        self._fechados = {}

    def inserir(self, no):
        """Inserir nó na memória de procura
            @param no: Nó a inserir"""
        estado = no.estado
        no_mem = self._explorados.get(estado)
        if no_mem is None or no.custo < no_mem.custo:
            self.inserir_fronteira(no)
            self._explorados[estado] = no

    def remover(self):
        """Remover nó da _fronteira de exploração
        @return: Nó removido"""
        no = self.remover_fronteira()
        self._fechados[no.estado] = no
        return no

    def inserir_fronteira(self, no):
        """Inserir nó na fronteira de exploração
            @param no: Nó a inserir"""
        raise NotImplementedError

    def remover_fronteira(self):
        """Remover nó da _fronteira de exploração
        @return: Nó removido"""
        return self._fronteira.pop(0)

    def fronteira_vazia(self):
        """Indicação de fronteira de exploração vazia
            @return: Fronteira de exploração vazia (sim/não)"""
        return len(self._fronteira) == 0