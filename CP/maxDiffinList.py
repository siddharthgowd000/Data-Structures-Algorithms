class Node:
    def __init__ (self):
        self.data = 0
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.head = None
        self.temp = None
        self.__length = 0
    
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

    def printList(self):
        if self.__length == 0:
            print("List is Empty")
            return
        self.temp = self.head
        while self.temp != None:
            print(self.temp.data, end="->")
            self.temp = self.temp.next
        print()


    def sortLinkedList(self):
        slow = self.head
        for i in range(self.__length):
            fast = slow.next
            while(fast):
                if slow.data > fast.data:
                    slow.data, fast.data = fast.data, slow.data
                fast = fast.next
            slow = slow.next
        return self.head
    
    def maxDiff(self):
        current = self.head
        nextt1 = self.head.next
        summ = 0
        maxx = 0
        for i in range(self.__length):
            summ = current.data + nextt1.data
            if summ > maxx:
                maxx = summ
            summ = 0
            current = current.next
        return maxx

            
if __name__ == "__main__":

    inp = input().split(" ")
    list1 = [int(i) for i in inp[2] if i.isdigit()]

    obj = Linkedlist()
    
    for i in list1:
        obj.appendNode(i)

    obj.sortLinkedList()
    obj.printList()
    maxx = obj.maxDiff()
    print(maxx)
    
        

