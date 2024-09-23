class Queue:
    """
    Description:
        A class that implements a basic queue using a list.
    Attributes:
        items (list): A list to store the elements of the queue.
    """

    def __init__(self):
        """
        Description:
            Initializes an empty queue.
        Parameters:
            None
        Returns:
            None
        """
        self.items = []

    def enqueue(self, item):
        """
        Description:
            Adds an item to the back of the queue.
        Parameters:
            item (any): The element to be added to the queue.
        Returns:
            None
        """
        self.items.append(item)

    def dequeue(self):
        """
        Description:
            Removes and returns the front item from the queue.
        Parameters:
            None
        Returns:
            any: The front element of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Description:
            Returns the front item of the queue without removing it.
        Parameters:
            None
        Returns:
            any: The front element of the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def is_empty(self):
        """
        Description:
            Checks if the queue is empty.
        Parameters:
            None
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Description:
            Returns the number of elements in the queue.
        Parameters:
            None
        Returns:
            int: The number of elements in the queue.
        """
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print("Front element:", queue.peek())  
    print("Dequeue:", queue.dequeue())      
    print("Front element after dequeue:", queue.peek())  
    print("Size of queue:", queue.size())  
