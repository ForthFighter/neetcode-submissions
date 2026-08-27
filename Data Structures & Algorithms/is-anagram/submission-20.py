# Neetcode version of my idea, with get() method, also more efficient

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        CountS, CountT = {}, {}


        # dict.get() returns value for key, second optional   argument is output if 0 if not a key

        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],0) 
            CountT[t[i]] = 1 + CountT.get(t[i],0)

        for key in CountS:
            if CountS[key] != CountT.get(key,0):
                return False
        # I don't know why he doesn't just return CountS == CountT ?
        
        return True
        
        
        

        

        