import unittest
from list_processor import sum_list

class TestListProcessor(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)  # Kesalahan: seharusnya 6

if __name__ == '__main__':
    unittest.main()
