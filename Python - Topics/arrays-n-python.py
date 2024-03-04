from array import *

my_arr = array('i',[1,2,3,4])

print(type(my_arr))
print(my_arr,my_arr[0])
my_arr.append(10)
print(my_arr)
my_arr.insert(0,10)
print(my_arr)

l = [1,2,3,4]
l2 = [5,6,7]
l.extend(l2)
print(l)

my_arr.fromlist(l[2:4])
print(my_arr)

'''
#str1 = my_arr.tostring()
#print(type(my_arr))
#print(type(str1))
print(my_arr)


print(type(my_arr[0]))
print(str1[0],type(str1[0]))
print(str1[1],type(str1[1]))  #need to learn STRING memory allocation
print(str1[2],type(str1[2]))'''


c = my_arr.tolist()
print(type(c))

listt =[1,2,0,4]
list2 = [1,2,3,4]
list3 = [-1,-2,1,2]

print(all(listt)) # except 0 all are True Iterable.
print(all(list2))
print(all(list3))

list4 = [0,0,1,False]
print(any(list4)) # atleast one non zero or false should be there then return true.





#difference between array and list?
# https://byjus.com/gate/difference-between-list-and-array-in-python/#:~:text=In%20a%20list%2C%20the%20complete,the%20components%20of%20the%20array.&text=It%20favors%20a%20shorter%20sequence,a%20longer%20sequence%20of%20data.