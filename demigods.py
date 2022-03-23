from calendar import monthcalendar, monthrange


class Demigods:

    status1 = "Viva"
    status2 = "Morto"
    status3 = "Receptáculo"

    def __init__(self, name, father, mother, cabin, weapon, age):
        self.name = name
        self.father = father
        self.mother = mother
        self.cabin = cabin
        self.weapon = weapon
        self.age = age

    def alive(self):
        print("A filha de "+self.mother+" está viva.")
    def dead(self):
        print("O filho de "+self.father+" está nos Campos Elíseos.")
    def vessel(self):
        print("O filho de "+self.father+" é a casca de Cronos.")