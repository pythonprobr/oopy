#!/usr/bin/env python3

from collections import namedtuple

Carta = namedtuple('Carta', 'valor naipe')

class Baralho:
    valores = [str(n) for n in range(2, 11)] + list('JQKA')
    naipes = 'paus ouros copas espadas'.split()

    def __init__(self):
        self.cartas = [Carta(v, n) for n in self.naipes for v in self.valores]

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]




