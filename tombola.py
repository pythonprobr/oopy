

"""
    >>> t = Tombola()
    >>> t.carregada()
    False
    >>> bolas = 'ABC'
    >>> t.carregar(bolas)
    >>> t.carregada()
    True
    >>> t.misturar()
    >>> t.sortear() in bolas
    True
    >>> t.sortear() in bolas
    True
    >>> t.sortear() in bolas
    True
    >>> t.carregada()
    False

"""

from random import shuffle

class Tombola:
    """sorteia itens sem repetir"""

    def __init__(self):
        self.itens = []

    def carregada(self):
        return bool(self.itens)

    def carregar(self, itens):
        self.itens = list(itens)

    def misturar(self):
        shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()
