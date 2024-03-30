# from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # valuesString = defaultdict(int)
        # valuesString = [0 for i in range(26)]
        valuesString = [0] * 26
        if len(s) != len(t):
            return False
        else:
            for charI in s:
                pos = ord(charI) - ord("a")
                valuesString[pos] += 1

            for charJ in t:
                pos = ord(charJ) - ord("a")
                valuesString[pos] -= 1

        for n in valuesString:
            if n != 0:
                return False
        return True


# Time Complexity :  O(N)
# Space Complexity:  O(1)
