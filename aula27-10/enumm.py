from enum import Enum

class Escolas(Enum):
    EMAp = 1
    EBAPE = 2
    DIREITO_RIO = 3

class Meses(Enum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3

print(Escolas.EMAp)
print(Escolas.EMAp.name)
print(Escolas.EMAp.value)

print("#"*80)

print(type(Escolas.EMAp))
print(type(Escolas.EMAp.name))
print(type(Escolas.EMAp.value))

print("#"*80)

print(Escolas.EMAp == Escolas.EBAPE)
print(Meses.FEVEREIRO.value > Meses.JANEIRO.value)

