n = int(input("Enter a Number: "))

c=0
for i in range(1,n):
    for j in range(i,n):
        for k in range(j,n):
            for l in range(k,n):
                if i+j+k+l == n:
                    c=c+1
print(str(c)+" Ways")