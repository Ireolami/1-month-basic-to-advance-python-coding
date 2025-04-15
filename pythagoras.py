#This simple calculator calculates the pythagoras theorem
# since a^2 +b^2 = c^2, this programme can collect the value of a and b and find c
import math
option = input('Which value are you looking for? a, b or c? ')
if option.lower() == "c":
    var_a = int(input("Enter value a: "))
    var_b = float(input("Enter value b: "))
    square_of_vara_varb = (var_a *var_a) + (var_b * var_b)
    result = math.sqrt(square_of_vara_varb)
    print(result)
elif option.lower() == 'b' or "a":
    var_1 =float(input("Enter angle 1: "))
    var_3 =float(input("Enter angle c: "))
    square = (var_3 * var_3) - (var_1 * var_1)
    result_2 = math.sqrt(square)
    print(f"The value of {option} is {result_2}")
else: 
    print("Invalid input")