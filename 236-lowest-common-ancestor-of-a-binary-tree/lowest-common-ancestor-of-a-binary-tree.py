# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val in [p.val, q.val]:
            return root

        # ask left and right child what do they have in hand ?
        l = r = None
        if root.left:
            l = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            r = self.lowestCommonAncestor(root.right, p, q)
        
        if l and r:
            return root
        if l: return l
        if r: return r
        return None
