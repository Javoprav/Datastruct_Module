import unittest
from custom_queue import *


class TestQueue(unittest.TestCase):

    def test_push(self):
        queue_1 = Queue()
        queue_1.enqueue('data1')
        queue_1.enqueue('data2')
        queue_1.enqueue('data3')

        self.assertEqual(queue_1.head.data, 'data1')
        self.assertEqual(queue_1.head.next_node.data, 'data2')
        self.assertEqual(queue_1.tail.data, 'data3')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data4')
        self.assertEqual(queue.dequeue(), 'data4')