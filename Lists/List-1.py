k = int(input())
n= int(input())
list1 = [x for x in range(1,n+1)]
list2=  []
for i in range(1,n+1,k):
    listt = []
    listt = [x for x in range(i,i+k) if x<=n]
    listt.sort(reverse=True)
    list2.extend(listt)
print(list2)

