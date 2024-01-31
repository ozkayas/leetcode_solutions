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
        if not node : return None
        visited = set()
        clones = dict()
        queue = [node]
        clones[node.val]= Node(node.val)
        
        while queue:  

            cur = queue.pop(0)
            if cur.val in visited: 
                continue
            visited.add(cur.val)
            clone = clones[cur.val] 
            for n in cur.neighbors:
                queue.append(n)
                if n.val in clones:
                    clone.neighbors.append(clones[n.val])
                else:
                    clones[n.val] = Node(n.val)
                    clone.neighbors.append(clones[n.val])


        # # print(clones)
        # print(clones[1].neighbors)
        # print(clones[2].neighbors)
        return clones[node.val]