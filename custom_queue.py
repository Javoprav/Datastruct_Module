class Node:
    """класс узла"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node