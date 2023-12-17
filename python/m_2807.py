# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        # https://www.youtube.com/watch?v=RUE0OSkkElE&ab_channel=vanAmsen
        
        # simulatenous assignment -> insert new node and point to next and move curr to next to skip new node
        while curr.next:
           curr.next, curr = ListNode(gcd(curr.val, curr.next.val), curr.next), curr.next
        return head
