class Node:
    def _init_(self):
        self.id=None
        self.firstname=None
        self.secondname=None
        self.phone=None
        self.next=None

class LinkedList:
    def _init_(self):
        self.head=None
        self.temp=None
    def appendNode(self):
        newnode=Node()
        newnode.id=int(input("enter emp id"))
        newnode.firstname=input("Enter first name: ")
        newnode.secondname=input("Enter second name: ")
        newnode.phone=int(input("Enter phone num: "))
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next
    
    
    def sortlistbyname(self):
        if self.head == None or self.head.next == None:
            self.displayLst()
            return
        sorted_head=self.head
        tempval=Node()
        slow=self.head
        fast= slow.next

        while slow:
            fast=slow.next
            while fast:
                if fast.firstname<slow.firstname:
                    tempval.id=slow.id
                    tempval.firstname=slow.firstname
                    tempval.secondname=slow.secondname
                    tempval.phone=slow.phone
                    slow.id=fast.id
                    slow.firstname=fast.firstname
                    slow.secondname=fast.secondname
                    slow.phone=fast.phone
                    fast.id=tempval.id
                    fast.firstname=tempval.firstname
                    fast.secondname=tempval.secondname
                    fast.phone=tempval.phone
                    fast=fast.next
                else:
                    fast=fast.next
            slow=slow.next

        self.head = sorted_head
        self.displayLst()
    
    
    def sortlistbynum(self):
        if self.head == None or self.head.next == None:
            self.displayLst()
            return

        sorted_head=self.head
        tempval=Node()
        slow=self.head
        fast= slow.next

        while slow:
            fast=slow.next
            while fast:
                if fast.phone<slow.phone:
                    tempval.id=slow.id
                    tempval.firstname=slow.firstname
                    tempval.secondname=slow.secondname
                    tempval.phone=slow.phone
                    slow.id=fast.id
                    slow.firstname=fast.firstname
                    slow.secondname=fast.secondname
                    slow.phone=fast.phone
                    fast.id=tempval.id
                    fast.firstname=tempval.firstname
                    fast.secondname=tempval.secondname
                    fast.phone=tempval.phone
                    fast=fast.next
                else:
                    fast=fast.next
            slow=slow.next

        self.head = sorted_head
        self.displayLst()
    

    def displayLst(self):
        sno=0
        if self.head==None:
            print("list is empty")
        else:
            self.temp=self.head
            while self.temp is not None:
                sno+=1
                print("S.No:",sno,"id:",self.temp.id,"first name",self.temp.firstname,"second name:",self.temp.secondname,"phone no:",self.temp.phone)
                self.temp=self.temp.next 

LLObj=LinkedList()
while True:

    LLObj.appendNode()
    n=int(input("enter choice (0/1)"))
    if n==0:
        break
print("before sorting")
LLObj.displayLst()
print("after sorting by name")
LLObj.sortlistbyname()
print("after sorting by number")
LLObj.sortlistbynum()