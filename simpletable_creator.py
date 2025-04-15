'This programme collects a number from a user and creates table based on the number'
numb = int(input('Enter your number: '))
for i in range(1, numb):
    print(f'{i} \t {i*numb}')
