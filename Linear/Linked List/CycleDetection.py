class Node:
    def __init__ (self):
        self.data = 0
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.head = None
        self.temp = None
        self.__length=0
    
    def appendNode(self, num=0):
        nn = Node()
        nn.data = num
        #self.temp = self.head
        if self.head == None:
            #list is empty
            self.head = nn
            self.temp = nn
            self.__length += 1

        else:
            #list is present
            self.temp = self.head
            while self.temp.next != None:
                self.temp = self.temp.next
            self.temp.next = nn
            self.__length += 1

    def deleteNode(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            self.__length -= 1
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None
        self.__length -= 1

    def makeCycle(self, position):
        current = self.head
        cycleNode = Node()
        count = 1
        while current.next != None:

            if count == position:
                    cycleNode = current
            current = current.next
            count += 1
        
        current.next = cycleNode
    
    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def removeCycle(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                fast = self.head
                break
        
        while fast.next != slow.next:
            fast = fast.next
            slow = slow.next
        slow.next = None


    def printList(self):
        if self.__length == 0:
            print("List is Empty")
            return
        self.temp = self.head
        while self.temp != None:
            print(self.temp.data, end="->")
            self.temp = self.temp.next
        print()

    def lengthOfList(self):
        print("Length of Linked List is: ", self.__length)

    
    
            
if __name__ == "__main__":
    obj = Linkedlist()
    for i in range(5):
        obj.appendNode(int(input("enter number: ")))
    position = int(input("Enter the position you want to make cycle: "))
    obj.makeCycle(position)
   
    a = obj.detectCycle()
    print(a)
    obj.removeCycle()
    a = obj.detectCycle()
    print(a)
        
    
        

