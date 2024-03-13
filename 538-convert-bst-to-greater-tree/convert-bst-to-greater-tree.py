# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, i) -> int:
            if not node: return i
            # thisVal = node.val

            fromR = dfs(node.right, i)

            # thisVal += fromR
            # print('setting {} to {}'.format(node.val, node.val+fromR))
            node.val += fromR

            fromL = dfs(node.left,node.val)

            # Do not add from Left to thisVal but pass to parent
            return fromL




        dfs(root,0)
        # print(root.val)

        return root
       