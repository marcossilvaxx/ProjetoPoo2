class Animal:
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def mover(self):
         print("Movendo genericamente")

    def comunicar(self):
        print("Comunicando genericamente")

    def __str__(self):
        return "Animal: %s" % self.nome
