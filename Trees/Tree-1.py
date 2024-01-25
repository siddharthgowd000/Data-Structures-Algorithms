class BinaryTree:
    def __init__(self, val=0):
        self.root = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.root == 0:
            self.root = val
        elif val < self.root:
            if self.left is None:
                self.left = BinaryTree(val)
            else:
                self.left.insert(val)
        elif val > self.root:
            if self.right is None:
                self.right = BinaryTree(val)
            else:
                self.right.insert(val)

    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.root)
        if self.right:
            self.right.Inorder()
            
    def preoder(self):
      print(self.root)
      if self.left:
        self.left.preoder()
      if self.right:
        self.right.preoder()
        
    def postoder(self):
      if self.left:
        self.left.postoder()
      if self.right:
        self.right.postoder()
      print(self.root)

      
    def search(self, data, count=0):
        count += 1  

        if self.root == data:
            print("Data found count=", count)
        elif data < self.root:
            if self.left is not None:
                self.left.search(data, count)
            else:
                print("Data not found")
        elif data > self.root:
            if self.right is not None:
                self.right.search(data, count)
            else:
                print("Data not found")
    


bt = BinaryTree(10)
bt.insert(7)
bt.insert(5)
bt.insert(15)
bt.insert(25)
bt.insert(20)


# print()
# print("preoder")
# bt.preoder()

# print()
# print("Inorder")
# bt.Inorder()

# print()
# print("postoder")
# bt.postoder()


bt.search(5)