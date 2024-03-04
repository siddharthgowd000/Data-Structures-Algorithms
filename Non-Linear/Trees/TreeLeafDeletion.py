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


    def delete(self, num):
        
        leaf = self.root
        if self.left is not None:
            if num == self.left.root:
                if self.left.left is None and self.left.right is None:
                    self.left = None
                    print("Deleted.")
                    return
                else:
                    print("Cannot be deleted.")
                    return
        if self.right is not None:
            if num == self.right.root:
                if self.right.left is None and self.right.right is None:
                    self.right = None
                    print("Deleted.")
                    return
                else:
                    print("Cannot be deleted.")
                    return

        if num <  self.root:
            if self.left is not None:
                self.left.delete(num)
        elif num > self.root:
            if self.right is not None:
                self.right.delete(num)
        '''
        slow = self
        fast = slow.left

        while(fast.left):
            slow = slow.left
            fast = fast.left
        print(f"{slow.root} , {fast.root}")
        slow.left = None
            '''

                
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.root)
        if self.right:
            self.right.Inorder()
            
    
    def search(self, num):
        if self.root == num:
            print("Number Found")
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
    bt = BinaryTree(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)

    bt.search(3)
    bt.search(4)
    bt.Inorder()
    bt.delete(3)
    bt.delete(4)
    bt.Inorder()
    bt.search(4)