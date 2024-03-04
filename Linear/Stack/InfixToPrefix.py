infix = "(a-b/c)*(a/k-l)"
reversedInfix = ""

for i in range(len(infix)-1,-1,-1):
    if infix[i] == "(":
        reversedInfix += ")"
    elif infix[i] == ")":
        reversedInfix += "("
    else:
        reversedInfix += infix[i]

reversedPrefix = ""

def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    if operator == "^":
        return 3
    return -1

stack = []
for i in reversedInfix:
    if i.isalpha() or i.isdigit():
        reversedPrefix += i
    elif i == "(":
        stack.append(i)
    elif i ==")":
        while len(stack) != 0 and stack[-1] != "(":
            reversedPrefix += stack[-1]
            stack.pop()
        stack.pop()
    else:
        while len(stack) !=0 and precedence(stack[-1]) > precedence(i):
            reversedPrefix += stack[-1]
            stack.pop()
        stack.append(i)
while len(stack) !=0:
    reversedPrefix += stack[-1]
    stack.pop()
prefix = ""
for i in reversedPrefix[::-1]:
    if i == "(":
        prefix += ")"
    elif i == ")":
        prefix += "("
    else:
        prefix += i
print(prefix)