class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()  # set to store unique characters
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # add it to the charset
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))  # 3
# Time Complexity: O(n)
# The time complexity of the algorithm will be O(N) where ‘N’ is the number of characters in the input string.
# The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

# Space Complexity: O(n)
