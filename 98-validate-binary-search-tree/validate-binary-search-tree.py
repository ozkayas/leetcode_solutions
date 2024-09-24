# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        ### Solution 1 - easier way
        # Inordertravers - fill array= check if increasing order.
        # arr = []
        # def dfs(node):
        #     if node.left:
        #         dfs(node.left)
        #     arr.append(node.val)
        #     if node.right:
        #         dfs(node.right)


        # dfs(root)
        # # Check if the array is in strictly increasing order
        # for i in range(1, len(arr)):
        #     if arr[i] <= arr[i - 1]:
        #         return False

        # return True


        ## Solution 2
        stack = [(root, -inf, inf)]
        while stack:
            node, lo, hi = stack.pop()
            if lo < node.val < hi:
                if node.left: stack.append((node.left, lo, node.val))
                if node.right: stack.append((node.right, node.val, hi))
            else: return False
        return True  
        