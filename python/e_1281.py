class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        prod = digits[0]
        for i in digits[1:]:
            prod *= i
        return prod - sum(digits)
