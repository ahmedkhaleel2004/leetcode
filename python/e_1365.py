class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            c = 0
            for j in nums:
                if i > j:
                    c += 1
            arr.append(c)
        return arr
