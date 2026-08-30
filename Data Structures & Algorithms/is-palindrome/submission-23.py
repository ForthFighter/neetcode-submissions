class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower().replace(' ', '') 
        for c in new_s:
            if not c.isalnum():
                new_s = new_s.replace(c, '')

        return new_s == new_s[::-1]
        