# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def dfs(node):
            if not node: return
            arr.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        
        dfs(root)
        for i in range(len(arr)):
            if i+1 < len(arr):
                arr[i].right = arr[i+1]
                arr[i].left = None

        return root

        