# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\modprob\problema.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 1083 bytes
"""
Definição de problema de procura
@author: Luís Morgado
"""

class Problema(object):
    """Definição geral de um problema de procura"""
    __module__ = __name__
    __qualname__ = 'Problema'

    def __init__(self, estado_inicial, operadores):
        """Iniciar problema
        @param estado_inicial: Estado inicial do problema
        @param operadores: Operadores definidos para o problema"""
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    @property
    def estado_inicial(self):
        """Obter estado inicial do problema"""
        return self._estado_inicial

    @property
    def operadores(self):
        """Obter operadores definidos para o problema"""
        return self._operadores

    def objectivo(self, estado):
        """Verificar se um estado satisfaz o objectivo
        @param estado: Estado a verificar
        @return: Indicação se estado satisfaz objectivo (sim/não)"""
        raise NotImplementedError