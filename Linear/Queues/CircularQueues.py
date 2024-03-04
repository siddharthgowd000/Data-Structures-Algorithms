class circularQueue:
    def __init__ (self,n):
        self.size = n
        self.q = [None]*n
        self.front = -1
        self.rear = -1
    
    def enqueue(self, n):        
        if self.rear == -1 and self.front == -1:
            self.front = self.rear = 0
            self.q[self.rear]= n
        elif self.front == (self.rear+1)%self.size:
            print("Queue is Full")
        else:
            self.rear = (self.rear+1)%self.size
            self.q[self.rear] = n
    
    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Empty!")
            return
        if self.front==self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.size
            self.q[self.front] = None
            
    def printQueue(self):
        for i in range(self.front,self.size):
            print(self.q[i],end =" ")
        for i in range(self.front):
            print(self.q[i], end =" ")

c = circularQueue(8)
for i in range(1,10):
    c.enqueue(i)
c.printQueue()
print("------------")
for i in range(6):   
    c.dequeue()

c.printQueue()
