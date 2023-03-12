class Node:
    """класс узла"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс стек"""

    def __init__(self):
        self.top = None

    def push(self, data):
        """Добавление элемента """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """Удаление элемента """
        remove = self.top
        self.top = self.top.next_node
        return remove.data
