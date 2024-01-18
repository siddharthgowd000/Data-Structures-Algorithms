'''
    No stack frames are used by Lambda function. Thats why it is inline/Anonymous Function.
    A stack frame is a section of memory allocated on the stack for each function call.
'''

greet_me = lambda: "Hello"
print(greet_me())

str1 = "Siddharth"
str2 = "Rohan"
convert_upper = lambda str1, str2 : str1.upper() + "\n" + str2.upper() 
print(convert_upper(str1,str2))

# cube of x value
powerMe = lambda x : x**3

listt = [powerMe(x) for x in range(1,11)]
print(listt)