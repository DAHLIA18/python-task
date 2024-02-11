import unittest

from Assignment import find_intersection, remove_item, sum_collection, duplicate_elements, sum_first_middle_last, \
    add_every_third, eliminate_duplicates, collect_unique_numbers


def construct_sequential_list():
    pass


class Test_main_class_Functions(unittest.TestCase):
    def test_construct_sequential_list(self):
        self.assertEqual(construct_sequential_list(), list(range(1, 16)))

    def test_duplicate_elements(self):
        self.assertEqual(duplicate_elements([1, 2, 3]), [1, 1, 2, 2, 3, 3])

    def test_eliminate_duplicates(self):
        self.assertEqual(eliminate_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_add_every_third(self):
        self.assertEqual(add_every_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 18)

    def test_sum_first_middle_last(self):
        self.assertEqual(sum_first_middle_last([1, 2, 3, 4, 5]), 9)
        self.assertEqual(sum_first_middle_last([1, 2, 3, 4]), 7.5)

    def test_collect_unique_numbers(self):
        self.assertTrue(len(collect_unique_numbers()) == 10)

    def test_sum_collection(self):
        self.assertEqual(sum_collection({1, 2, 3}), 6)

    def test_remove_item(self):
        my_set = {1, 2, 3, 4, 5}
        self.assertEqual(remove_item(my_set, 3), 3)
        self.assertIsNone(remove_item(my_set, 6))

    def test_find_intersection(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        self.assertEqual(find_intersection(set1, set2), {4, 5})


if __name__ == "_main_":
    unittest.main()
