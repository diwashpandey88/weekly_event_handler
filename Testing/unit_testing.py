import unittest
from classes.clsevent import Event
from classes.todo import Tododbsunday

class MyTest(unittest.TestCase):
    evnt = Event()
    sun = Tododbsunday()

    def test_add_item(self):
        result = self.evnt.add_item('sunday', 'online class')
        self.assertTrue(result)

    def test_delete(self):
        result = self.evnt.deleter(74,)
        self.assertTrue(result)

    def test_add_item1(self):
        result = self.evnt.add_item('', '')
        self.assertFalse(result)

    def test_add_item2(self):
        result = self.evnt.add_item('Sunday', '')
        self.assertFalse(result)

    def test_add_item3(self):
        result = self.evnt.add_item('hello', '')
        self.assertFalse(result)


    def test_search_item(self):
        data = self.evnt.search_item('Friday')
        actual_result = len(data)
        expected_result = 1
        self.assertEqual(expected_result,actual_result)

    def test_update_item(self):
        result = self.evnt.update_item(32,'sunday','Hiking')
        self.assertTrue(result)

    def testtodo_sun(self):
        result = self.sun.add_item('1:00', 'task')
        self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()
