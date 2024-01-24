class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, num in enumerate(nums):
            target.insert(index[i], num)
        return target
