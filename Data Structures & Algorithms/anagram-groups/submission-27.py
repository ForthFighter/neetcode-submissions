# Neetcode Solution: hashmap key is Counter(str), sort of

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a, ..., z

            for c in s:
                count[ord(c) - ord("a")] += 1 # ASCII values, will map
                # 0 to 25 for a to z respectively. The += 1 counts.
            
            res[tuple(count)].append(s) # tuples can be keys for a dict,
            # and allow duplicates

        return list(res.values())

        



# Lesson is to use the write keys for the hashmap. Sorting is O(nlogn),
# whilst counting is trivially O(n)