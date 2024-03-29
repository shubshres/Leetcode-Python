class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()

        # return newStr == newStr[::-1]

        l = 0
        r = len(s) - 1

        while l < r:
            # check if alpha numeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True

    def alphaNum(self, c):
        # checking if alphanumeric or not
        return (
            (ord("a") <= ord(c) <= ord("z"))
            or (ord("A") <= ord(c) <= ord("Z"))
            or (ord("0") <= ord(c) <= ord("9"))
        )

# Time complexity: O(N)
# Space complexity: O(1)