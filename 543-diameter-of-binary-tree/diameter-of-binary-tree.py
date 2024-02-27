# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
    
        def dfs(node) -> int:
            if not node: return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            res[0] = max(res[0], leftDepth+rightDepth)

            return max(leftDepth, rightDepth) + 1

        dfs(root)

        return res[0]