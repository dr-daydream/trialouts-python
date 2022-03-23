#multiple inheritance 

class Deuses:
    def gods(self):
        print("Esse é olimpiano.")

class Titans:
    def titans(self):
        print("Esse é Titã.")

class Japeto(Titans):
    pass
class Poseidon(Deuses):
    pass
class Afrodite(Deuses, Titans):
    pass

japeto = Japeto()
poseidon = Poseidon()
afrodite = Afrodite()

japeto.titans()
poseidon.gods()