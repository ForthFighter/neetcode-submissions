# Neetcode first solution. I don't think I would come up with this at this point. It seems to be a hard medium.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {} # hashmap to count characters in sliding window
        res = 0 # length of valid substring after replacements

        l = 0 # left pointer 

        for r in range(len(s)): # right pointer just goes through
            count[s[r]] = 1 + count.get(s[r],0) # 

            while (r - l + 1) - max(count.values()) > k: # then can't make entire substring one character, otherwise can. r - l + 1 is length of sliding window.
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res

        

        
        
        
        





        return 
        