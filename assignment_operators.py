# "This programme is algorithm that performs all  operators such as and, or, -=, +=, *=, /=, %="
# #Simple total score calculator
# number_of_subjects =int(input('What is the total number of courses? '))
# total = 0
# for i in range(1, number_of_subjects):
#     scores = int(input("Enter your score for subject " + str(i) + " "))
#     total +=scores

# print("Your total score is " +str(total))

#Debt payment plan
total_loan = 1000000
no_of_instalments = int(input("Enter the number of times you want to pay the loan: "))
payment_per_installment = total_loan/no_of_instalments
for i in range(no_of_instalments):
    while True:
        try:
            payment = int(input(f"The total amount you are paying this month is {payment_per_installment}\n,Enter the amount to pay: "))
        except ValueError:
            payment= int(input('Payment must be figure '))
        if payment:
            if payment == payment_per_installment:
                print(f"You have successfully paid your loan for this month, the amount paid is {payment}\n and your balance is {total_loan}")
                break
            else:
                outstanding = payment_per_installment - payment
                attempt =0
                while outstanding !=0:
                   
                    asking = input(f"Would you like to pay the remaining outstanding of {outstanding}? ")
                    if asking not in ("yes", 'y'):
                        attempt +=1
                        if attempt ==2:

                            interest_balance = (payment_per_installment -payment) * 0.1
                            total_loan += interest_balance
                            print(f'You did not pay your outstanding, else, we will be charging you with interest of {interest_balance}\nYour new loan balance is {total_loan} ')
                            break
                    else:
                        payment2 = int(input(f"Pls pay an outstanding of {outstanding}"))
                        
                        total_loan -= (payment +payment2)
                        print(f"You have successfully pay your loan for this month\nYour new balance is {total_loan}")
                        break
                else:
                    total_loan -=payment + outstanding
                    print(f"You have been able to pay your loan for this month\n Total loan paid is {payment_per_installment}\nYour loan balance is {total_loan}")
                    
                       

        else:
            attempt =0
            try:
                payment =int(input("You must make your payment now: "))
            except ValueError:
                payment =int(input("You must make your payment now: "))
            attempt += 1
            if attempt == 2 and payment is None:
                print("You failed to pay your outstanding for this month")
                interest = 0.15 * payment_per_installment
                total_loan +=interest
                print(f"Your interest for the failed month is {interest} and your loan balance is {total_loan}")
                break
            else:
                print(f'You are able to pay your loan on time, your loan balance is {total_loan}')
                break
if total_loan ==0:
    print(f"Thank you so much for paying your loan on time. You've successfully paid your loan and your balance is {total_loan}")
else:
    print(f'You failed to balance your loan payment, you loan balance is {total_loan}')
