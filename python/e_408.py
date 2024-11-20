class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                steps = 0

                if abbr[abbr_ptr] == "0": return False

                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                
                word_ptr += steps
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                
                word_ptr += 1
                abbr_ptr += 1
            
        return word_ptr == len(word) and abbr_ptr == len(abbr)
            
