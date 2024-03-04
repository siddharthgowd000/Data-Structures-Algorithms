class BinaryTree:
    def __init__ (self, val=0):
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
        if self.root is None or self.root == 0:
            print("Empty")
            return
        if num < self.root:
            if self.left:
                self.left = self.left.delete(num)
            else:
                print("Not found")
        elif num > self.root:
            if self.right:
                self.right = self.right.delete(num)
            else:
                print("Not found")
        
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.root = node.root
            self.right = self.right.delete(node.num)
        return self


                
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.root)
        if self.right:
            self.right.Inorder()
        
   

def countNodes(root):
    if root is None:
        return 0
    return 1+countNodes(root.left)+countNodes(root.right)

l = [2,3,4,5]
bt = BinaryTree()
for i in l:
    bt.insert(i)

bt.Inorder()
if countNodes(bt) > 1:
    bt.delete(1)
else:
    print("Cannot be deleted")
print("After deleted")
bt.Inorder()
print()
print(countNodes(bt))
