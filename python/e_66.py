class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # my own solution, faster than neetcode?!!!
        if digits[-1] == 9:
            carry = 1
            i = len(digits) - 1
            while carry and i >= 0:
                if digits[i] != 9:
                    carry = 0
                    digits[i] += 1
                    break
                else:   
                    digits[i] = 0 # modifies in place
                i -= 1
            if carry: digits.insert(0, 1)
            return digits
        else:
            digits[-1] += 1
            return digits

        # O(n) worst case where all 9's
