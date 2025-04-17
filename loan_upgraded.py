import mysql.connector as connection
import re
import time
import sys
from Bank_verification import create
myconn = connection.connect(
    host="127.0.0.1", user="root", password="DigitalWorld1.", database="i_loan"
)
cursor = myconn.cursor()
querry = """
        INSERT INTO customers(customer_id, FirstName, LastName, Address, PhoneNumber, Username, 
        pwd, Email, Next_of_kin, Next_of_kin_Number, BVN)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)"""

def bvn_search():
    bvnconn= connection.connect(host='127.0.0.1', 
                                user='root', 
                                password='DigitalWorld1.', 
                                db='bvn_creation')
    bvncursor =bvnconn.cursor()
    bvnquerry ='SELECT BVN FROM Bvn'
    bvncursor.execute(bvnquerry)
    global result
    result = [str(row[0]) for row in bvncursor.fetchall()]

    bvncursor.close()
    # if result:
        #print(f"Found {result}")

bvn_search()
def confirm_bvn():
    print("You are welcome to i-Loan App\n\nDo you have a BVN?")
    response =input("Enter yes or no: ")
    if response.lower() in ('yes', 'y'):
        user_registration()
    else:
        next_step = input("Would you like to register for BVN? Enter Yes to Register and No to Exit: ")
        if next_step.lower() not in ('yes', 'y'):
            print("Sorry you cannot register for this Application without BVN")
            sys.exit()
        else:
            print("You are being redirected to BVN Creation portal\nRedirecting")
            time.sleep(5)
            create()
def user_registration():
    print("📋 Please fill in your details:")
    info_needed =['FirstName', 'LastName', 'Address', "PhoneNumber", "Username", "pwd", "Email", "Next_of_kin", "Next_of_kin_Num", "BVN"]
    global user_info
    user_info =[]
    customer_id =20250417
    user_info.append(customer_id)
    for i in info_needed:
        while True:
            
            value = input(f"Enter your {i}: ").strip()

            
            
            if i =='PhoneNumber':
                confirmation = value.isdigit() and len(value) ==11
                if not confirmation:
                    print("❌ Phone number must be 11 digits.")
                    continue
            elif i == 'Email':
                email_confirmation=re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value)
                if not email_confirmation:
                    print("❌ Invalid email format.")
                    continue

            elif i == 'pwd':
                password_validator = (len(value) >= 8 and re.search(r'[A-Z]', value) and re.search(r'[a-z]', value) and re.search(r'[0-9]', value))
                if not password_validator:
                    print("❌ Password must be at least 8 characters and contain upper, lower, and numbers.")
                    continue

            elif i=="Next_of_kin_Num":
                Next_confirmation = value.isdigit() and len(value) ==11
                if not Next_confirmation:
                    print("❌ Phone number must be 11 digits.")
                    continue

            elif i == 'BVN':
                print('pls hold while we searching for your Bank Verification Number ...')
                time.sleep(5)
                if value not in result:
                    bv_decision = input("Bank Verification Number not found\nEnter 1 to Try again\nEnter 2 to register new BVN\nEnter 3 to Exit the App: ")
                    if bv_decision == '1':
                        value = input(f"Enter your {i}: ").strip()
                    elif bv_decision == '2':
                        print('You are being redirected to BVN creation portal\nRedirecting...')
                        time.sleep(5)
                        create()
                        print("You are welcome back")
                        user_registration()
                    elif bv_decision== '3':
                        print("Thank you for checking i-Loan Application\nSystem is shutting down")
                        sys.exit()
                    else:
                        print('You made an unclear decision\nThe registration process will begin again')
                        user_registration()
                        

                    

            # Passed validation
            user_info.append(value)
            break

    

user_registration()
cursor.execute(querry, user_info)
myconn.commit()
cursor.close()


    