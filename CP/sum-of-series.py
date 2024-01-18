n = int(input("Enter a number: "))
b=""
summ=0
for i in range(1,n+1):
    b=b+'3'*i
    summ= summ+int(b)
    b=""
print(summ)