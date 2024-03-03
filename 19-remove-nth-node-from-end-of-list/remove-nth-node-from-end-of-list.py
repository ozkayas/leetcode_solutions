# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        l , r = dummy, head
        for i in range(n):
            r = r.next
        
        while r:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next


