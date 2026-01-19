import random

try:
    points = int(input("How many points: "))
except ValueError:
    print("Invalid input")

points_in_circle = 0

i = 0

while i in range(points):
    point = (random.uniform(-1, 1), random.uniform(-1, 1))

    if point[0] ** 2 + point[1] ** 2 < 1:
        points_in_circle += 1

    i += 1

pi_approx = 4 * points_in_circle / points

print(f"Approximation of pi: {pi_approx}")