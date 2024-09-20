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

def is_cycle_prsent(head):
    """
    Description:
        Detects if there is a cycle (loop) in a singly linked list using the Floyd's Cycle Detection Algorithm (also known as the Tortoise and Hare Algorithm).
        - The slow pointer moves one step at a time.
        - The fast pointer moves two steps at a time.
        - If the slow pointer and fast pointer meet at some point, it indicates the presence of a cycle.
    Parameters:
        head (Node): The head node of the linked list.
    Return:
        bool: Returns True if a cycle is detected in the linked list, otherwise False.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            return True
    return False

def is_cycle_present_using_dict(head):
    """
    Description:
        Detects if there is a cycle (loop) in a singly linked list by using a dictionary (or set) to track visited nodes.
        - The function traverses the linked list and stores each node in a dictionary.
        - If a node is encountered that has already been seen, it indicates the presence of a cycle.
    Parameters:
        head (Node): The head node of the linked list.
    Return:
        bool: Returns True if a cycle is detected in the linked list, otherwise False.
    """
    visited_nodes = {}
    current = head
    while current:
        if current in visited_nodes:
            return True
        visited_nodes[current] = True  # Mark the node as visited
        current = current.next
    return False

if __name__ == "__main__":
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    head.next.next.next = Node(400)
    head.next.next.next.next = Node(500)
    head.next.next.next.next.next = Node(600)
    
    print(is_cycle_prsent(head))

    head.next.next.next = head
    print(is_cycle_prsent(head))
    