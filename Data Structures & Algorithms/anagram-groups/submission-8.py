class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmap of sorted elements to sublists
        hashmap = {}
        for element in strs:
            if ''.join(sorted(element)) in hashmap:
                hashmap[''.join(sorted(element))].append(element)
            else: 
                hashmap[''.join(sorted(element))] = [element]
        
        return list(hashmap.values())

        
            

        