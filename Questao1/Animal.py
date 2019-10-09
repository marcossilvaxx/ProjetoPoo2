class Animal:
    def __init__(self, name, weight, habitat):
        self.name = name
        self.weight = weight
        self.habitat = habitat

    def move(self):
         print("Moving generically")

    def comunicates(self):
        print("Communicating generically")

    def __str__(self):
        return "Animal: %s" % self.name
