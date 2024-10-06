# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = [(root, 0)]
        ans = []
        
        while q:
            cur, level = q.pop()
            if len(ans) == level: 
                ans.append([cur.val])
            else:
                ans[level].append(cur.val)

            if cur.right: q.append((cur.right, level+1))
            if cur.left: q.append((cur.left, level+1))

        
        return ans
