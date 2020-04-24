# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\mecproc\no.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 1359 bytes
"""
Nó de árvore de procura 
@author: Luís Morgado
"""

class No:
    """Nó da árvore de procura"""
    __module__ = __name__
    __qualname__ = 'No'

    def __init__(self, estado, operador=None, antecessor=None):
        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor
        if antecessor:
            self._profundidade = antecessor.profundidade + 1
            self._custo = antecessor.custo + operador.custo(antecessor.estado, estado)
        else:
            self._profundidade = 0
            self._custo = 0

    @property
    def estado(self):
        return self._estado

    @property
    def operador(self):
        return self._operador

    @property
    def antecessor(self):
        return self._antecessor

    @property
    def profundidade(self):
        return self._profundidade

    @property
    def custo(self):
        return self._custo

    def __lt__(self, no):
        return self.custo < no.custo

    def __repr__(self):
        return str(self._estado)