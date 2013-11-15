
class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
       return 'Carta(valor=%r, naipe=%r)' % (self.valor, self.naipe)
