str1 = input()
str1 = list(str1)
d={}
sett = set(str1)
for i in sett:
    d.update({i:str1.count(i)})

print(d)

