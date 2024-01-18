class Node:
    def __init__ (self):
        self.data = 0
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.top = None
        self.__length = 0

    def push(self, inp):
        nn = Node()
        nn.data = inp
        if self.top == None:
            self.top = nn
            self.__length += 1
        else:
            nn.next = self.top
            self.top = nn
            self.__length +=1
    
    def pop(self):
 
        if self.top == None:
            print("List Empty")
            return
        else:
            popped = self.top
            self.top = self.top.next
            self.__length -= 1
        return popped.data

    def printList(self):
        current = self.top
        if self.__length == 0:
            print("List is empty")
            return
        while current != None:
            print(current.data,end="->")
            current = current.next

    def checkPalindrome(self, inp):
        is_Palindrome = True
        for char in inp:
            if char != obj.pop():
                is_Palindrome = False
                break
        if is_Palindrome:
            print(f"'{inp}' is a palindrome")
        else:
            print(f"'{inp}' is not a palindrome")

if __name__ == "__main__":
    obj = Linkedlist()
    inp = input("\nEnter string to check Palindrome or Not: ")
    for i in range(len(inp)):
        obj.push(inp[i])
    
    obj.checkPalindrome(inp)
    
    
    
