str1 = "Python Programming"
print(len(str1))

# Replace function

print(str1.replace("Python","Sid"))

str2="python python"
print(str2.replace("python","Sid",1))

# Join Function
print('-'.join(str1))

# Find method
print(str1.find("P"))

print(str1.find("P",8))

print(str1.find("P",5,7))

# same as for index also like find
print(str1.index("n"))
# find finds the given input present or not , but in index it gives error if it is not present in the string.
print(str1.find("z"))
#print(str1.index("z"))

# checking all numbers or not with isalnum()

print(str1.isalnum())
str3 = "123"
print(str3.isalnum())

