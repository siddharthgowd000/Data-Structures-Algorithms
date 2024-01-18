
def backSpace(str1):
    list1 = list(str1)
    for i in list1:
        if i == "#":
            list1 = list1[:list1.index(i)-1] + list1[list1.index(i)+1:]
    return "".join(list1)

str1 = input()
print(backSpace(str1))

