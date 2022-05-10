try:
    num1 = 4
    num2 = 0
    print(num1 / num2)
except ZeroDivisionError:
    print("A number cannot be divided by zero")
finally:
    print("Please, change variable's values if they are zero")
