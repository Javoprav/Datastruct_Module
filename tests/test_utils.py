import unittest
from utils import *


class TestNode(unittest.TestCase):

    def setUp(self) -> None:
        self.node_10 = Node(10)

    def test_node_init(self):
        assert self.node_10.data == 10
        self.node_10 = Node(100)
        assert self.node_10.next_node is None

    def test_node_next_node(self):
        node2 = Node(220, self.node_10)
        assert node2.next_node is self.node_10

    def test_push(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(stack.top.data, 'data3')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        print(stack.top)
        print(data)
        self.assertEqual(stack.top, None)
        self.assertEqual(data, 'data1')

