"""

    >>> class FrozenDate(date):
    ...     @staticmethod
    ...     def today():
    ...         return date.fromtimestamp(10**9) # 2001-09-08
    ...
    >>> juca = Aluno('João Carlos', date(1997, 10, 30))
    >>> juca.nome
    'João Carlos'
    >>> juca.idade(FrozenDate)
    3


"""

from datetime import date

class Aluno:

    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc

    def idade(self, classe_date_congelada=date):
        hoje = classe_date_congelada.today()
        try:
            niver = date(hoje.year, self.data_nasc.month, self.data_nasc.day)
        except ValueError:
             # acontece quando nascimento é 29/fev e ano atual não é bissexto
            niver = date(hoje.year, 3, 1)
        anos = hoje.year - self.data_nasc.year
        return anos if niver <= hoje else anos - 1
