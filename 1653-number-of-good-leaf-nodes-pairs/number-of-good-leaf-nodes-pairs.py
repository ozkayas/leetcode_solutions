# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Dict, Set

class Solution:
    def getAdjList(self, root: TreeNode) -> (Dict[TreeNode, Set[TreeNode]], Set):
        adj = defaultdict(set)
        leafs = set()

        bfsQ = deque([root])
        while bfsQ:
            curN = bfsQ.popleft()
            # is Leaf
            if not curN.left and not curN.right: leafs.add(curN)
            if curN.left:
                adj[curN].add(curN.left)
                adj[curN.left].add(curN)
                bfsQ.append(curN.left)
            if curN.right:
                adj[curN].add(curN.right)
                adj[curN.right].add(curN)
                bfsQ.append(curN.right)

        return (adj, leafs)
    
    # takes a leaf and find the leafs in distance
    def bfsFromLeaf(self, root: TreeNode, distance: int, leafs: Set, adjList) -> List[int]:
        bfsQ = deque([(root, 0)])
        pairs = []
        visited = set()
        while bfsQ:
            cur, level = bfsQ.popleft()
            visited.add(cur)
            # do not need to look further
            if level > distance: return pairs
            if cur != root and level <= distance and cur in leafs:
                # found a pair for root
                pairs.append(cur)
            
            # add neighbors in bfs
            for neigb in adjList[cur]:
                if neigb not in visited:
                    bfsQ.append((neigb, level+1)) 

        return pairs

    def countPairs(self, root: TreeNode, distance: int) -> int:
        adj, leafs = self.getAdjList(root)
        counter = 0
        # print(leafs)

        for leaf in leafs:
            # do bfs until distance if see a leaf add as a pair
            pairs = self.bfsFromLeaf(leaf, distance, leafs, adj)
            # print(leaf.val)
            # print(pairs)
            counter += len(pairs)

        return counter //2 