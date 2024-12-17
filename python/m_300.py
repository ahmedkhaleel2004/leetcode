class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # got similar one at PCC, except it was diff=1 only and i sorted it
        # but this dp is smart too
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
