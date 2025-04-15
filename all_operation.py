#This simple programme performs all arithmetic operations
try:
    value1= float(input('Input value 1: '))
    value2= float(input('Input value 2: '))
except ValueError:
    print('Invalid input')
    exit()
operation = input('Which operation would you like to perform (+, -, *, / %, ? ')

def addition():
    return value1 + value2
def subtraction():
    return value1 - value2
def multiplication():
    return value1 * value2
def division():
   if value2 == 0:
       print("Cannot divide by 0")
   return value1/value2
def modulus():
    if value2 ==0:
        print("Cannot find modulus by 0")

if operation == '+':
    print(addition())
elif operation == '-':
    print(subtraction())
elif operation == '*':
    print(multiplication())
elif operation == '/':
    print(division())
elif operation == '%':
    print(modulus())
else:
    print('Invalid operation')