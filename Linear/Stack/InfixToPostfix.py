infix = "(l-k/a)*(c/b-a)"
n = len(infix)
stack = []
dictt = {
    "(" : ")",
    "[" : "]",
    "{" : "}"
}

operators = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
    "^" : 3,
    "(" : -1
}
postfix = ""

for i in infix:
    if i.isdigit() or i.isalpha():
        postfix += i
    elif i in dictt.keys():
        stack.append(i)
    elif i in dictt.values():
        key_list = [key for key, val in dictt.items() if val == i]
        while len(stack) !=0 and stack[-1] != key_list[0]:
            postfix += stack[-1]
            stack.pop()
        if len(stack) != 0:
            stack.pop()
    elif i in operators.keys():
        while len(stack) != 0 and operators[stack[-1]]>operators[i]:
            postfix += stack[-1]
            stack.pop()
        stack.append(i)
while len(stack) !=0:
    postfix += stack[-1]
    stack.pop()

print(postfix)