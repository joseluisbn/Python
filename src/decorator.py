# Decorators: class methods, static methods

# From the class


class Human:
    # Attributes
    def __init__(self, name, surname, genre):  # __init__ is the constructor
        self.name = name
        self.surname = surname
        self.genre = genre

    # Methods
    def develop(self, hours):
        self.hours = 0
        print(f"is developing for {hours} hours")

    def sleep(self):
        print("Zzzzzzzz")

    @classmethod
    def my_method(cls):
        pass

    @staticmethod
    def my_static_method():
        pass
