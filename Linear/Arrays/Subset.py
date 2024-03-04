#Find the subset with sum target K
target = 4
arr = [1,2,1,3]

ans = []
summ = 0
i = 0
j = 1
d = ""

while i!=j:
    if j == len(arr):
        i += 1
        j = i+1
    summ += arr[i]+arr[j]
    d += str(arr[i])+str(arr[j])
    if summ == target:
        ans.append(d)
    j += 1
    if j==len(arr):
        j = i+2
sett= set(ans)
print(ans)
    