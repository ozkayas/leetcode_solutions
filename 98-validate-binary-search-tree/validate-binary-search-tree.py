# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Inordertravers - fill array= check if increasing order.
        arr = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            arr.append(node.val)
            if node.right:
                dfs(node.right)


        dfs(root)
        # Check if the array is in strictly increasing order
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False

        return True
        