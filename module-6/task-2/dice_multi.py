import random


def roll_dice(sides):
    return random.randint(1, sides)


sides_input = int(input())

while True:
    roll = roll_dice(sides_input)
    print(roll)

    if roll == sides_input:
        break