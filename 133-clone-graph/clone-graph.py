"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clones = dict()
        q = [node] 
        clones[node] = Node(node.val)

        #BFS Algo 
        while q:
            cur = q.pop(0)

            for nei in cur.neighbors:
                if nei not in clones:
                    q.append(nei)
                    clone = Node(nei.val)
                    clones[nei] = clone
                clones[cur].neighbors.append(clones[nei])

        return clones[node]