def isPrime(n):   
    flag = False
    c=0
    if n==1 or n==0:
        flag = False
    for i in range(2,n//2):
        if n%i == 0:
            flag = False
            break
    if flag == False:
        return False
    return True

n = int(input())
print(isPrime(n))