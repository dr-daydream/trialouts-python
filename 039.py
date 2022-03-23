# demigods - object oriented programming (oop)

from demigods import Demigods

percy = Demigods("Perseu Jackson", "Poseidon","Sally Jackson","Chalé 3","Anaklusmos","16")
annabeth = Demigods("Annabeth Chase", "Frederick Chase","Atena","Chalé 6","Adaga", "16")
luke = Demigods("Luke Castellan", "Hermes", "May Castellan", "Chalé 11", "Mordecostas", "23")



print("Nome: "+percy.name)
print("Pai: "+percy.father)
print("Mãe: "+percy.mother)
print("Chalé: "+percy.cabin)
print("Arma: "+percy.weapon)
print("Idade: "+percy.age)
print("Status: "+percy.status2)
percy.dead()
print("------------------------------")
print("Nome: "+annabeth.name)
print("Pai: "+annabeth.father)
print("Mãe: "+annabeth.mother)
print("Chalé: "+annabeth.cabin)
print("Arma: "+annabeth.weapon)
print("Idade: "+annabeth.age)
print("Status: "+annabeth.status1)
annabeth.alive()
print("------------------------------")
print("Nome: "+luke.name)
print("Pai: "+luke.father)
print("Mãe: "+luke.mother)
print("Chalé: "+luke.cabin)
print("Arma: "+luke.weapon)
print("Idade: "+luke.age)
print("Status: "+luke.status3)
luke.vessel()