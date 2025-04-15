#This programme runs until the users stops it and find the max number in user inputs

def num_collector():
    numbers =[]
    while True:
        try:
            number= int(input('Enter your number: '))
            numbers.append(number)
        except ValueError:
            next= input('Your input is invalid, enter done to stop ')
            if next == 'done':
                break
            else:
                continue
        next_input = input("Would you like to enter a new number? ")
        if next_input not in ('yes', 'y'):
            break
    return numbers

def find_max(numbers):
    if not numbers:
        return None
    else:
        return max(numbers)
all_numbers = num_collector()
maxi=find_max(all_numbers)
print(f'The maximum number is \n {maxi}')