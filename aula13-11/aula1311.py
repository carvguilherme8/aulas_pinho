'''
class Aventureiro:
    def __init__(self, nome):
        self._nome = nome

class GrupoAventureiros:
    def __init__(self, nome):
        self._nome = nome
        self._aventureiro = []

guerreiro = Aventureiro("Átila, o Huno")
print(guerreiro)

feiticeiro = Aventureiro("Gandalf, o Branco")
print(feiticeiro)

grupo_de_aventureiros = GrupoAventureiros("Grupo dos Sonhos")
grupo_de_aventureiros._aventureiro.append(guerreiro) 
grupo_de_aventureiros._aventureiro.append(feiticeiro) 
print(grupo_de_aventureiros)
'''

'''
#Has a
class Guerreiro:
    def __init__(self, nome):
        self._nome = nome
        self._arma = None

    def atacar(self):
        if self._arma is not None:
            print(print(f"{self._nome} ataca com {self._arma._nome} e causa {self._arma._dano} ponto de dano"))
        else:
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano")


class Arma1M:
    def __init__(self, nome, dano):
        self._nome = nome
        self._dano = dano

    def __str__(self):
        return f"A arma \"{self._nome}\" causa ({self._dano}) pontos de dano"
    

guerreiro_1 = Guerreiro("Vercingetorix")
guerreiro_1.atacar()
guerreiro_2 = Guerreiro("Boudicca")
guerreiro_2.atacar()

adaga = Arma1M("Adaga", 7)
print(adaga)
espada_curta = Arma1M("Espada Curta", 13)
print(espada_curta)

guerreiro_1._arma = adaga
guerreiro_2._arma = espada_curta
guerreiro_1.atacar()
guerreiro_2.atacar()

del guerreiro_1
del guerreiro_2
'''

class Guerreiro:
    def __init__(self, nome):
        self._nome = nome
        self._arma = None

    def atacar(self):
        if self._arma is not None:
            print(print(f"{self._nome} ataca com {self._arma._nome} e causa {self._arma._dano} ponto de dano"))
        else:
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano")

    def equipar_arma(self, nome, dano):
        self._arma = Arma1M(nome, dano)

    def __del__(self):
        print(f"Removendo {self._nome}")


class Arma1M:
    def __init__(self, nome, dano):
        self._nome = nome
        self._dano = dano

    def __str__(self):
        return f"A arma \"{self._nome}\" causa ({self._dano}) pontos de dano"
    
    def __del__(self):
        print(f"Removendo {self._nome}")
    
guerreiro = Guerreiro("Miyamoto Musashi")
guerreiro.atacar()
guerreiro.equipar_arma("Wokizashi", 15)
guerreiro.atacar()

guerreiro.equipar_arma("Katana", 25)
guerreiro.atacar