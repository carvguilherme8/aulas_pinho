class AlunoEMap:
    def __init__(self):
        print("classe criada")



def func():
    pass

s = 1
t = 1.0
u = "Um"
v = True
x = [1, 2, 3]

tipo_s = type(s)
print(type(tipo_s))
print("-"*80)
print(type(s)) #Class <int>
print(type(t)) #Class <float>
print(type(u)) #Class <str>
print(type(v)) #Class <bool>
print(type(x)) #Class <list>
print(type(func)) #Class <function>
print(type(AlunoEMap)) #Class <type>

print(dir(s))
print(dir(t))
print(dir(u))
print(dir(v))
print(dir(x))
print(dir(func))
print(dir(AlunoEMap()))
