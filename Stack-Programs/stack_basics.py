class Stack:
    """
    Description:
        A class to represent a Stack (LIFO) data structure.
    Attributes:
        items (list): A list to store stack elements.
    """

    def __init__(self):
        """
        Description:
            Initializes the stack as an empty list.
        Parameters:
            None
        Returns:
            None
        """
        self.items = []

    def is_empty(self):
        """
        Description:
            Checks if the stack is empty.
        Parameters:
            None
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Description:
            Adds an item to the top of the stack. 
        Parameters:
            item (any): The element to be added to the stack.
        Returns:
            None
        """
        self.items.append(item)

    def pop(self):
        """
        Description:
            Removes and returns the top item from the stack. 
        Parameters:
            None
        Returns:
            any: The top element from the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """
        Description:
            Returns the top item of the stack without removing it.
        Parameters:
            None
        Returns:
            any: The top element from the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        """
        Description:
            Returns the current size of the stack.   
        Parameters:
            None   
        Returns:
            int: The number of elements in the stack.
        """
        return len(self.items)

    def display(self):
        """
        Description:
            Displays all elements in the stack from top to bottom.
        Parameters:
            None
        Returns:
            None
        """
        print("Stack :", self.items[::-1])


if __name__ == "__main__":

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()  

    # Peek the top element
    print("Top element:", stack.peek())  

    # Pop the top element
    stack.pop()  
    stack.display()  

    # Check if the stack is empty
    print("Is the stack empty?", stack.is_empty())  

    # Get the size of the stack
    print("Stack size:", stack.size())  