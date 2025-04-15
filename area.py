#This programme finds area of circle
# radius =float(input("Enter the radius of the circle, this can only be figure: "))
# radius_square = radius * radius
# print(f"The area of the circle is {3.14 * radius_square}")

#Using function
import math
def area(radius):
    area_of_circle = math.pi * radius **2
    return area_of_circle

print(f"The area of the circle is {area(5)}")