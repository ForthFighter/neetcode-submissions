# Happy that I came up with this in the end, I think it is a good solution. Usefulness of having pen and paper really 

# showed here.

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        if s == '':
            return True
        
        open_brackets_map = { '(' : ')', '[' : ']', '{' : '}'}

        if s[0] not in open_brackets_map:
            return False

        open_bracket = s[0]

        j = 0

        while s[j] not in open_brackets_map.values():
            j += 1
            if j == len(s): # Still didn't find a closed pair
                return False

        if open_brackets_map[s[j-1]] != s[j]:
            return False
        else:
            new_string = s[0:j-1] + s[j+1:]   
            return self.isValid(new_string)

        