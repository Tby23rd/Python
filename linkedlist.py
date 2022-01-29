"""
linked list has a reference to head and tail.
nodes are self-referential objects
singly(point to front) and doubly(point to front and back) linked list
"""


class Node:
    """
    An object fro storing a single node for a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def ___repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        :return: the number of nodes in the list takes O(n) Time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new node containing data at the head of the list
        Takes O(1) time
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        :param key:
        :return: the node or None if not found
        Takes O(n) time(Linear Time)
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        """
        :return: a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)

"""
l = LinkedList()
N1 = Node(10)
l.head = N1
print(l.size())

l = LinkedList()
l.add(2)
print(l.size())
"""
l = LinkedList()
l.add(1)
l.add(10)
l.add(100)
n = l.search(10)
print(l)

