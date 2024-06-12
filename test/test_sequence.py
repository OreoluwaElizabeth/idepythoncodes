import unittest

from birthdaySnacks.sequence import generate_list, duplicate_generate_list, remove_duplicates, add_third_element, \
    unique_numbers, sum_collection, remove_item, find_intersection, find_union, subset, remove_first_element, \
    maximum_and_minimum, set_length


class MyTestCase(unittest.TestCase):
    def test_generate_list(self):
         my_list = generate_list()
         self.assertEqual(len(my_list), 15) # add assertion here

    def test_duplicate_generate_list(self):
        my_list = [1, 2, 3, 4, 5]
        duplicated_list = duplicate_generate_list(my_list)
        self.assertEqual(len(duplicated_list),len(my_list) * 2)
        for item in my_list:
            self.assertEqual(duplicated_list.count(item), 2)

    def test_eliminate_duplicates(self):
        duplicated_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        transformed_list = remove_duplicates(duplicated_list)
        self.assertEqual(len(transformed_list), 5)

    def test_add_third_element(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = 18
        self.assertEqual(add_third_element(lst), expected_result)

        lst = []
        expected_result = 0
        self.assertEqual(add_third_element(lst), expected_result)

        lst = [1, 2, 3]
        expected_result = 3
        self.assertEqual(add_third_element(lst), expected_result)

        lst = [1, 2]
        expected_result = 0
        self.assertEqual(add_third_element(lst), expected_result)

    def test_unique_number(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = set(numbers)
        self.assertEqual(unique_numbers(numbers), expected_result)

        numbers = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
        expected_result = set([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(unique_numbers(numbers), expected_result)

    def test_sum_collection(self):
        collection = [1, 2, 3, 4, 5]
        expected_result = 15
        self.assertEqual(sum_collection(collection), expected_result)

        collection = [-1, -2, -3, -4, -5]
        expected_result = -15
        self.assertEqual(sum_collection(collection), expected_result)

        collection = [1, -2, 3, -4, 5]
        expected_result = 3
        self.assertEqual(sum_collection(collection), expected_result)

        collection = []
        expected_result = 0
        self.assertEqual(sum_collection(collection), expected_result)

        collection = [5]
        expected_result = 5
        self.assertEqual(sum_collection(collection), expected_result)


    def test_remove_item(self):
        my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        removed_element = remove_item(my_set, 10)
        self.assertEqual(removed_element, 10)
        self.assertNotIn(10, my_set)

        my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        removed_element = remove_item(my_set, 11)
        self.assertIsNone(removed_element)
        self.assertEqual(my_set, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        expected_intersection = {4, 5}
        self.assertEqual(find_intersection(set1, set2), expected_intersection)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected_intersection = {3}
        self.assertEqual(find_intersection(set1, set2), expected_intersection)

        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        expected_intersection = set()
        self.assertEqual(find_intersection(set1, set2), expected_intersection)

    def test_find_union(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        expected_union = {1, 2, 3, 4, 5, 6, 7, 8}
        self.assertEqual(find_union(set1, set2), expected_union)

        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected_union = {1, 2, 3, 4, 5}
        self.assertEqual(find_union(set1, set2), expected_union)

        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        expected_union = {1, 2, 3, 4, 5, 6}
        self.assertEqual(find_union(set1, set2), expected_union)

    def test_subset(self):
        set1 = {1, 2, 3}
        set2 = {1, 2, 3, 4, 5}
        self.assertTrue(subset(set1,set2))

        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        self.assertFalse(subset(set1, set2))

    def test_remove_first_element(self):
        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        set1_expected = set()
        set2_expected = {4, 5, 6}
        set1, set2 = remove_first_element(set1, set2)
        self.assertEqual(set1, set1_expected)
        self.assertEqual(set2, set2_expected)

    def test_maxi_mini(self):
        set1 = {1, 2, 3}
        set2 = {4, 5, 6}
        set1_expected = {1, 2, 3}
        set2_expected = {4, 5, 6}
        max_expected = 6
        min_expected = 4
        set1, set2, max_value, min_value = maximum_and_minimum(set1, set2)
        self.assertEqual(set1, set1_expected)
        self.assertEqual(set2, set2_expected)
        self.assertEqual(max_value, max_expected)
        self.assertEqual(min_value, min_expected)

    def test_set_length(self):
        set1 = {1, 2, 3, 4, 5}
        self.assertEqual(set_length(set1), 5)

        set1 = set()
        self.assertEqual(set_length(set1), 0)

        set1 = {1}
        self.assertEqual(set_length(set1), 1)


if __name__ == '__main__':
    unittest.main()
