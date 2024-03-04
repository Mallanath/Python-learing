# Create a function that return both the area and circumstance 
# of a circle given its radius
import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(4)

print("Area: ", a, "Circumference: ", c)
