class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower().replace(' ', '')
        a = new_s
        for c in a:
            if not c.isalpha() and not c in {str(n) for n in range(10)}:
                new_s = new_s.replace(c, '')

        return new_s == new_s[::-1]
        