class MinStack:
    """
    A class that implements a stack with a feature to retrieve the minimum element in constant time.
    Attributes:
        stack (list): A list to store stack elements.
        min_value (int): The current minimum value in the stack.
    """

    def __init__(self):
        """
        Initializes an empty MinStack.

        Parameters:
            None
        
        Returns:
            None
        """
        self.stack = []       
        self.min_value = float('inf')  

    def push(self, val):
        """
        Description:
            Pushes an element onto the stack.
        Parameters:
            val (int): The value to be pushed onto the stack.
        Returns:
            None
        """
        # Update the minimum value if the new value is less than the current min_value
        if val < self.min_value:
            self.min_value = val
        
        self.stack.append(val)

    def pop(self):
        """
        Description:
            Removes the top element from the stack.
        Parameters:
            None

        Returns:
            None
        """
        if not self.stack:
            return
        
        popped_value = self.stack.pop()
        
        # If the popped value was the minimum, recalculate the minimum
        if popped_value == self.min_value:
            if self.stack:  # If stack is not empty
                self.min_value = min(self.stack)  # Recalculate the minimum
            else:
                self.min_value = float('inf')  # Reset min_value to infinity if stack is empty

    def top(self):
        """
        Description:
            Gets the top element of the stack.
        Parameters:
            None
        Returns:
            int: The top element of the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if not self.stack:
            raise IndexError("Top from an empty stack")
        return self.stack[-1]

    def get_min(self):
        """
        Description:
            Retrieves the minimum element in the stack.
        Parameters:
            None
        Returns:
            int: The minimum element in the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        if not self.stack:
            raise IndexError("Get min from an empty stack")
        return self.min_value

if __name__ == "__main__":
    stack = MinStack()
    # print(stack.get_min()) 
    stack.push(100)
    stack.push(20)
    print(stack.get_min()) 
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(1)

    print(stack.get_min()) 
    stack.pop()
    print(stack.get_min()) 
    stack.pop()
    print(stack.get_min()) 
