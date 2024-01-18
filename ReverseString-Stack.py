
class Stack:
    def __init__ (self,capacity):
        self.s = []
        self.cap = capacity
        self.top = 0
        self.bottom = 0
    
    def pushStk(self, num):
        if self.top == self.cap:
            print("Stack is full.")
            return
        self.s.append(num)
        self.top = self.top + 1
    
    def popStk(self):
        if self.top == self.bottom:
            print("Stack is Empty.")
            return
        ret = self.s[self.top-1]
        self.top = self.top - 1
        return ret
    
    def printStack(self):
        if self.top == self.bottom:
            print("Stack is Empty")
            return
        for i in range(self.top-1,-1,-1):  #Reversing Stack
            print(self.s[i])
        
    

    
if __name__ =="__main__":
    inp = input("Enter String to Reverse: ")
    inp = list(inp)
    s = Stack(len(inp))
    for i in inp:
        s.pushStk(i)
    
    print("Reversed String is: ")
    s.printStack()
    print()
    for i in range(len(inp)):
        print(s.popStk())

