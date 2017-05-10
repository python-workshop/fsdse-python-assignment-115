from unittest import TestCase


class TestBuild(TestCase):
    # check whether the values are there
    # check that the duplicates are removed
    def test_check_whether_the_values_are_there(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result= build("")
        self.assertEqual(False,result)

    def test_check_that_the_duplicates_are_removed(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Error")

        result = build([1,1,2,3])
        self.assertEqual(None, result)
