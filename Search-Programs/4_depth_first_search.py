class Node:
    """
    Description:
        Represents a node in a binary tree.
    Parameters:
        data: The value stored in the node.
    Attributes:
        data: The value stored in the node.
        left: Reference to the left child node (initially None).
        right: Reference to the right child node (initially None).
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Description:
        Represents a binary tree with methods for tree traversal.
    Attributes:
        root: The root node of the binary tree (initially None).
    Methods:
        preorder(node):
            Performs a preorder traversal (Root -> Left -> Right).
        inorder(node):
            Performs an inorder traversal (Left -> Root -> Right).
        postorder(node):
            Performs a postorder traversal (Left -> Right -> Root).
    """

    def __init__(self):
        self.root = None

    def preorder(self, node):
        """
        Description:
            Performs a preorder traversal of the binary tree (Root -> Left -> Right).
        Parameters:
            node: The current node in the traversal process.
        Returns:
            None
        """
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        """
        Description:
            Performs an inorder traversal of the binary tree (Left -> Root -> Right).
        Parameters:
            node: The current node in the traversal process.
        Returns:
            None
        """
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        """
        Description:
            Performs a postorder traversal of the binary tree (Left -> Right -> Root).
        Parameters:
            node: The current node in the traversal process.
        Returns:
            None
        """
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')


if __name__ == "__main__" :
    
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Preorder traversal:")
    tree.preorder(tree.root)

    print("\nInorder traversal:")
    tree.inorder(tree.root)

    print("\nPostorder traversal:")
    tree.postorder(tree.root)
