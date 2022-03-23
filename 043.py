#overriding

class Seres:
    def vegano(self):
        print("Esse ser não come carne.")

class Satiro(Seres):
    def vegano(self):
        print("Mas adora uma enchilada!")

satiro = Satiro()
satiro.vegano()