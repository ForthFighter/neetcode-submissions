# Neetcode optimal solution using stack.
# Note the use of a list as a truth variable (True if and only if not empty)

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        CloseToOpen = {')':'(', '}' : '{', ']' : '['}

        for c in s:
            if c in CloseToOpen:
                if stack and stack[-1] == CloseToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
        