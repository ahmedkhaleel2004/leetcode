class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # its sorted, binary search the idx of the kth missing num since
        # you know how many are missing before at any certain element
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2

            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1

        return left + k
