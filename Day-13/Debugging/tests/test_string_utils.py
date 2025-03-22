import unittest
from string_utils import reverse_string

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")  # Kesalahan: seharusnya "olleh"

if __name__ == '__main__':
    unittest.main()
