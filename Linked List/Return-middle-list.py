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


    def middleElement(self):
        fast = self.head
        slow = self.head

        while fast and fast.next :
            slow = slow.next
            fast= fast.next.next
        if self.__length%2 == 0:
            return slow.data, slow.next.data
        return slow.data
    def printList(self):
        if self.__length == 0:
            print("List is Empty")
            return
        self.temp = self.head
        while self.temp != None:
            print(self.temp.data, end="->")
            self.temp = self.temp.next
        print()

ll = Linkedlist()
for i in range(1,7):
    ll.appendNode(i)
ll.printList()
print(ll.middleElement())