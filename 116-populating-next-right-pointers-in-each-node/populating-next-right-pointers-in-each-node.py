"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        bfs = deque([(root, 0)])
        # prev = (node, level) 
        prev = None
        while bfs:
            cur, level = bfs.popleft()
            if prev and prev[1] == level:
                prev[0].next = cur
            prev = (cur, level)
            if cur.left:
                bfs.append((cur.left, level+1)) 
            if cur.right:
                bfs.append((cur.right, level + 1)) 

        return root