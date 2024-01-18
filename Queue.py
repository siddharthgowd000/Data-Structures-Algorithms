Q=[]
cap = 5
rear=0
front=0

def enqueueEle(num):
    global rear
    global Q
    if rear == cap:
        print("Queue is full.")
        return
    Q.append(num)
    rear = rear +1

def dequeue():
    global front
    global rear
    if front==rear:
        if(rear==cap):
            front=0
            rear=0
        print("Queue is empty")
        return
    print(f"{Q[front]} element is dequeued.")
    front = front+1
    # rear -= 1

def printList():
    global front, rear
    if front==rear:
        print("Queue is empty!")
        return
    for i in range(front, len(Q),1):  # print(Q[front:rear+1])
        print(Q[i], end=" ")
    print() # printing line after printing op

if __name__ == "__main__":
    enqueueEle(10)
    enqueueEle(20)
    enqueueEle(30)
    enqueueEle(40)
    enqueueEle(50)
    printList()
    dequeue()
    dequeue()
    printList()