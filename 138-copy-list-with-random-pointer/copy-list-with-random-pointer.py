"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        copies = dict()
        cur = head
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copyOfCur = copies[cur]
            if cur.next:
                copyOfCur.next = copies[cur.next]
            if cur.random:
                copyOfCur.random = copies[cur.random]
            cur = cur.next
        
        newHead = copies[head]
        return newHead 
        




        