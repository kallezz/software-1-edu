import random

dices = input("How many dice to roll: ")


try:
    dices = int(dices)
except ValueError:
    print("Invalid input")

rolls = []
for i in range(dices):
    rolls.append(random.randint(1, 6))


print(f"Sum of the dice: {sum(rolls)}")