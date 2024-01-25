class BinaryTree:
    def __init__ (self,val=0):
        self.root = val
        self.left = None
        self.right = None
    
    def insert(self, val):

        if self.root == None:
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
    
    def search(self, num):
        if self.root == num:
            print("Number Found")
            return
        if num < self.root:
            if self.left is None:
                print("Not Found")
            else:
                self.left.search(num)
        elif num > self.root:
            if  self.right is None:
                print("Not found")
            else:
                self.right.search(num)


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)

    bt.search(6)