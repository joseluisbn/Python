# Lists

from random import random


gang = ["Dani", "Yajie", "Lucía", "José Luis"]
print(gang)

# To print a concrete value, we use indexes

print(gang[1])

## Adding a new member

gang.append("María")
print(gang)


## Delete a member

gang.pop((4))
print(gang)

# Sort list

gang.sort()
print(gang)
