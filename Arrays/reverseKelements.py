list1 = [1,2,3,4,5,6]

for i in range(3,6):
    current = list1[i]
    prev = i-1
    c = 0
    while prev>=0 and c <3:
        list1[i] = list1[prev]
        list1[prev] = current
        prev -= 1
        c += 1
    list1[prev+1] = current
print(list1)