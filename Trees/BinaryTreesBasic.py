class TreeNode:
    def __init__ (self,val = 0):
        self.data = val
        self.left = None
        self.right = None
    
class BinaryTree:

    def search_node(self,root):
        node = TreeNode(root)
        if not node :
            print("root is not existed")
            return
        


    def insert_node(self, root, node, which_child):
        node = TreeNode(node)
        if not root:
