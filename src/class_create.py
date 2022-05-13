# Class

class Human:
    # Attributes
    def __init__(self, name, surname, genre):  # __init__ is the constructor
        self.name = name
        self.surname = surname
        self.genre = genre

    # Methods
    def develop(self, hours):
        print(f"is developing for {hours} hours")

    def sleep(self):
        print("Zzzzzzzz")


# Object

my_human = Human("Hironobu", "Sakaguchi", "male")

print(my_human.name, my_human.surname)
print(my_human, my_human.develop(16))
