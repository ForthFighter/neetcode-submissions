class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
   
        left, right = 0, 1
        substring = s[left:right] # Base cases
        best = len(substring)

        while right <= len(s) - 1:
            while s[right] in substring:
                left += 1
                substring = s[left: right]
            right += 1
            substring = s[left: right]
            best = max(best, len(substring))

        return best






