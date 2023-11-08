class SerieTV:
    def __init__(self, num_temporadas, num_episodios):
        self.num_temporadas = num_temporadas
        self.num_episodios = num_episodios

    #paia (repr tem prioridade)
    def __str__(self):
        return f"{self.num_temporadas} temporadas de {self.num_episodios} episódios"
    
    #esse é bao
    def __repr__(self):
        class_ = self.__class__.__name__
        
        return f"{class_}(num_temporadas={self.num_temporadas!r}, num_episódios={self.num_episodios!r})"

serie_1 = SerieTV(7, 13)
serie_2 = SerieTV(42, 666)

print(serie_1)
print(f"{serie_1!s}") #str

print(serie_2)
print(f"{serie_2!r}") #repr
print(repr(serie_2))
