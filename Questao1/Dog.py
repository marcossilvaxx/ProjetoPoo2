from Animal import Animal

class Dog(Animal):

    def __init__(self, breed, name, weight, habitat):
        self.breed = breed
        super(Dog, self).__init__(name, weight, habitat)

    def play(self):
        print(self.name + " playing ")

    def guard(self):
        print(self.name + " guarding ")

    def __str__(self):
        return "Dog: %s" % self.name

niceDog = Dog("Chiuaua", "Bolinha", 5, "Casa")


print(niceDog)

niceDog.guard()
