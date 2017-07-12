from Animal import Animal
from Calda import Calda

class Peixe(Animal):

    def __init__(self, tipo):
        self.calda = Calda(tipo)

    def __str__(self):
        return "Calda do peixe: %s" % self.calda
