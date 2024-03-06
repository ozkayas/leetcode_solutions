# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        if not head or not head.next: return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True

        return False
