# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        bfs = deque()
        bfs.append((root,0))
        maxValues = defaultdict(lambda:float("-inf"))

        while bfs:
            cur, level = bfs.popleft()
            maxValues[level] = max(maxValues[level], cur.val)
            if cur.left:
                bfs.append((cur.left, level+1))
            if cur.right:
                bfs.append((cur.right, level+1))

        return [val for val in maxValues.values()]
        