"This programme collects num and store the number and then sum it"
storage = []
summation= 0
for i in range(6):
    user_input= int(input("Enter your number "))
    storage.append(user_input)
# print(storage)
for i in storage:
    # print(i)
    summation +=i
print("Total sum of the num is " + str(summation))