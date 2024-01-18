if __name__ == '__main__':
    list1=[]
    list2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        list2.append(score)

    minn = min(set(list2))
    list2 = set(list2)
    if minn in list2:
        list2.remove(minn)
    for i in list1:
        if minn == i[1]:
            list1.remove(i)
    minn = min(list2)
    
    list2 = []
    for i in list1:
        if minn in i:
            list2.append(i[0])
    list2.sort()
    for i in list2:
        print(i)
    
    
        
