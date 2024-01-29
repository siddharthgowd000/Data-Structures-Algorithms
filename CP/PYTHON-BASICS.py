m = 20
sum = 0
while m <= 30:
    if m%2 == 0:
        sum = (sum + 1)
    if m%5 == 0:
        sum = (sum+2)
    m = (m+1)
print(sum)

print("\n2.")

dict_a = {
    'name': "sid",
    'age' : 20
};

dict_b = dict_a.copy()
for k in dict_a.keys():
    if k == 'name':
        del dict_b[k]
print(dict_b)

print("\n3.")
listt = ["a","b"]
listt += list("cd")
print(listt)

print("\n4.")

from datetime import datetime

now = datetime.now()
now2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print(type(now2))

print("\n5.")
print(len("python"+"3"))

print("\n6.")
a = 10.5
a = int(a)
print(a)

# Map, Filter, Reduce methods are iteratable and applies function passed.

print("\n7.")

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def fullname(self,firstname = "Sai", lastname="megha"):
        return "{} {}".format(self.firstname, self.lastname)

obj = Person("Ravi", "Kumar")
print(obj.fullname("sai","megha"))

print("\n8.")

x = 2
for i in range(x):
    x = x+1
    print(x)

'''print("\n9.")
set_a = {5,[8,9]}
print(set_a[1])'''


print("\n10.")

word = "Leader"
modified = word[1:5:-2]
listt = list(word)
listt = listt[1:5:-2]
listt = "".join(listt)
is_same = listt == modified
print(is_same)

print("\n11.")

r = "good gmorning morning"
m = r.replace("morning", "evening")
print(m)

print("\n.12")

aa = []
for i in range(1,4):
    aa = [i]
print(aa)

print("\n13.")
num = 10
for i in str(num):
    print(i)
'''dictt = {
    'name': "sid"
};
str_a = dictt['city']
str_b = dictt.get('city')
print(str_a == str_b)'''
print("\n14.")



print("\n15")

k = "toe"
l = "tic"
m = "tac"
o = "{}"
print(o.format(k,l,m))

aaa = "4.2"
aaa = int(aaa)
print(type(aaa))