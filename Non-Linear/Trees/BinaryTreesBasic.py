
class BinarySearchTree:
    def __init__ (self,val = 0):
        self.root = val
        self.left = None
        self.right = None

    def insert_node(self, val):
        if self.root == None:
            self.root = val
        elif val < self.root:
            if self.left == None:
                self.left = BinarySearchTree(val)
            else:
                self.left.insert_node(val)
        elif val >= self.root:
            if self.right == None:
                self.right = BinarySearchTree(val)
            else:
                self.right.insert_node(val)
    
    def inorder(self):
        if self.left: 
            self.left.inorder()
        print(self.root, end=" ")
        if self.right:
            self.right.inorder()
    
    def search(self,parent,current,val):
        if not current:
            return parent
        if val < current.root:
            parent = current
            self.search(parent,current.left,val)
        elif val > current.root:
            parent = current
            self.search(parent, current.right, val)

        

    def delete(self, root, val):
        parent = None
        curr = root
        parent,curr = self.search_node_with_parent(curr, parent,val)
        if(curr.left==None and curr.right==None):
            if curr==root:
                root=None
            else:
                if parent.left==curr:
                    parent.left = None
                else:
                    parent.right = None
            del curr
            return
        elif curr.left is not None and curr.right is not None:
            successor = self.findMin(curr.right).val

            self.delete(root,successor)
            curr.val = successor
            
        else:
            if curr.left is None:
                if parent.left==curr:
                    parent.left = curr.right
                else:
                    parent.right = curr.right
                del curr

            else:
                if parent.left == curr:
                    parent.left = curr.left
                else:
                    parent.right = curr.left
                del curr

    
bt = BinarySearchTree(10)
root = bt.root
bt.insert_node(8)
bt.insert_node(7)
bt.inorder()
bt.delete_node(root,7)