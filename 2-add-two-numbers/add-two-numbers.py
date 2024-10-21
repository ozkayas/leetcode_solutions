# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2, p3 = l1, l2, dummy
        carry = 0

        while p1 or p2 or carry:
            if p1:
                carry += p1.val
                p1 = p1.next
            if p2:
                carry += p2.val
                p2 = p2.next
            
            newNode = ListNode(carry % 10)
            p3.next = newNode
            p3 = p3.next
            carry //= 10
        
        return dummy.next
            
        