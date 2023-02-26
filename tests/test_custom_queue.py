import unittest
from custom_queue import *


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

class TestQueue(unittest.TestCase):

    def test_push(self):
        queue_1 = Queue()
        queue_1.enqueue('data1')
        queue_1.enqueue('data2')
        queue_1.enqueue('data3')

        self.assertEqual(queue_1.head.data, 'data1')
        self.assertEqual(queue_1.head.next_node.data, 'data2')
        self.assertEqual(queue_1.tail.data, 'data3')