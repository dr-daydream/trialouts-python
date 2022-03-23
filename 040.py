# inheritance

class Deuses:
    alive = True
    def danger(self):
        print("Esse deus é perigoso.")
    def peaceful(self):
        print("Esse deus é pacífico.")

class Ares(Deuses):
    def guerra(self):
        print("Ele é o deus da guerra.")
class Hefesto(Deuses):
    def forja(self):
        print("Ele é o deus das forjas.")
class Hades(Deuses):
    def mortos(self):
        print("Ele é o deus dos mortos.")

ares = Ares()
hefesto = Hefesto()
hades = Hades()

ares.danger()
ares.guerra()
hefesto.peaceful()
hefesto.forja()
hades.peaceful()
hades.mortos()