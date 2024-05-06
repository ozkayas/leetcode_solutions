# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        mono_stack = deque([head])
        p = head

        while p:
            while mono_stack and mono_stack[-1].val < p.val:
                mono_stack.pop()
            mono_stack.append(p)
            p = p.next
        
        dummy = ListNode(None)
        last = dummy
        while mono_stack:
            cur = mono_stack.popleft()
            last.next = cur
            last = last.next
        
        return dummy.next


        