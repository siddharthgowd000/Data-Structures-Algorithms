n=int(input("Enter number: "))
summ=0
for i in range(1,(n*n)+1):
    if i%n ==0:
        print(i,end="\n")
    else:
        print(i,end="*")
    