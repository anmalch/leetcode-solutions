class Solution:
    def is_palindrome(self, x):
        # convert x (int) to string, revers it to use slicing and compare with the original string
        return str(x) == str(x)[::-1]