class Solution:

    # Problem is that [''] and [] each get encoded the same way
    # i.e. both go to ''. Let's send [''] to EMPTYQUOTE, by replacing 
    # first, then calling join

    def encode(self, strs: List[str]) -> str:
        if strs == []: return 'RETURN_NULL_LIST'
        index = 0
        #for string in strs:
            #if string == '':
                #strs[index] = 'EMPTYQUOTE'
            #index += 1
        return 'SPACE'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'RETURN_NULL_LIST':
            return []
        Almost_answer = s.split('SPACE')
        #index = 0
        #for string in Almost_answer:
            #if string == 'EMPTYQUOTE':
                #Almost_answer[index] = ''
            #index += 1
        return Almost_answer

