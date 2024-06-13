import unittest
import random

from birthdaySnacks.roasted_corn import generate_numbers, generate_random_tuple, sum_odd_positions, sum_even_positions, \
    sum_smallest_largest, unpack_first_five_elements, students_data
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

    def test_generate_random_tuple(self):
        random.seed(15)
        numbers = generate_random_tuple(10)
        self.assertEqual(len(numbers), 10)
        self.assertTrue(all(1 <= num <= 20 for num in numbers))

    def test_sum_odd_positions(self):
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        result = sum_odd_positions(numbers)
        self.assertEqual(result, 30)

        numbers = ()
        result = sum_odd_positions(numbers)
        self.assertEqual(result, 0)

    def test_sum_even_positions(self):
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        result = sum_even_positions(numbers)
        self.assertEqual(result, 25)

    def test_sum_smallest_largest(self):
        numbers = (3, 1, 4, 2, 5)
        result = sum_smallest_largest(numbers)
        self.assertEqual(result, 6)

        numbers = (-3, -1, -4, -2, -5)
        result = sum_smallest_largest(numbers)
        self.assertEqual(result, -6)

    def test_unpack_first_five_elements(self):
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        a, b, c, d, e = unpack_first_five_elements(numbers)
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)
        self.assertEqual(c, 3)
        self.assertEqual(d, 4)
        self.assertEqual(e, 5)

    def test_students_data(self):
        students = students_data()
        self.assertEqual(len(students), 10)
        for count in range(1, 11):
            name = f"Student_{count}"
            self.assertIn(name, students)
            self.assertEqual(students[name], count + 9)

    def test_sort_student(self):
        students = {
            "Student_3": 12,
            "Student_1": 10,
            "Student_2": 11,
            "Student_5": 15,
            "Student_4": 14
        }
        sorted_students = sort_student(students)
        self.assertEqual(list(sorted_students.keys()), ["Student_1", "Student_2", "Student_3", "Student_4", "Student_5"])


if __name__ == '__main__':
    unittest.main()
