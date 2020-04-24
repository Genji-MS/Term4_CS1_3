#!python

from linkedlist import LinkedList

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # √: Check if empty
        if self.head is None:
            return True

    def length(self):
        """Return the number of items in this stack."""
        # √: Count number of items
        length = 0
        currentNode = self.head
        while currentNode != None:
            length +=1
            currentNode = currentNode.next

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [√]
        We only reassign the head to point to the new head, and update 'head' to our current item. No itteration
        """
        # √: Push given item
        new_node = item
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # √: Return top item, if any
        if (self.is_empty == True):
            return None
        return self.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – Why? [√]
        LinkedLists store data anywhere, no need to move anything around, Just update the head to the head.next. No itteration
        """
        # √: Remove and return top item, if any
        value = self.peek
        if (self.peek == None):
            raise ValueError('Item not found')
        else:
            self.head = self.head.next
            return value


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # √: Check if empty
        if len(self) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        # √: Count number of items
        length = 0
        if (self.is_empty() == True):
            return length
        for item in self.list:
            length += 1
        return length

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(n) – Why? [√]
        list is lined up in memory, adding a new item at the head requires every item to be shifted by 1
        """
        # TODO: Insert given item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack

if __name__ == "__main__":
    stack = LinkedStack([1,2,3,4])
    stack.peek()