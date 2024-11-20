class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(s, i + 1, j) or self.is_palindrome(s, i, j - 1)
            else:
                i += 1
                j -= 1
        
        return True

    def is_palindrome(self, string, i, j):
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
