def demoMap(x):
    return x*3

l1 = [1,2,3]
list1 = list(map(demoMap, l1))
print(list1)

l2 = [4,5,6,10,11]

def demoMap1(x,y):
    return x*y


list2 = list(map(demoMap1, l1,l2))
print(list2)

list3 = list(map(lambda x,y: x*y,l1,l2))
print(list3)