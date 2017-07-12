from Animal import Animal

class Cachorro(Animal):

    def __init__(self,raca, nome, peso, habitat):
        self.raca = raca
        super(Cachorro, self).__init__(nome, peso, habitat)

    def brincar(self):
        print(self.nome + " brincando ")

    def vigiar(self):
        print(self.nome + " vigiando ")

    def __str__(self):
        return "Cachorro: %s" % self.nome

c = Cachorro("Chiuaua", "Bolinha", 5, "Casa")


print(c)

c.vigiar()
