class Employee:
    def __init__ (self, firstName, lastName, contact, age, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.contact = contact
        self.age = age
        self.salary = salary
        self.next = None

class EmployeeLinkedlist:
    def __init__ (self):
        self.head = None
        self.temp = None
        self.__length=0
    
    def addEmployee(self, firstName, lastName, contact, age, salary):
        ne = Employee(firstName, lastName, contact, age, salary)

        #self.temp = self.head
        if self.head == None:
            #list is empty
            self.head = ne
            self.temp = ne
            self.__length += 1

        else:
            #list is present
            self.temp = self.head
            while self.temp.next != None:
                self.temp = self.temp.next
            self.temp.next = ne
            self.__length += 1


    def deleteEmployee(self):
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

    

    def printEmployeeList(self):
        if self.__length == 0:
            print("List is Empty")
            return
        self.temp = self.head
        while self.temp != None:
            print(self.temp.firstName,self.temp.contact, end="->")
            self.temp = self.temp.next
        print()

    def numberOfEmployee(self):
        print("No. of Employee is: ", self.__length)

    def sortEmployee(self):
        slow = self.head
        for i in range(self.__length):
            fast = slow.next
            while(fast):
                
                slowOrd = sum(ord(i) for i in slow.firstName + str(slow.contact))
                fastOrd = sum(ord(i) for i in fast.firstName + str(fast.contact))

                if slowOrd > fastOrd:
                    
                    slow.firstName , fast.firstName = fast.firstName, slow.firstName
                    slow.lastName, fast.lastName = fast.lastName, slow.lastName
                    slow.contact, fast.contact = fast.contact, slow.contact
                    slow.age , fast.age = fast.age ,slow.age
                    slow.salary, fast.salary = fast.salary, slow.salary 
                fast = fast.next
            slow = slow.next
        return self.head

            
if __name__ == "__main__":
    obj = EmployeeLinkedlist()
    while(1):
        print("1. Add Employee\n2. Delete Emplloyee\n3. Print Employee List\n4. Number of Employee\n5. Sort A-Z Employee\n6. Exit")
        choice = int(input("\nEnter Choice :"))
    
        if choice == 1:
            firstName = input("\nEnter the Employee name: ")
            lastName = input("\nEnter the last name: ")
            contact = int(input("\nEnter the Contact number: "))
            age = int(input("\nEnter the age: "))
            salary = int(input("\nEnter the salary: "))
            obj.addEmployee(firstName, lastName,contact,age,salary)
        elif choice == 2:
            obj.deleteEmployee()
        elif choice == 3:
            obj.printEmployeeList()
        elif choice == 4:
            obj.numberOfEmployee()
        elif choice == 5:
            obj.sortEmployee()
        elif choice == 6:
            print("\nExited.")
            break
        else:
            print("Invalid choice. Please Enter Correct Choice.!")
        
