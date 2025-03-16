class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data  
        self.left = left  
        self.right = right  

class BinaryTree:
    def __init__(self, root=None):
        self.root = root  
    
    def print_tree(self):
        """Prints the tree structure in pre-order traversal (root, left, right)."""
        if self.root is None:
            print("The tree is empty.") 
        else:
            self._pre_order(self.root)
    
    def _pre_order(self, node):
        """Helper method for pre-order traversal."""
        if node is not None:
            print(node.data, end=" ")  
            self._pre_order(node.left)  
            self._pre_order(node.right)  

node_7 = Node(7)
node_6 = Node(6)
node_5 = Node(5)
node_4 = Node(4)
node_3 = Node(3, node_6, node_7)
node_2 = Node(2, node_4, node_5)
root = Node(1, node_2, node_3)


binary_tree = BinaryTree(root)


print("Binary Tree (Pre-order Traversal):")
binary_tree.print_tree()

empty_tree = BinaryTree()

print("\nTesting with an empty tree:")
empty_tree.print_tree()
