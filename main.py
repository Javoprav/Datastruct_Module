"""Импорты"""
from utils import *
from custom_queue import *
from linked_list import LinkedList

if __name__ == "__main__":
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2.next_node)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)
    print(stack.top.next_node.data)
    print(stack.top.next_node.next_node.data)
    print(stack.top.next_node.next_node.next_node)
    #print(stack.top.next_node.next_node.next_node.data)

    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стэк стал пустой
    print(stack.top)
    # None

    # pop() удаляет элемент и возвращает данные удаленного элемента
    print(data)
    # 'data1'

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    print(stack.top.data)
    # 'data1'

    # данные удаленного элемента
    print(data)
    # data2
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print(queue.head.data)
    print(queue.head.next_node.data)
    print(queue.tail.data)
    print(queue.tail.next_node)
    # print(queue.tail.next_node.data)

    # Результаты вывода в консоли
    # data1
    # data2
    # data3
    # None
    # AttributeError: 'NoneType' object has no attribute 'data'
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    print(queue.dequeue())
    # data1
    print(queue.dequeue())
    # data2
    print(queue.dequeue())
    # data3
    print(queue.dequeue())
    # None
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()
    # {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None