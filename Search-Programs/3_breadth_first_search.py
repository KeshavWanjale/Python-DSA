from collections import deque


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

def bfs(root):
        """
        Description:
            Performs a breadth-first search (BFS) or level-order traversal on a tree. 
        Parameters:
            root: The root node of the binary tree.
        Returns:
            None
        """
        if root is None:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()  # Dequeue
            print(node.data, end=" ")  # Process the node
            
            # Enqueue left and right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)    



if __name__ == "__main__":

    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    bfs(tree.root)
