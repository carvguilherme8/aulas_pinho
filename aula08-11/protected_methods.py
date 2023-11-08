class foo:
    def __init__(self):
        self.public = "Public" #Qualquer unidade pode utilizar
        self._protected = "Protected" #Utilizado na classe e em subclasses
        self.__private = "Private"

    def public_method(self):
        print("Método Público")
        self._protected_method()
        self.__private_method()

    def _protected_method(self):
        #self.public_method()
        print("Método Protegido")

    def __private_method(self):
        print("Método Privado")

class Bar(foo):
    def using_parent_public_method_and_attributes(self):
        print("OK invocar métodos públicos e acessar atributos públicos")
        super().public_method()
        print(self.public)

    def using_parent_protected_method_and_attributes(self):
        print("OK invocar métodos públicos e acessar atributos protegidos")
        super()._protected_method()
        print(self._protected)

    def using_parent_private_method_and_attributes(self):
        print("OK invocar métodos públicos e acessar atributos privados")
        super()._foo__private_method()
        print(self._foo__private)

print("#"*40)
object_ = foo()
print(object_.public)
object_.public_method()

print("#"*40)
print("ERRO SEMÂNTICO")
print(object_._protected)
object_._protected_method()

print("#"*40)
print("ERRO SEMÂNTICO")
print(object_._foo__private)
object_._foo__private_method()

print("#"*40)
object_ = Bar()
object_.using_parent_private_method_and_attributes()
object_.using_parent_protected_method_and_attributes()
object_.using_parent_public_method_and_attributes