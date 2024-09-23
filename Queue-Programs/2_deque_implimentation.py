class Deque:
    """
    Description:
        A class to represent a deque (double-ended queue) using a Python list.
    Attributes:
        deque (list): A list to store the elements of the deque.
    """
    
    def __init__(self):
        """
        Description:
            Initialize an empty deque.
        """
        self.deque = []
    
    def append(self, value):
        """
        Description:
            Add an element to the rear (right end) of the deque.
        Parameters:
            value: The element to be added to the rear of the deque.
        """
        self.deque.append(value)
    
    def appendleft(self, value):
        """
        Description:
            Add an element to the front (left end) of the deque.
        Parameters:
            value: The element to be added to the front of the deque.
        """
        self.deque.insert(0, value)  # Insert at the front of the list
    
    def pop(self):
        """
        Description:
            Remove and return the element from the rear (right end) of the deque.
        Returns:
            The element removed from the rear of the deque.
        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        return self.deque.pop()  # Remove from the rear
    
    def popleft(self):
        """
        Description:
            Remove and return the element from the front (left end) of the deque.
        Returns:
            The element removed from the front of the deque.
        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("popleft from an empty deque")
        return self.deque.pop(0)  # Remove from the front
    
    def is_empty(self):
        """
        Description:
            Check if the deque is empty.
        Returns:
            True if the deque is empty, False otherwise.
        """
        return len(self.deque) == 0
    
    def size(self):
        """
        Description:
            Get the number of elements in the deque.
        Returns:
            The number of elements in the deque.
        """
        return len(self.deque)
    
    def peek_front(self):
        """
        Description:
            Peek at the element at the front of the deque without removing it.
        Returns:
            The element at the front of the deque.
        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.deque[0]
    
    def peek_rear(self):
        """
        Description:
            Peek at the element at the rear of the deque without removing it.
        Returns:
            The element at the rear of the deque.
        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.deque[-1]
    

if __name__ == "__main__":
    dq = Deque()

    # Add elements to the deque
    dq.append(10)
    dq.appendleft(20)
    dq.append(30)

    # Check the elements in the deque
    print("Deque after append operations:", dq.deque)  

    # Remove elements from the deque
    dq.popleft()  # Remove from the front
    print("Deque after popleft:", dq.deque) 

    dq.pop()  # Remove from the rear
    print("Deque after pop:", dq.deque) 

    # Peek front and rear
    print("Front element:", dq.peek_front()) 
    dq.append(40)
    print("Rear element:", dq.peek_rear())   

    # Check if deque is empty
    print("Is deque empty?", dq.is_empty())  

    # Size of the deque
    print("Size of deque:", dq.size())  
