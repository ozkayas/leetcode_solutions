# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Explanation 
        # https://youtu.be/_-QHfMDde90
        if not root: return None

        if root.val == p.val: return p
        if root.val == q.val: return q

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: return root
        if left: return left
        if right: return right
        # return None


        