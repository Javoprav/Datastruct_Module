from utils import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.nodelist = []

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

    def to_list(self):
        if self.head is None:
            print("Linkedlist пуст")
        else:
            current_node = self.head
            self.nodelist.append(current_node.data)
            while current_node.next_node is not None:
                current_node = current_node.next_node
                self.nodelist.append(current_node.data)
        return self.nodelist

    def get_data_by_id(self, id):
        try:
            for i in self.nodelist:
                if type(i) == dict and i['id'] == id:
                    return i
                else:
                    print('Данные не являются словарем или в словаре нет id')
                    continue
        except TypeError:
            return 'Данные не являются словарем или в словаре нет id'
