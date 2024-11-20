"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def distFromTop(n):
            if not n:
                return -1
            return 1 + distFromTop(n.parent)
        
        pDistFromTop = distFromTop(p)
        qDistFromTop = distFromTop(q)

        while pDistFromTop > qDistFromTop:
            p = p.parent
            pDistFromTop -= 1
        while qDistFromTop > pDistFromTop:
            q = q.parent
            qDistFromTop -= 1
        
        while p != q:
            p = p.parent
            q = q.parent
        
        return p
