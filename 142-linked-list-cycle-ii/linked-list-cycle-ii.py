# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

            if s == f: # found a spot, now move f to head as slow2
                f = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        
        return None


        