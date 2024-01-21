class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(banks) for banks in accounts])
