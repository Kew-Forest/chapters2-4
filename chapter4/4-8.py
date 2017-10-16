#Write a function area_of_circle(r) which returns the area of a circle of radius r.
import math

pi = math.pi
radius = float(input("radius of circle: "))
def area_of_circle(r):
    area = pi * radius **2
    return area

area = area_of_circle(radius)
print(area)
