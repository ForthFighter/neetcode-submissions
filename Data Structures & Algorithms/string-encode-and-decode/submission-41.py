#Neetcode solution

class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ''
        for string in strs:
            result += (f'{len(string)}'+'#' + string)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        current_index = 0

        while current_index < len(s):
            word_length = ''
            while True:
                if s[current_index] == '#':
                    current_index += 1
                    break
                word_length += s[current_index]
                if current_index == len(s) - 1:
                    break
                current_index += 1

            word_length = int(word_length)

            result.append(s[current_index: current_index + word_length])
            current_index += word_length

        return result
            
            




            
                
            
