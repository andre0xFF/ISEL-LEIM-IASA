# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\mecproc\solucao.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 1274 bytes
"""
Solução de uma procura
@author: Luís Morgado
"""

class Solucao:
    """Solução de uma procura"""
    __module__ = __name__
    __qualname__ = 'Solucao'

    def __init__(self):
        self._percurso = []

    @property
    def percurso(self):
        return self._percurso

    def juntar_percurso(self, percurso):
        """Juntar percurso no final da solução
        @param percurso: Percurso a inserir"""
        self._percurso += percurso

    def juntar_inicio(self, no):
        """Juntar nó no início da solução
        @param no: Nó a inserir"""
        self._percurso.insert(0, no)

    def dimensao(self):
        """Obter dimensão da solução
        @return: Dimensão da solução"""
        return len(self._percurso)

    def custo(self):
        """Obter custo da solução
        @return: Custo da solução"""
        if not self._percurso:
            return 0
        return self._percurso[(-1)].get_custo()

    def __iter__(self):
        """Obter iterador"""
        return iter(self._percurso)

    def __getitem__(self, key):
        """Obter nó da solução"""
        return self._percurso[key]