"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        new_node = ListNode(value, None, None)

        if not self.head:

            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:

            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
      
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):

        if self.length == 0:

            return None
        
        if self.length == 1:

            value = self.head.value 
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        
        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):

        new_node = ListNode(value, None, None)

        if self.length == 0:

            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        
        if self.length == 0:

            return None
        
        if self.length == 1:

            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        
        value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):

        if self.node_in_dll(node):

            if self.length < 2:

                pass

            else:

                if self.head == node:

                    pass

                else:

                    if self.tail == node:

                        self.add_to_head(self.remove_from_tail())

                    else: 

                        self.add_to_head(node.value)
                        node.delete()
                        self.length -= 1


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        
        if self.node_in_dll(node):

            if self.length < 2:

                pass

            else:

                if self.tail == node:

                    pass

                else:

                    if self.head == node:

                        self.add_to_tail(self.remove_from_head())

                    else:

                        node.delete()
                        self.add_to_tail(node.value)
                        self.length -= 1

    """check if the given node is in the dll, returns True if yes,
    returns False if not """
    def node_in_dll(self, node):

        current = self.head

        while current:

            if current == node:

                return True

            current = current.next

        return False

    """Removes a node from the list and 
    handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        
        if self.node_in_dll(node):

            if self.length == 1:

                self.head = None    
                self.tail = None
                self.length -= 1
        
            else:

                if self.head == node:

                    self.remove_from_head()

                elif self.tail == node:

                    self.remove_from_tail()

                else:

                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):

        if self.length > 0:

            values = []

            current = self.head

            while current:

                values.append(current.value)

                current = current.next

            return max(values)

        return None

