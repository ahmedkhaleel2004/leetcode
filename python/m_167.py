class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            # since its sorted:
            if curSum > target:
                # right is too big
                r -= 1
            elif curSum < target:
                # left is too small
                l += 1
            else:
                return [l + 1, r + 1]
