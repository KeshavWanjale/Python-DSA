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

def display_linked_list(head):
    if head == None:
        print("Linked list is empty")
    else:
        while head is not None:
            print(f"{head.data}",end="-> ")
            head = head.next
        print("None")

def delete_node(node):
    """
    Description:
        Deletes a node from a singly linked list given only access to that node.
        - This function copies the data from the next node to the current node, and then bypasses the next node by updating the current node's pointer.
        - It effectively removes the next node from the linked list by shifting its content to the current node.
        - This approach works only if the node to be deleted is not the last node in the list.
    Parameters:
        node (Node): The node in the linked list that needs to be deleted.
    Return:
        None: The function modifies the linked list in place and does not return anything.
    """
    node.data = node.next.data
    node.next = node.next.next

head = Node(100)
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500)
head.next.next.next.next.next = Node(600)

display_linked_list(head)

delete_node(head.next.next.next)

display_linked_list(head)