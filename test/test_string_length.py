import unittest

from birthdaySnacks.string_length import countstrings


class MyTestCase(unittest.TestCase):
    def test_count_strings(self):
        words = ["hello", "world", "abcba", "radar", "level"]
        self.assertEqual(countstrings(words), 3) # add assertion here

        words = ["nelson", "madam", "elephant"]
        self.assertEqual(countstrings(words), 2)

        words = []
        self.assertEqual(countstrings(words), 0)

if __name__ == '__main__':
    unittest.main()
