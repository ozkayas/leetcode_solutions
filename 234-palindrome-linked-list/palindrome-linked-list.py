# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next

        # Final position of S
        # Even numbers: 1 2 3 3 2 1.  s-> second 3
        # Odd numbers: 1 2 3 4 3 2 1   s-> again second 3

        # Reverse the remaining part starting from s

        prev = None
        while s:
            temp = s.next
            s.next = prev
            prev = s 
            s = temp
        
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True

        