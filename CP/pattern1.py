n=int(input("Enter a number: "))

for i in range(1,n+1):
    print("\n")
    for j in range(1,i+1):
        if i<=n:
            print("*",end=" ")
        else:
            print("* "*(n-j))
    