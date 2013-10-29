Uma instância de `Cao` tem uma representação de depuração (`repr`) que
permite construir uma instância igual::

    >>> from cao import Cao
    >>> rex = Cao('Rex')
    >>> rex
    Cao('Rex')

A representação amigável é simplesmente o nome do cão::

    >>> print(rex)
    Rex

Alguns atributos, como `qt_patas` são definidos na classe `Cao` e herdados
pelas instâncias::

    >>> rex.qt_patas
    4

O método latir aceita um número de latidas opcional, e se o cão estiver
nervoso, ele sempre late duas vezes mais::

    >>> rex.latir()
    Rex: Au!
    >>> rex.latir(2)
    Rex: Au! Au!
    >>> rex.nervoso = True
    >>> rex.latir(3)
    Rex: Au! Au! Au! Au! Au! Au!
