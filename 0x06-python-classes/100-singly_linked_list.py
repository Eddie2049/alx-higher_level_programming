#!/usr/bin/python3

"""Define singly-linked list class."""


class Node:
    """Repr. a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter of the next_node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Repr. a singly-linked list."""

    def __init__(self):
        """Initalize a SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert Node to the SinglyLinkedList.
        """
        n_node = Node(value)
        if self.__head is None:
            n_node.next_node = None
            self.__head = n_node
        elif self.__head.data > value:
            n_node.next_node = self.__head
            self.__head = n_node
        else:
            temp_ = self.__head
            while (temp_.next_node.data < value and
                    temp_.next_node is not None):
                temp_ = temp_.next_node
            n_node.next_node = temp_.next_node
            temp_.next_node = n_node

    def __str__(self):
        """print SinglyLinkedList."""
        vals = []
        temp_ = self.__head
        while temp_ is not None:
            vals.append(str(temp_.data))
            temp_ = temp_.next_node
        return ('\n'.join(vals))
