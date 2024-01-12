class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        largest = 0
        x_vals = sorted([x for x, _ in points])

        for i in range(len(x_vals) - 1):
            largest = max(largest, abs(x_vals[i]-x_vals[i+1]))

        return largest
