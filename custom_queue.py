class Node:
    """класс узла"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Добавление элемента """
        new_node = Node(data)
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
           self.tail.next_node = new_node
           self.tail = new_node
        

