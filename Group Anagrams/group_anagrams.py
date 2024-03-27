from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram = defaultdict(list)  # mapping charcount to list of anagrams

        # go through each string that we are given
        for s in strs:
            # want to count how many of each letter we have
            count = [0] * 26  # initialize to array of 0

            # we want to go through each character of the string and count
            for c in s:
                count[ord(c) - ord("a")] += 1

            anagram[tuple(count)].append(s)

        return list(anagram.values())

# Time Complexity: (O(N * K)) where N is the number of strings in the input list and K is the maximum length of a string in the list.
# Space Complexity: O(N * K) where N is the number of strings in the input list and K is the maximum length of a string in the list.    