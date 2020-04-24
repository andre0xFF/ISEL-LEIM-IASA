# uncompyle6 version 3.6.6
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
# [GCC 8.4.0]
# Embedded file name: C:\Users\sp1\Documents\dt19\proj\proj19\aulas\iasa19\teste-iasa-cp3-python3.7.2\iasa-cp3\lib\pee\modprob\operador.py
# Compiled at: 2019-01-12 10:23:18
# Size of source mod 2**32: 673 bytes
"""
Interface Operador
@author: Luís Morgado
"""

class Operador:
    """Interface Operador"""
    __module__ = __name__
    __qualname__ = 'Operador'

    def aplicar(self, estado):
        """Aplicar operador a estado gerando um novo estado
        @param estado: Estado a aplicar operador
        @return: Novo estado"""
        raise NotImplementedError

    def custo(self, estado, estado_suc):
        """Custo de aplicação do operador
        @param estado: Estado antecessor
        @param estado_suc: Estado sucessor
        @return: Custo de aplicação do operador"""
        raise NotImplementedError