n=int(input("Enter a Number: "))
list1 = []
c=0
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            c=c+1
            break
    if c==0:
        list1.append(i)
    c=0
p=0
for i in list1:
    for j in list1[list1.index(i):]:   #Kadane algorithm
        if i+j == n:
            p = p+1
if p==0:
    print("0 Ways")
else:
    print(str(p)+" Ways")

#Write a program to give two sum of prime numbers that should equals to input number.
