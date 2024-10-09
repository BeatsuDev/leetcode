### Solution 1: Removing non-alphanumeric characters first
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(
            letter
            for letter in s
            if letter.isalnum()
        )

        i, j = 0, len(s)-1
        while j >= i:
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True
    
### Solution 2: Sliding the two pointers when they are on non-alphanumeric characters
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while j >= i:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True