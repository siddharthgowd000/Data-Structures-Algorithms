# from prefix to answer
# for postfix traverse from left to right opreand2 = top and next value is operand1
prefix = input().split(" ")
prefix = list(prefix)
n  = len(prefix)
stack = []
operators = ["+","-","*","/","^"]
ans = 0
for i in range(n-1,-1,-1): #normal traversal in postfix left to right

    if prefix[i] in operators:
        operand1 = int(stack.pop()) # reverse in postfix
        operand2 = int(stack.pop())
        match prefix[i]:
            case "+":
                ans = operand1 + operand2
                stack.append(ans)
            case "-":
                ans = operand1 - operand2
                stack.append(ans)
            case "*":
                ans = operand1 * operand2
                stack.append(ans)
            case "/":
                ans = operand1/operand2
                stack.append(ans)
            case "^":
                ans = operand1 ** operand2
                stack.append(ans)
    else:
        stack.append(prefix[i])
print(stack[0])
        
        