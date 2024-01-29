l1 = [1, 3,2, 4, 5]
count = 0

for i in range(len(l1)):
    #count += 1
    for j in range(i,len(l1)):
        #count += 1
        if l1[i]>l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
            count += 1

print(l1)
print("Count: ",count)