class Aluno:
    def __init__(self, qi, nr_artigos_publicados):
        self.qi = qi
        self.nr_artigos_publicados = nr_artigos_publicados

    def __str__(self):
        return f"QI: {self.qi}, Publicações: {self.nr_artigos_publicados}"
    
    def __add__(self, other):
        qi_total = self.qi + other.qi
        publicacoes_acumuladas = self.nr_artigos_publicados + other.nr_artigos_publicados

        return Aluno(qi_total, publicacoes_acumuladas)
    
    def __gt__(self, other):
        if self.qi > other.qi:
            return True
        elif self.qi == other.qi:
            return  self.nr_artigos_publicados > other.nr_artigos_publicados
        else: 
            return False


aluno_1 = Aluno(100, 0)
aluno_2 = Aluno(130, 2)
super_aluno = aluno_1 + aluno_2

print(aluno_1)
print(aluno_2)
print(super_aluno)


if aluno_1 > aluno_2:
    print("O aluno 1 é melhor que o aluno 2")
else:
    print("O aluno 2 é melhor que o aluno 1")
