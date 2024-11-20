import math

radius = float(input("Enter the radius of the sphere: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius ** 3

print("Diameter of the sphere:", diameter)
print("Circumference of the sphere:", circumference)
print("Surface area of the sphere:", surface_area)
print("Volume of the sphere:", volume)
