# OP NeetCode solution using OP Python Data Structure

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


        