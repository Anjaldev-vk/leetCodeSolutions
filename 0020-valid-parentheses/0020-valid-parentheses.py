class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        stack = []

        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                last = stack.pop()
                
                if opening.index(last) != closing.index(ch):
                    return False

        return len(stack) == 0