from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set.__len__ and list.__len__ is implemented in O(1)
        # time complexity in CPython. The set object is also
        # written in C, including the __init__.
        # Basically, this is fast:
        return not len(set(nums)) == len(nums)

        ## Alternative:
        # seen = set()
        # for n in nums:
        #    if n in seen:
        #        return True
        #    seen.add(n)
        # return False

# Set creation implementation in CPython: https://github.com/python/cpython/blob/7487db4c7af629f0a81b2127a3ee0000a288cefc/Objects/setobject.c#L2345
# Set length implementation in CPython: https://github.com/python/cpython/blob/7487db4c7af629f0a81b2127a3ee0000a288cefc/Objects/setobject.c#L575
# List length implementation in CPython: https://github.com/python/cpython/blob/7487db4c7af629f0a81b2127a3ee0000a288cefc/Objects/listobject.c#L587
