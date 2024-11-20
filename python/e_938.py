# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        searchStack = [root]

        while searchStack:
            node = searchStack.pop()

            if node:
                if low <= node.val <= high:
                    total += node.val
                if low < node.val:
                    searchStack.append(node.left)
                if node.val < high:
                    searchStack.append(node.right)

        return total
