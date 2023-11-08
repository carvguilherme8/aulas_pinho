class DeuRuimError(ZeroDivisionError):
    def __init__(self, message="Deu ruim, mané!"):
        self.message = message
        super().__init__(self.message)
    
def teste():
    raise DeuRuimError()

try:
    teste()
except Exception:
    print("Pelo menos tentamos :( 3")
except DeuRuimError:
    print("Pelo menos tentamos :( 2")
except ZeroDivisionError:
    print("Pelo menos tentamos :(")

#Organizar da mais genérica pra menos não faz sentido