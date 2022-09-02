import math

radius = 30
area_of_circle = math.pi * math.pow(radius, 2)
print("area is: ", area_of_circle, "Sqr Meter")

circum_of_circle = 2 * math.pi * radius

radius = input("Enter radius")

try:
    radius = int(radius)
    area_of_circle = math.pi * math.pow(radius, 2)
    print("area is: ", area_of_circle, "Sqr Meter")
except Exception:
    print('invalid input')