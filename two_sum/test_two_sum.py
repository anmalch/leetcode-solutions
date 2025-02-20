import unittest
from two_sum import Solution


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.two_sum([2, 5, 7, 9, 17], 14), [1, 3])

    def test_no_solution(self):
        self.assertEqual(self.solution.two_sum([3, 5, 9, 10], 20), [])

    def test_multiple_pairs(self):
        self.assertEqual(self.solution.two_sum([1, 3, 5, 6], 11), [2, 3])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.two_sum([0, -2, 1, 2], 0), [1, 3])


if __name__ == '__main__':
    unittest.main()
