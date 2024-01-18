class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot: # less than or EQUAL to
            row = (top + bot) // 2 # the midpoint
            if target > matrix[row][-1]:
                # if its bigger than the rows biggest element
                top = row + 1 # move it up
            elif target < matrix[row][0]:
                # if its smaller than the smallest element
                bot = row - 1 # move it down
            else:
                break
        # if it wasnt in any of the ranges
        # then top != bot or bigger
        if not (top <= bot):
            return False
        # simple binary search now
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = l + ((r - l) // 2) # no integer overflow as compared to (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
