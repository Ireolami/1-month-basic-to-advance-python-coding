#This programme is a modification of the previous programme and it can be used to 
#to find the index of a max number. Two approaches will be used, the zip and dictionary approach

def collect_num():
    scores = []
    names=[]
    while True:
        name = input('Enter your name: ').upper().strip()
        names.append(name)
        try:
            score= int(input('Enter your score: '))
            scores.append(score)
            
        except ValueError:
            another= int(input("Invalid score, pls enter a numerical value: "))
            scores.append(another)
        next =input('Would you like to enter another information? ')
        if next not in ("yes", 'y'):
            break
    return names, scores
def student_with_maximum(names, scores):
    info = max(zip(names, scores), key=lambda x:x[1])
    
    return info
names, scores = collect_num()
maxi = student_with_maximum(names, scores)
print(f'The student with the highest score is {maxi[0]} and his or her score is {maxi[1]}')
    
