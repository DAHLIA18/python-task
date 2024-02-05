from unittest import TestCase
import Classwork

class Test(TestCase):
    def test_list_length(self):
        numbers = [11, 9, 5, 30, 39, 15, 49, 36, 29]
        Classwork.list_length(numbers)
        self.assertEqual(10, Classwork.list_length(numbers))

    def test_even_positions(self):
        numbers = [11, 9, 5, 30, 39, 15, 49, 36, 29]
        Classwork.even_positions(numbers)
        self.assertEqual(90, Classwork.even_positions(numbers))

    def test_odd_positions(self):
        numbers = [11, 9, 5, 30, 39, 15, 49, 36, 29]
        Classwork.odd_positions(numbers)
        self.assertEqual(133, Classwork.odd_positions(numbers))

    def test_multiply_third_position(self):
        self.fail()

    def test_average(self):
        self.fail()

    def test_largest_element(self):
        self.fail()

    def test_smallest_element(self):
        self.fail()

    def test_get_number_of_strings(self):
            get_number_of_strings: int = sum(1 for word in numbers if word and word[0].lower() == word[-1].lower())
            actualCount: Any = get_number_of_strings(numbers)
            assert actualCount: Any = get_number_of_strings(numbers))