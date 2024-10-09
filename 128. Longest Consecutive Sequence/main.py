from typing import List, Set

### Solution 1: Storing the sequences
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums: return 0
        
        sequences: List[List[int]] = []

        for n in nums:
            # This is the start of a new sequence
            if n-1 not in nums:
                sequences.append(self.sequence_at(n, nums))

        longest_sequence = max(sequences, key=len)
        return len(longest_sequence)
    
    def sequence_at(self, n: int, nums: Set[int]) -> List[int]:
        sequence = []
        while n in nums:
            sequence.append(n)
            n += 1
        return sequence


### Solution 2: Without storing the sequences, just the longest sequence length:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)    
    
        longest_sequence = 0
        for n in nums:
            # This is the start of a new sequence
            if n-1 not in nums:
                length = self.sequence_length_at(n, nums)
                longest_sequence = max(longest_sequence, length)

        return longest_sequence
    
    def sequence_length_at(self, n: int, nums: Set[int]) -> int:
        i = 0
        while n+i in nums:
            i += 1
        return i