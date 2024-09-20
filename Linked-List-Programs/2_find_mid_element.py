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

def find_middle(head):
    """
    Description:
        Finds the middle node of a singly linked list using the two-pointer (slow and fast) technique.
        - The slow pointer moves one step at a time.
        - The fast pointer moves two steps at a time.
        - When the fast pointer reaches the end, the slow pointer will be at the middle node.
    Parameters:
        head (Node): The head node of the linked list.
    Return:
        Node.data: Returns the data of the middle node. If the list is empty, returns None.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

if __name__ == "__main__":
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    head.next.next.next = Node(400)
    head.next.next.next.next = Node(500)
    # head.next.next.next.next.next = Node(600)

    print(find_middle(head))