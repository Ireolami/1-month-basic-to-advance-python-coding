"This programme is a continuation of the previous Exam programme with function and asking student to provide information"

def collect_details():
    students_Names, Department,Ages,phone =[],[],[],[]
    info = ['Name', 'Age', 'phone', 'Department']
    while True:
        for inf in info:
            details =input(f'Enter your {inf}: ')
            if details.strip() is not None:
                if inf =='Name':
                    students_Names.append(details.title())
                elif inf == 'Age':
                    Ages.append(int(details))
                elif inf == 'phone':
                    while len(details) != 11:
                        details =input(f'Phone number cannot be less than 11, Enter your {inf}: ')

                    else:
                        phone.append((details))
                elif inf == 'Department':
                    Department.append(details.title())
            else:
                details = input(f"Your {inf} cannot be empty. Enter your {inf}: ").title()
        asking= input('Do you want to register another student? ')
        if asking not in ('yes', 'y'):
            break
    return students_Names, Department, Ages, phone
student =collect_details()
import time
def exam():
   
    print('Kindly read the question properly, each question carries equal mark\n for every question you get right, you get 5 and for every question you miss, 2 is deducted from your score')
    question = ['1. Who is the president of nigeria?', '2. Where is the capital of Nigeria?',
                '3. Naira is to Nigeria as ___ is to Czech?', '4. Where is Lionel Messi from?',
                '5. In forex, what does XAUUSD mean?', '6. The following are countries in Africa except?',
                "7.Who wrote the book 'poor Dad, Rich Dad'?", '8. These are social media except ___?', '9. Who is the president of Burkina Faso?',
                '10. Who is the Senate President of Nigeria?']
    options = ['a. President Muhammad Buhari\nb. President Bola Ahmed Tinubu\nc.President Gregory Peter Obi',
            'a. Abuja\nb.Lagos\nc.Portharcourt', 'a. Swiss\nb.Dollar\n.Krona', 'a. Brazil\nb. Argentina\nc. Nigeria',
            'a. Gold-United State Dollar\nb. Silver-United State Dollar\nc. Xaugh-United State Dollar',
            'a. Ghana\n b.Ivory Coast\nc. Estonia', 'a. John C. Maxwell\nb. Richard Kiyosaki\nc. Chimamanda Achebe',
            'a. Facebook\nb. Apple\nc. X', 'a. President Babangida Ibrahim\n b. Col. Ibrahim Traore\n c. President Donald J. Trump',
            'a Senator Dino Melaye\nb. Senator Omoyele Sowore\nc. Senator Godswill Akpabio']
    answer =['b', 'a', 'c', 'b','a','c','b','b','b','c']
    score, n= 0,0

    for stu in student[0]:

        for que, option in zip(question, options):
            print(que)
            print(option)
            ans = input("Enter your answer below:\n ")
            if ans==answer[n]:
                score += 5
                print(f'Correct! you have additional 5, you score is {score}')
                
            else:
                score -=2
                print(f'Wrong answer, you just lost 2 scores, your score is {score}')
            n +=1
            time.sleep(2)
    print(f'Your total score is  {score}')