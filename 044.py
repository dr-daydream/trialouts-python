# method chaining

class Carro:
    def ligar(self):
        print("Você ligou o motor.")
        return self
    def dirigir(self):
        print("Você dirigiu o carro.")
        return self
    def freio(self):
        print("Você freiou o carro.")
        return self
    def desligar(self):
        print("Você desligou o carro.")
        return self

carro = Carro()
carro.ligar()\
    .dirigir()\
    .freio()\
    .desligar()