class Solution:
    def two_sum(self, nums, target):
        known_indexes = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in known_indexes:
                return [known_indexes[diff], i]
            known_indexes[num] = i
        return []
