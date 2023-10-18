class Point2D(object):
    """
    Pode fazer docstring na classe

    Atribbutes:
        x (int): aishdasd
        y (int): iajpjasj
    """
    def __init__(self, x, y):
        """
        asdasdasndkjdwad

        Parameters:
            x (int): jdasda
            y (int): ldasda
        """
        self.x = x
        self.y = y

    def set_x(self, valor):
        if valor < 0:
            print("Erro. Valor não foi alterado!")
        else:
            self.x = valor

    def set_y(self, valor):
        if valor < 0:
            print("Erro. Valor não foi alterado!")
        else:
            self.y = valor

ponto_1 = Point2D(7, 42)
ponto_2 = Point2D(1, 10)
ponto_1.set_x(13)
ponto_1.set_y(10)
ponto_2.set_x(42)
ponto_2.set_y(1)

print(ponto_1)
print("-"*80)
print(dir(ponto_1))
print("-"*80)
print(type(ponto_1))
print("-"*80)
