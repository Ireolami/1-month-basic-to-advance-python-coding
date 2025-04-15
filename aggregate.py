"This programme takes number as much as the user provides and calculate the sum"
all_number= []
while True:
    Decision = input('Do you want to enter  number? ')
    if Decision.lower() == 'yes':
        number =int(input('Enter a number to calculate the sum: '))
        all_number.append(number)

    else:
        print("System will now calculate the sum")
        break
import math
operation= input('which operation would you like to perform on them? ')
if operation == 'sum':
    print(sum(all_number))
elif operation =='sumproduct':
    dummy =[1 for _ in all_number]
    sump = sum(a*b for a, b in zip(dummy, all_number))
    print(f"The sum product is {sump}")
elif operation == 'avg':
    print(sum(all_number)//len(all_number))
print("Operation completed")