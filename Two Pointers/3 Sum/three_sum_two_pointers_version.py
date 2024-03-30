class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # sort the input array

        for i, a in enumerate(nums):
            # iterate through every value as the possible first array
            # if this isnt the first value and its the same value as before, then continue
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, (len(nums) - 1)
            while l < r:
                total = a + nums[l] + nums[r]

                if total == 0:
                    result.append([a, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l - 1] and l < r:
                        l = l + 1
                elif total > 0:
                    r = r - 1
                elif total < 0:
                    l = l + 1

        return result
