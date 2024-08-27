# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        p3 = newHead
        p1, p2 = l1, l2

        # continue while we still have any of the lists to be processed
        carry = 0
        while p1 or p2 or carry:

            if p1:
                carry += p1.val
                p1 = p1.next
            if p2:
                carry += p2.val
                p2 = p2.next

            # create new Node and add to newList, and move pointer to this node
            node = ListNode(carry % 10)
            p3.next = node
            p3 = node
            carry = carry // 10
        
        return newHead.next