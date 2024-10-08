class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding_close = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for p in s:
            if p in "{[(":
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                if p != corresponding_close[stack.pop()]:
                    return False
        
        return len(stack) == 0