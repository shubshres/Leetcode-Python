from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramMap = defaultdict(int)

        if len(s) != len(t):
            return False
        else:
            for charI in s:
                anagramMap[charI] += 1

            for charT in t:
                anagramMap[charT] += 1

            print(anagramMap)

            for i in anagramMap:
                if (anagramMap[i] % 2) != 0:
                    return False
                
            return True


print(Solution.isAnagram(Solution, "aa", "bb"))
