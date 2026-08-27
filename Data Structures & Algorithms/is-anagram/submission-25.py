# NeetCode Solution for O(1) memory

# Idea is to sort them and then check
# Sorting is O(nlogn) time, though, and can be O(1) memory

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # Python's built-in sort function is 'sorted'

        return sorted(s) == sorted(t)

            

        
        