from unittest import TestCase
from linked_list import LinkedList

class TestBuild(TestCase):
    def test_check_whether_the_values_are_there(self):
        try:
            from build import remove_dupes
        except ImportError:
            self.assertFalse("no function found")

        linked_list = LinkedList(None)
        remove_dupes(linked_list)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        remove_dupes(linked_list)
        self.assertEqual(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        remove_dupes(linked_list)
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print('Test: General case, no duplicates')
        remove_dupes(linked_list)
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])