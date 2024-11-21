class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        from collections import defaultdict

        ransomNote = ransomNote.lower()
        magazine = magazine.lower()

        countCharMag = defaultdict(int)

        for char in magazine:
            if char.isalnum():
                countCharMag[char] += 1
        
        for char in ransomNote:
            if char in countCharMag and countCharMag[char] > 0:
                countCharMag[char] -= 1
            else:
                return False
        
        return True

