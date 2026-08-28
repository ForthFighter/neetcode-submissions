class Solution:

    # Problem is that [''] and [] each get encoded the same way
    # But [] is very unique, so can just hardcode it away
    # '' gets dealt with properly anyway.

    def encode(self, strs: List[str]) -> str:
        if strs == []: 
            return 'RETURN_NULL_LIST'
        index = 0
        return 'SPACE'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'RETURN_NULL_LIST':
            return []
        Almost_answer = s.split('SPACE')
        return Almost_answer

