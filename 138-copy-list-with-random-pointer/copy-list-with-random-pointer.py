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
        clones = dict()
        cur = head
        while cur:
            clones[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                clones[cur].next = clones[cur.next]
            if cur.random:
                clones[cur].random = clones[cur.random]
            cur = cur.next

        return clones[head]

        
        