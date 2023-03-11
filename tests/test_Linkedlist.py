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

    def test_get_data_by_id(self):
        ll2 = LinkedList()
        ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll2.insert_at_end('idusername')
        ll2.insert_at_end([1, 2, 3])
        ll2.insert_at_end({'id': 2, 'username': 'mosh_s'})
        lst2 = ll2.to_list()
        self.assertEqual(lst2, [{'id': 1, 'username': 'lazzy508509'}, 'idusername', [1, 2, 3],{'id': 2, 'username': 'mosh_s'}])
        user_data = ll2.get_data_by_id(2)
        # Данные не являются словарем или в словаре нет id.
        # Данные не являются словарем или в словаре нет id.
        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})
        # {'id': 2, 'username': 'mosh_s'}