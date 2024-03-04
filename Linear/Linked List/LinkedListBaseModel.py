class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
        self.length = 0
    
    def insertNode(self, val):
        nn = Node(val)
        if not self.head:
            self.head = nn
            self.temp = nn
            self.length += 1
        else:
            self.temp = self.head
            while self.temp.next:
                self.temp = self.temp.next
            self.temp.next = nn
            self.length += 1
    
    def insertAtBegin(self,val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn
        self.temp = self.head
        self.length += 1
    
    def deleteNode(self):
        if not self.head:
            print("Empty")
        elif not self.head.next:
            self.head = None
            self.length -= 1
        else:
            self.temp = self.head
            while self.temp.next.next:
                self.temp = self.temp.next
            self.temp.next = None
            self.length -= 1
        
    def printList(self):
        if not self.head:
            print("empty")
            return
        
        self.temp = self.head
        while self.temp:
            print(self.temp.val,end="->")
            self.temp = self.temp.next

ll = LinkedList()
ll.insertAtBegin(5)
ll.insertNode(6)
ll.insertNode(7)
ll.insertAtBegin(8)
ll.printList()
ll.deleteNode()
ll.printList()