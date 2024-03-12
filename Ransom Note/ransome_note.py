from collections import defaultdict

class Solution(object):
    def canSpell(self, magazine, word):
        # By default all of the letters are init to 0
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1

        for c in word:
            if (letters[c] < 1):
                return False
            else:
                letters[c] -=1

        return True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
