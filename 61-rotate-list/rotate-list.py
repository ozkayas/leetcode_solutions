# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head


        # First count the length of the list, to use module for k 
        N, p = 1, head
        while p.next:
            p = p.next
            N += 1
        k = k % N
        
        if k == 0: return head
        # print(k,N)

        dummy = ListNode()

        e = head
        # move head k times
        while k and e.next:
            e = e.next
            k -= 1
        # print(f"e: {e.val} - k:{k}")

        p = head
        # move p and e together until e reaches the end
        while e.next:
            p = p.next
            e = e.next
        
        # print(p.val, e.val)
        dummy.next = p.next
        p.next = None
        e.next = head

        return dummy.next

        