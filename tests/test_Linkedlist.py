from linked_list import LinkedList
# from utils import Node
import unittest


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})

    def test_print_ll(self):
        lll = LinkedList()
        lll.insert_beginning({'id': 1})
        lll.insert_at_end({'id': 2})
        lll.insert_at_end({'id': 3})
        lll.insert_beginning({'id': 0})
        self.assertEqual(lll.print_ll(), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")