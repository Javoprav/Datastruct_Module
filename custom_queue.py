from utils import *


class Queue:
    def __init__(self, head=None, tail=None):
        self.__head = head
        self.__tail = tail

    def enqueue(self, value) -> None:
        new_node = Node(data=value)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next_node = new_node
            self.__tail = new_node

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail