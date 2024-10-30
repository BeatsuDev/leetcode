class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # The right-most occurence of letters in needle
        letters = {letter: i for i, letter in enumerate(needle)}

        haystack_length = len(haystack)
        needle_length = len(needle)

        i = 0
        while i <= haystack_length - needle_length:
            # Iterate backwards
            j = needle_length - 1
            while j >= 0 and haystack[i+j] == needle[j]:
                j -= 1

            if j < 0:
                return i
            i += max(1, j - letters.get(haystack[i+j], -1))
        return -1
