parul = {}
N=int(input())

for i in range(N):
    rollno = int(input("Enter roll no: "))
    marks = sum(map(int, input().split()))
    name = input("Enter name of student: ")
    parul.update({rollno : name})
    
print(parul)

