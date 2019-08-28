import unittest
from ma.stacks_queues.stack import Stack


class MyTestCase(unittest.TestCase):
    def test_is_empty(self):
        temp = Stack()
        self.assertTrue(temp.is_empty(), True)

    def test_push_item(self):
        temp = Stack()
        temp.push_item(123)
        self.assertFalse(temp.is_empty(), False)
        self.assertEqual(temp.top_item(), 123)

    def test_pop_item(self):
        temp = Stack()
        temp.push_item(123)
        temp.push_item(321)
        temp.pop_item()
        self.assertEqual(temp.top_item(), 123)

    def test_top_item(self):
        temp = Stack()
        temp.push_item(123)
        temp.push_item(321)
        self.assertEqual(temp.top_item(), 321)

    def test_stack_size(self):
        temp = Stack()
        temp.push_item(123)
        temp.push_item(321)
        self.assertEqual(temp.length(), 2)


if __name__ == '__main__':
    unittest.main()
