import unittest

from problem_001 import get_components_of_sum


class Problem001Test(unittest.TestCase):
    def test_from_example(self):
        self.assertEqual(get_components_of_sum([10, 15, 3, 7], 17), (10, 7))

    def test_from_leetcode_first_example(self):
        self.assertEqual(get_components_of_sum([2, 7, 11, 15], 9), (2, 7))

    def test_from_leetcode_second_example(self):
        self.assertEqual(get_components_of_sum([3, 2, 4], 6), (2, 4))

    def test_from_leetcode_third_example(self):
        self.assertEqual(get_components_of_sum([3, 3], 6), (3, 3))


if __name__ == "__main__":
    unittest.main()
