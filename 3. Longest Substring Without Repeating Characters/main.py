class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        i = -1
        j = 0
        longest_length = 0
        seen = {}

        while j < len(s):
            if seen.get(s[j], -1) > i:
                i = seen[s[j]]
            else:
                longest_length = max(longest_length, j-i)

            seen[s[j]] = j
            j += 1

        return longest_length
