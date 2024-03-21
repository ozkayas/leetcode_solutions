# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None

        while p:
            p_next= p.next
            p.next = prev
            prev = p
            p = p_next

        return prev

        