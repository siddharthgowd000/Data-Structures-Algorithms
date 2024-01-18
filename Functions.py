
#docstring acts as commment in function -> ""
def isPrime(n):
    c=0
    if n==1 or n==0:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                c=c+1
                break
        if c==0:
            return True
        else:
            return False
    

b=int(input())
count=0
str1=""
check=0
i=1

while (True):
    str1 = ""
    str1 = str1 + str(i);
    for j in range(len(str1)):
        if isPrime(int(str1[j])):
            check = check + 1
    if check == len(str1):
        count = count+1
    if b == count:
        print(i)
        break
    i = i+ 1
    check = 0
    