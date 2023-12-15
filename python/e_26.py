class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(set(nums))
        nums[:k] = sorted([x for x in set(nums)])
        return k
