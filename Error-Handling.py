n = int(input())
str1=""
for i in range(1,n+1):
    if i <= n//2:
        print(" "*(i-1)+str(i)+" "*(n-i*2)+str(n-i+1))
    if i>n//2:
        print(" "*(n-i)+str(n-i+1)+" "*(i-n+2)+str(i))