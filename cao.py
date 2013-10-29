class Mamifero(object):
    """vertebrados dotados de glândulas mamárias"""


class Cao(Mamifero):
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def latir(self, vezes=1):
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print(self.nome + ':' + ' Au!' * vezes)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao(%r)' % self.nome
