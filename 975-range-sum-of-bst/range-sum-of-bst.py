# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = [0]
    

        def dfs(root):
            if not root: return
            print(root.val, sum)
            
            if root.val <= high and root.val >= low:
                sum[0] += root.val

            if root.val >= low:
                dfs(root.left)
            if root.val <= high:
                dfs(root.right)


        dfs(root)
        return sum[0]







'''
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        childrenSum = self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        if root.val in range(low, high+1):
            return root.val + childrenSum
        else:
            return childrenSum
        
'''