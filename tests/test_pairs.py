import unittest
from src.utils import remove_non_duplicates, get_unique_pairs
from src.models import CArray

class TestPairs(unittest.TestCase):
    """test methods"""

    def test_carray_to_list_valid(self):
        """ Test valid """
        c: CArray = CArray("{1, 2, 3, 4}")
        self.assertEqual(c.to_list(), [1, 2, 3, 4])

    def test_carray_to_list_invalid(self):
        """ Test invalid """
        c: CArray = CArray("{1, a, 3}")
        self.assertEqual(c.to_list(), [])

    def test_get_unique_pairs(self):
        """test get_unique_pairs function"""
        arr: list = [6, 4, 12, 10]
        result: dict = get_unique_pairs(arr)
        self.assertIn(16, result)
        self.assertCountEqual(result[16], [(6, 10), (4, 12)])

    def test_remove_non_duplicates(self):
        """test remove_non_duplicated key-value pairs"""
        dic: dict = {16: [(6, 10), (4, 12)], 18: [(6, 12)]}
        new_dic: dict = remove_non_duplicates(dic)
        self.assertIn(16, new_dic)
        self.assertNotIn(18, new_dic)


if __name__ == '__main__':
    unittest.main()
