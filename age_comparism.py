#This is a simple programme that ask if user is greater than or equals to 18, 
# #if true, user can vote, else, user is old enough to vote

name = input('Kindly supply your name: ')
age = int(input('What is your age? '))
if age >= 18:
    print(f"Hi {name}!, you're {age} years old, congratulations because you're eligible to vote")
else:
    print(f"Hi {name}!, you're {age} years old, I'm sorry because you're not eligible to vote /nyou will be able to vote in {18 - age} years time")