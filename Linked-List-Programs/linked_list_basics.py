class Node:
    def __init__(self, data) :
        """
        Description:
            Represents a node in a linked list, holding data and a reference to the next node.
        Parameters:
            data (any): The data to be stored in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    Description:
        Implements a singly linked list with various methods to manipulate the list.
    """
    def __init__(self):
        """
        Description:
            Initializes an empty linked list with a head pointer set to None.
        """
        self.head = None

    def length(self):
        """
            Description:
                returns the length of a linkedlist
            Parameters:
                None
            Returns:
                length of the linked list
        """
        len = 1
        if self.head == None :
            return 0
        else :
            current = self.head
            while current.next is not None:
                len +=1
                current = current.next
        
        return len
    
    def append(self, data):
        """
        Description:
            Adds a new node with the given data at the end of the linked list.
        Parameters:
            data (any): The data to be added to the new node.
        """
        new_node = Node(data)
        if self.head is None:  # Handle the case when the list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:  
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """
        Description:
            Adds a new node with the given data at the beginning of the linked list.
        Parameters:
            data (any): The data to be added to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, index):
        """
        Description:
            Inserts a new node with the given data at the specified index in the linked list.
        Parameters:
            data (any): The data to be added to the new node.
            index (int): The position to insert the new node (1-based index).
        """
        if index == 1:  # Handle insertion at the start
            self.prepend(data)
            return
        new_node = Node(data)
        temp_head = self.head
        for i in range(1, index - 1):  # Loop until the node before the insertion point
            if temp_head is None:  # Handle invalid index case
                print("Index out of bounds")
                return
            temp_head = temp_head.next
        
        new_node.next = temp_head.next
        temp_head.next = new_node

    def display(self):
        """
        Description:
            Prints the data of each node in the linked list, from the head to the end.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicates the end of the list

    def delete_start(self):
        """
        Description:
            Deletes the first node (head node) of the linked list.
        """
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return
        self.head = self.head.next  # Move the head to the next node

    def delete_end(self):
        """
        Description:
            Deletes the last node of the linked list.
        """
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return
        if self.head.next is None:  # Handle the case with only one node
            self.head = None
            return
        prev = self.head
        temp_head = self.head.next

        while temp_head.next is not None:
            temp_head = temp_head.next
            prev = prev.next
        prev.next = None

    def delete_at_index(self, index):
        """
        Description:
            Deletes the node at the specified index in the linked list.
        Parameters:
            index (int): The position of the node to be deleted (1-based index).
        """
        if self.head is None:
            print("The list is empty, nothing to delete.")
            return
        if index == 1:  # Handle deletion of the head node
            self.delete_start()
            return
        prev = self.head
        temp_head = self.head.next

        for i in range(1, index-1):
            temp_head = temp_head.next
            prev = prev.next
        
        prev.next = temp_head.next
        temp_head = None



def display_linked_list(head):
    if head == None:
        print("Linked list is empty")
    else:
        while head is not None:
            print(f"{head.data}",end="-> ")
            head = head.next
        print("None")

def length_linked_list(head):
    if head == None:
        print("Linked list is empty")
        return
    else:
        len = 0
        while head is not None:
            len += 1
            head = head.next
        return len
            
if __name__ == "__main__":
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    head.next.next.next = Node(400)
    head.next.next.next.next = Node(500)
    head.next.next.next.next.next = Node(600)

    display_linked_list(head)
    print(length_linked_list(head))

    # using Linkd list class
    linked_list = LinkedList()

    n1 = Node(0)
    linked_list.head = n1
    n2 = Node(1)
    n1.next = n2

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(40)

    linked_list.display()

    linked_list.prepend(-1)
    linked_list.display()

    linked_list.insert("S5",8)
    linked_list.display()

    linked_list.delete_start()
    linked_list.display()

    linked_list.delete_end()
    linked_list.display()

    linked_list.delete_at_index(7)
    linked_list.display()