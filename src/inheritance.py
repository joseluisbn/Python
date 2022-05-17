class Animal:
    # Attributes
    def __init__(self, name, specie, genre):  # __init__ is the constructor
        self.name = name
        self.specie = specie
        self.genre = genre

    # Methods
    def eat(self):
        print(f"is eating")

    def sleep(self):
        print("Zzzzzzzz")


class Bird(Animal):
    pass


sparrow = Bird()

sparrow.eat
