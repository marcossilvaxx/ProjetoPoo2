from Animal import Animal
from Tail import Tail

class Peixe(Animal):

    def __init__(self, type):
        self.tail = Tail(type)

    def __str__(self):
        return "Fish tail: %s" % self.tail
