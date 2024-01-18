def hamming(str1, str2):
    c=0
    l1,l2 = len(list(str1)),len(list(str2))
    cc = l1-l2 if (l1>l2) else l2-l1
    for i,j in zip(str1, str2):
        if i!=j:
            c +=1
    print(c + cc)

str1=input()
str2=input()
hamming(str1, str2)