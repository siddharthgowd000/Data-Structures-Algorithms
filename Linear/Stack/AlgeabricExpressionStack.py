class Stack:
    def __init__(self, size):
        self.s = []
        self.top = 0
        self.bottom = 0
        self.size = size
    
    def push(self, num=0):
        if self.top == self.size:
            print("Stack is Overflow.")
            return
        self.s.append(num)
        self.top += 1

    def pop(self):
        if self.top == self.bottom:
            print("Stack is Underflow.")
            return
        ret = self.s[self.top-1]
        self.top -= 1

        return ret
    
    def printStk(self):
        if self.top == self.bottom:
            print("Stack is Empty.")
            return
        for i in range(self.top):
            print(self.s[i])
    
    def isOperator(self,ch):
        return ch in ["+", "-","*","/","^"]
    
    def precedence(self,op):
        if op == "^":
            return 3
        elif op == "*" or op == "/":
            return 2
        elif op == "+" or op == "-":
            return 1
        else:
            return -1

    def postfixStk(self, expression):
        postfix = ""
        for ch in expression:
            if ch.isalnum():  # If the character is an operand, add it to postfix
                postfix += ch
            elif ch == '(':  # If the character is '(', push it to stack
                self.push(ch)
            elif ch == ')':  # If the character is ')', pop and output from the stack until '(' is encountered
                while self.top > 0 and self.s[self.top - 1] != '(':
                    postfix += self.pop()
                self.pop()  # Pop '(' from the stack but don't add it to postfix
            else:  # If the character is an operator
                while self.top > 0 and self.precedence(ch) <= self.precedence(self.s[self.top - 1]):
                    postfix += self.pop()
                self.push(ch)

        return postfix


if __name__ == "__main__":
    A = input()
    stk = Stack(len(A))
    
    
    print(stk.postfixStk(A))
    stk.printStk()

    

