# TODO: Basic implementation of a linked list and common operations.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.next(self.head)
        self.head = temp
