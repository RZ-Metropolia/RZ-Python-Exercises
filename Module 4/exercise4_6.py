from random import random

points_total = int(input("Enter the total number of points you want to generate:\n"))
points_in_circle = 0
points_tested = 0

while points_tested < points_total:
    point_x = random()
    point_y = random()

    if point_x**2 + point_y**2 < 1:
        points_in_circle = points_in_circle + 1

    points_tested = points_tested + 1

pi = 4*points_in_circle / points_total
print(pi)