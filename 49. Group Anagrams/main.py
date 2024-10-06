from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            # All anagrams of each other are equal when sorted
            key = "".join(sorted(s))
            anagrams[key].append(s)

        return list(anagrams.values())