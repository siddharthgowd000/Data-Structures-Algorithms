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
        nn.data = int(input("Enter the data to append: "))
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

    def addFirst(self, num=0):
        nn = Node()
        nn.data = int(input("Enter element to append at BEGIN: "))
        nn.next = self.head
        self.head = nn
        self.temp = self.head
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
    while(1):
        print("1. Add Node\n2. Add Node at First\n3. Delete Node\n4. Print List\n5. Length of List\n6. Exit")
        choice = int(input("\nEnter Choice :"))
    
        if choice == 1:
            obj.appendNode()
        elif choice == 2:
            obj.addFirst()
        elif choice == 3:
            obj.deleteNode()
        elif choice == 4:
            obj.printList()
        elif choice == 5:
            obj.lengthOfList()
        elif choice == 6:
            print("\nExited.")
            break
        else:
            print("Invalid choice. Please Enter Correct Choice.!")
        
