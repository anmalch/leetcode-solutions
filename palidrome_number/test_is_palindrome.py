import unittest
from palindrome_number import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_palindrome(self):
        self.assertEqual(self.solution.is_palindrome(1221), True)

    def test_is_not_palindrome(self):
        self.assertEqual(self.solution.is_palindrome(1231), False)


if __name__ == '__main__':
    unittest.main()
