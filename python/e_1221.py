class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        r = 0
        l = 0
        for i, ch in enumerate(s):
            if ch == "R":
                r += 1
            else:
                l += 1
            if r == l:
                count += 1
                r = 0
                l = 0
        return count
            
            
