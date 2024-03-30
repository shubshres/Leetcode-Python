class Solution(object):
    # brute force -- BAD APPROACH
    # def twoSumBruteForce(self, nums, target):
    #     for i1, a in enumerate(nums):
    #         for i2, b in enumerate(nums):
    #             if a == b:
    #                 continue
    #             elif a + b == target:
    #                 return [i1, i2]
    #     return []

    def twoSum(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []


print(Solution().twoSum([2, 7, 11, 15], 18))
