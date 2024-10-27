# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSoFar = float("-inf")

        def dfs(node) -> int:
            nonlocal maxSoFar
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            val = max(node.val, node.val + left, node.val + right, node.val + left + right)
            maxSoFar = max(maxSoFar, val)

            return max(node.val, node.val + left, node.val + right)


        dfs(root)
        return maxSoFar

        