

l1 = [1,2,3,10,11]
l2 = [4,5,6]

for item in zip(l1,l2): # returns as a tuple .
    print(item)

for x,y in zip(l1,l2):   # as a variables.
    print(x,y)

powerMe = lambda x,y : x**y

for x,y in zip(l1,l2):   # as a variables.
    print(powerMe(x,y))
