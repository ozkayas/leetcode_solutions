# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = dict()
        maxLevel = 0

        q = deque()
        q.append((root,0))

        while q:
            cur, level = q.popleft()
            if level not in res:
                res[level] = cur.val
                maxLevel = level
            if cur.left: 
                q.append((cur.left, level+1))
            if cur.right:
                q.append((cur.right, level+1))
            
        return res[maxLevel]




        