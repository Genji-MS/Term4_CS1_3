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
        if self.length == 0:
            return True
        if self.list.head is None:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        # √: Count number of items
        length = 0
        currentNode = self.list.head
        while currentNode != None:
            length +=1
            currentNode = currentNode.next
        return length

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [√]
        We only reassign the head to point to the new head, and update 'head' to our current item. No itteration
        """
        # √: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # √: Return top item, if any
        if (self.is_empty()):
            return None
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – Why? [√]
        LinkedLists store data anywhere, no need to move anything around, Just update the head to the head.next. No itteration
        """
        # √: Remove and return top item, if any
        value = self.peek()
        if (value == None):
            raise ValueError('Item not found')
        else:
            self.list.delete(value)
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
        # √: Insert given item
        for i in range(-1+1,0,-1):
            self.list[i] = self.list[i-1]
        self.list[0]= item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # √: Return top item, if any
        if self.length >0:
            return self.list[0]
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # √: Remove and return top item, if any
        if self.length == 0:
            raise ValueError('Empty Stack')
        item = self.list[0]
        for i in range(0,self.length-2):
            self.list[i] = self.list[i+1]
        self.list[-1] = None
        return item

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack

if __name__ == "__main__":
    stack = LinkedStack([1,2,3,4])
    stack.peek()