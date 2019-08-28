import unittest
from ma.linked_lists.linkedList import LinkedList


class MyTestCase(unittest.TestCase):

    def test_is_empty(self):
        temp = LinkedList()
        self.assertTrue(temp.is_empty(), True)

    def test_add_item(self):
        temp = LinkedList()
        temp.add(123)
        self.assertFalse(temp.is_empty(), False)

    def test_find_item(self):
        temp = LinkedList()
        temp.add(123)
        self.assertTrue(temp.search(123), True)

    def test_delete_item(self):
        temp = LinkedList()
        temp.add(123)
        temp.add(321)
        temp.delete(123)
        self.assertFalse(temp.search(123), False)

    def test_list_length(self):
        temp = LinkedList()
        temp.add(1)
        temp.add(2)
        self.assertEqual(temp.length(), 2)


if __name__ == '__main__':
    unittest.main()
