# This is more or less what I wrote, but much more efficient. The major improvement is using ' while str[j] != '"#" ', which is much more convenient than having a still_reading phase. i and j is maybe cleaner than current_index and a changing word_length, but equivalent.

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += (str(len(s)) + '#' + s)
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # Should use this syntax more

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[ j + 1 : j + 1 + length ])
            i = j + 1 + length

        return res
