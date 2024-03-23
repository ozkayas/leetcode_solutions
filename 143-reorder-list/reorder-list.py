# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s , f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next

        #reverse till tail startin from s
        prev = None
        while s:
            s_next = s.next
            s.next = prev
            prev = s
            s = s_next
        
        p1, p2 = head, prev
        while p2 and p2.next:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next



