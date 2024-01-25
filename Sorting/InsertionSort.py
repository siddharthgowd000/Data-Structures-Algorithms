list1 = [2,5,3,1,4]

current = 0
prev = 0
for i in range(1,len(list1)):
    current = list1[i]
    prev = i-1
    while list1[prev] > current and prev>=0 :
        list1[prev+1] = list1[prev]
        prev -= 1
    list1[prev+1] = current
print(list1)

