import unittest

from birthdaySnacks.roasted_corn import generate_numbers
from birthdaySnacks.roasted_corn import count_numbers
from birthdaySnacks.roasted_corn import sum_even_numbers
from birthdaySnacks.roasted_corn import odd_even_numbers
from birthdaySnacks.roasted_corn import product
from birthdaySnacks.roasted_corn import average
from birthdaySnacks.roasted_corn import largest_elements
from birthdaySnacks.roasted_corn import smallest_elements

class MyTestCase(unittest.TestCase):
    def test_generate_numbers(self):
        numbers = generate_numbers()
        self.assertEqual(len(numbers),10)
        self.assertTrue(all(1 <= num <= 50 for num in numbers))

    def test_count_numbers(self):
        numbers = [1, 5, 7, 12, 10, 13, 17]
        self.assertEqual(count_numbers(numbers), 7)

    def test_sum_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sum_even_numbers(numbers), 25)

    def test_sum_odd_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(odd_even_numbers(numbers), 30)

    def test_product_number(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(product(numbers), 162)

    def test_average_of_numbers(self):
        numbers = [12, 11, 5, 8, 3, 15]
        self.assertEqual(average(numbers),5.4)

    def test_largest_numbers(self):
        numbers = [12, 11, 5, 8, 3, 15]
        self.assertEqual(largest_elements(numbers), 15)

    def test_smallest_numbers(self):
        numbers = [12, 11, 5, 8, 3, 15]
        self.assertEqual(smallest_elements(numbers), 3)

if __name__ == '__main__':
    unittest.main()
