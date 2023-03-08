from utils import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, value) -> None:
        new_node = Node(value)
        new_node.data = value
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        new_node.data = value
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
