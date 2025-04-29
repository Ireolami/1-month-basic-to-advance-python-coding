#This programme performs on an operation of a(1+c)+b/b(2a+3b)
"""This is the same as 
a +ca +b
---------
b(2a + 3b)

Algorithm
"""


val_a = int(input("Enter value a: "))
val_b = int(input('Enter value b: '))
val_c =int(input("Enter value c: "))
#Calculation
result = (val_a*(1 + val_c) +val_b )/(val_b*(2*val_a +3*val_b))
# print(f'{result:.3f}')
print(round(result, 3))