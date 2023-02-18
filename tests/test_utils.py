import unittest
from utils import *


class TestNode(unittest.TestCase):

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