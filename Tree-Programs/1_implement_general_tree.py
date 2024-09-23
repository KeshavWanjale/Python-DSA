class TreeNode:
    """
    Description:
        Represents a node in a general tree structure.
    Attributes:
        data : any
            The value or data stored in the node.
        children : list
            A list of child nodes that are connected to this node.
    Methods:
        add_child(child_node):
            Adds a child node to this node.
        remove_child(child_node):
            Removes a specified child node from this node.
        display(level=0):
            Recursively prints the tree structure starting from this node.
    """
    
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        """
        Description:
            Adds a child node to this node.
        """
        self.children.append(child_node)

    def remove_child(self, child_node):
        """
        Description:
            Removes a specified child node from this node.
        """
        self.children = [child for child in self.children if child != child_node]

    def display(self, level=0):
        """
        Description:
            Displays the tree structure from this node with proper indentation based on the level.
        """
        print(' ' * level * 4 + str(self.data))
        for child in self.children:
            child.display(level + 1)


class GeneralTree:
    """
    Description:
        Represents a general tree structure.
    Attributes:
        root : TreeNode  The root node of the tree.
    Methods:
        traverse(node):
            Performs a preorder traversal starting from the given node.
    """
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def traverse(self, node):
        """
        Description:
            Traverses the tree in preorder: Root -> Children.
        """
        if node:
            print(node.data, end=" ")
            for child in node.children:
                self.traverse(child)


if __name__ == "__main__":

    # Create the general tree with a root node
    tree = GeneralTree("Root")

    # Add children to the root node
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    tree.root.add_child(child1)
    tree.root.add_child(child2)

    # Add children to Child1
    grandchild1 = TreeNode("Grandchild1")
    grandchild2 = TreeNode("Grandchild2")
    child1.add_child(grandchild1)
    child1.add_child(grandchild2)

    # Add children to Child2
    grandchild3 = TreeNode("Grandchild3")
    child2.add_child(grandchild3)

    # Display the tree structure
    print("Tree structure:")
    tree.root.display()

    # Traverse the tree (Preorder traversal)
    print("\nTree traversal (Preorder):")
    tree.traverse(tree.root)
