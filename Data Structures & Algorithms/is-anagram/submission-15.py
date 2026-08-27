class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        # Idea is to have dictionary mapping letter to number of times
        # it shows up

        hashmap_s = {}
        
        for letter in s:
            if letter not in hashmap_s:
                hashmap_s[letter] = 1
            else:
                hashmap_s[letter] += 1

        hashmap_t = dict()

        for letter in t:
            if letter not in hashmap_t:
                hashmap_t[letter] = 1
            else:
                hashmap_t[letter] += 1

        return hashmap_s == hashmap_t




        