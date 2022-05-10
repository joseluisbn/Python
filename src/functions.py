# Functions in python

def user():
    name = input("What's your name?")
    age = input("How old are you?")
    print(name + age)


# Functions with parameters

user()


def another_user(name, age):
    print(f"Your name is {name} and your age is {age}")


another_user("Luis", 34)

# With return


def multiply(num1, num2):
    total = num1 * num2
    return total
