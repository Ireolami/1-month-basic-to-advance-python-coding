#This is an intermediate version of our loan payment stimulation app. On this app, you can borrow and pay your loan
def user_registration():
    "Pls fill your information and make sure your enter valid details"
    info_needed =['First Name', 'Last Name', 'Address', 'Phone Number', 'Email', 'Username', 'Password', 'Bank Verification Number', 'Phone Number', 'Next of Kin', ]
    
def get_valid_integer(prompt):
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def confirm(prompt):
    """Prompt the user for yes/no confirmation."""
    return input(prompt).lower() in ['yes', 'y']

def loan_payment_system():
    total_loan = 1_000_000
    no_of_installments = get_valid_integer("📆 Enter the number of times you want to pay the loan: ")
    payment_per_installment = total_loan / no_of_installments
    total_paid = 0

    print(f"\n💰 Your loan amount is ₦{total_loan:,.2f}, to be paid in {no_of_installments} installments of ₦{payment_per_installment:,.2f} each.\n")

    for i in range(1, no_of_installments + 1):
        print(f"\n📅 Payment {i} of {no_of_installments}")
        while True:
            payment = get_valid_integer(f"Enter amount to pay this month (₦{payment_per_installment:,.2f} expected): ")

            if payment == payment_per_installment:
                total_loan -= payment
                total_paid += payment
                print(f"✅ Payment successful! Loan balance: ₦{total_loan:,.2f}")
                break

            elif payment < payment_per_installment:
                outstanding = payment_per_installment - payment
                total_paid += payment

                print(f"⚠️ You paid ₦{payment:,.2f}, which is ₦{outstanding:,.2f} short.")

                if confirm("Would you like to pay the outstanding now? (yes/no): "):
                    top_up = get_valid_integer(f"Enter additional payment of ₦{outstanding:,.2f}: ")
                    if top_up == outstanding:
                        total_loan -= (payment + top_up)
                        print(f"✅ Full payment received. Loan balance: ₦{total_loan:,.2f}")
                    else:
                        interest = (outstanding - top_up) * 0.1
                        total_loan = total_loan - (payment + top_up) + interest
                        print(f"⚠️ Partial top-up received. Interest of ₦{interest:,.2f} applied.")
                        print(f"New loan balance: ₦{total_loan:,.2f}")
                    break
                else:
                    interest = outstanding * 0.1
                    total_loan = total_loan - payment + interest
                    print(f"⚠️ Outstanding unpaid. Interest of ₦{interest:,.2f} applied.")
                    print(f"New loan balance: ₦{total_loan:,.2f}")
                    break

            elif payment > payment_per_installment:
                extra = payment - payment_per_installment
                total_loan -= payment
                total_paid += payment
                print(f"✅ You overpaid by ₦{extra:,.2f}. Loan balance: ₦{total_loan:,.2f}")
                break

    
    print("\n🔚 Loan Payment Summary")
    print(f"Total Paid: ₦{total_paid:,.2f}")
    print(f"Loan Balance: ₦{total_loan:,.2f}")

    if total_loan <= 0:
        print("🎉 Congratulations! You have completed your loan repayment.")
    else:
        print("⚠️ You still have an outstanding loan balance. Please settle it as soon as possible.")


loan_payment_system()
